
"""
This script creates a Streamlit web application that allows users to interact with their Snowflake data 
using natural language queries. The application leverages a language model agent to convert user questions 
into SQL queries and fetch relevant data.
Modules:
- `streamlit`: Used to build the web application interface.
- `llm_agent`: Contains the `get_sql_chain` function to initialize the language model agent.
Key Components:
- The app displays a title "💬 Talk to My Data (Hybrid Mode)".
- Users can input their questions about Snowflake data in a text input field.
- When a question is submitted, the app uses the language model agent to process the query and fetch the response.
- A spinner is displayed while the agent processes the query.
Functions:
- `get_sql_chain()`: Initializes and returns the SQL chain object for processing queries.
Usage:
- Run the script in a Python environment with Streamlit installed.
- Open the Streamlit app in a web browser and input questions about your Snowflake data.
"""
import streamlit as st
from llm_agent import get_sql_chain

st.title("💬 Talk to My Data (Hybrid Mode)")

chain = get_sql_chain()
question = st.text_input("Ask me about your Snowflake data:")

if question:
    with st.spinner("Thinking..."):
        response = chain.run(question)
        st.write(response)
