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

from llm_agent import get_agent


st.title("💬 Talk to My Data – Hybrid (LLM + Snowflake)")

question = st.text_input("Ask a question about your data:")

if question:
    # 1) Get chain + DB
    chain, db = get_agent()

    # 2) NL -> SQL (chain is in *SQL-only* mode)
    sql = chain.invoke({"question": question})

    st.subheader("Generated SQL")
    st.code(sql, language="sql")

    # 3) Execute SQL on Snowflake
    try:
        rows = db.run(sql)  # typically a list of tuples, e.g. [(6001215,)]
    except Exception as e:
        st.error(f"Query failed: {e}")
    else:
        if not rows:
            st.info("No rows returned.")
        # Single aggregated value, e.g. COUNT(*)
        elif (
            isinstance(rows, list)
            and len(rows) == 1
            and isinstance(rows[0], (list, tuple))
            and len(rows[0]) == 1
        ):
            value = rows[0][0]
            st.subheader("Result")
            st.metric(label="Value", value=value)
            # Optional: show raw rows for debugging
            st.caption(f"Raw rows: {rows}")
        else:
            # Generic table case
            df = pd.DataFrame(rows)
            st.subheader("Results")
            st.dataframe(df)
