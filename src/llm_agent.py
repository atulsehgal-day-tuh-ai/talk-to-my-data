from utils.config_loader import load_env
load_env()

import os
from sqlalchemy import create_engine
from langchain_openai import ChatOpenAI
from langchain_community.utilities import SQLDatabase
from src.db_connector import get_connection


def _snowflake_engine_from_connector():
    conn = get_connection()

    user = os.getenv("SNOWFLAKE_USER")
    account = os.getenv("SNOWFLAKE_ACCOUNT")
    database = os.getenv("SNOWFLAKE_DB")
    schema = os.getenv("SNOWFLAKE_SCHEMA")
    role = os.getenv("SNOWFLAKE_ROLE")
    warehouse = os.getenv("SNOWFLAKE_WAREHOUSE")

    cur = conn.cursor()
    cur.execute(f"USE ROLE {role}")
    cur.execute(f"USE WAREHOUSE {warehouse}")
    cur.execute(f"USE DATABASE {database}")
    cur.execute(f"USE SCHEMA {schema}")
    cur.close()

    url = f"snowflake://{user}@{account}/{database}/{schema}"
    engine = create_engine(url, creator=lambda: conn)

    return engine, database, schema


def get_agent():
    engine, database, schema = _snowflake_engine_from_connector()
    db = SQLDatabase(engine=engine)

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    def generate_sql(question: str) -> str:
        tables = db.get_table_info()
        prompt = f"""
                    You are a Snowflake SQL expert.

                    Database: {database}
                    Schema: {schema}

                    Tables:
                    {tables}

                    Rewrite the following user question as a valid SQL query.
                    Do NOT include backticks, markdown, or triple quotes.
                    Return ONLY the SQL.

                    Question: {question}
                    """
        return llm.invoke(prompt).content.strip()

    return generate_sql, db
