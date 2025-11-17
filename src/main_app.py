"""
Streamlit app: NL question -> SQL (via LangChain) -> run on Snowflake -> show results.
"""

# --- Path and environment setup ---------------------------------------------
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.config_loader import load_env

load_env()

# --- Application imports ----------------------------------------------------
import streamlit as st
import pandas as pd

from src.llm_agent import get_agent
from utils.helper import normalize_rows


st.title("💬 Talk to My Data – Hybrid (LLM + Snowflake)")

question = st.text_input("Ask a question about your data:")

if question:
    
    generate_sql, db = get_agent()

    sql = generate_sql(question)

    st.subheader("Generated SQL")
    st.code(sql, language="sql")

    try:
        raw = db.run(sql)
    except Exception as e:
        st.error(f"Query failed: {e}")
    else:
        result = normalize_rows(raw)

        if result is None:
            st.info("No rows returned.")

        elif isinstance(result, pd.DataFrame):
            st.subheader("Results")
            st.dataframe(result)

        else:
            # Scalar result
            st.metric("Value", result)
