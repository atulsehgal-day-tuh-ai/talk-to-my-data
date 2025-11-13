"""
This Streamlit application allows users to interact with their data using natural language queries.
It combines the power of a Large Language Model (LLM) and Snowflake database to generate SQL queries
from user input and execute them on the database.
"""

# --- Path and environment setup ---------------------------------------------
import sys, os

# Ensure project root (/src parent) is available for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Load environment variables
from utils.config_loader import load_env
load_env()

# --- Application imports ----------------------------------------------------
import streamlit as st
from llm_agent import get_agent


st.title("💬 Talk to My Data – Hybrid (LLM + Snowflake)")

question = st.text_input("Ask a question about your data:")

if question:
    chain, db = get_agent()

    # --- 1) Run chain to generate SQL ---------------------------------------
    response = chain.invoke({"query": question})

    # Extract ONLY the SQL string
    sql = response.get("result")

    st.subheader("Generated SQL")
    st.code(sql, language="sql")

    # --- 2) Run SQL on Snowflake -------------------------------------------
    try:
        rows = db.run(sql)  # rows is a list of tuples
        if not rows:
            st.info("No rows returned.")
        else:
            st.subheader("Results")
            st.dataframe(rows)
    except Exception as e:
        st.error(f"Query failed: {e}")
