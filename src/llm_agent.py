"""
LangChain SQL Agent for Snowflake using existing db_connector.
Fully compatible with SQLAlchemy + LangChain introspection.
"""

from utils.config_loader import load_env
load_env()

import os
from sqlalchemy import create_engine
from langchain_openai import ChatOpenAI
from langchain_experimental.sql.base import SQLDatabaseChain
from langchain_community.utilities import SQLDatabase
from db_connector import get_connection


def _snowflake_engine_from_connector():
    """
    Create a SQLAlchemy engine that wraps the Snowflake connector connection.
    Ensures proper DB + SCHEMA context without breaking SQLAlchemy reflection.
    """

    conn = get_connection()

    # Required env vars
    user = os.getenv("SNOWFLAKE_USER")
    account = os.getenv("SNOWFLAKE_ACCOUNT")
    role = os.getenv("SNOWFLAKE_ROLE")
    warehouse = os.getenv("SNOWFLAKE_WAREHOUSE") or "COMPUTE_WH"
    database = os.getenv("SNOWFLAKE_DB") or "SNOWFLAKE_SAMPLE_DATA"
    schema = os.getenv("SNOWFLAKE_SCHEMA") or "TPCH_SF1"

    # Set the session context (correct way)
    cur = conn.cursor()
    cur.execute(f"USE DATABASE {database}")
    cur.execute(f"USE SCHEMA {schema}")
    cur.execute(f"USE ROLE {role}")
    cur.execute(f"USE WAREHOUSE {warehouse}")
    cur.close()

    print(f"🔗 Connected to Snowflake as {user} | DB={database} | Schema={schema} | Role={role}")

    # IMPORTANT:
    # Do NOT include database/schema in the URL path.
    # SQLAlchemy gets schema separately via SQLDatabase(schema="...").
    url = f"snowflake://{user}@{account}"

    # Wrap the existing Snowflake connector session
    engine = create_engine(
        url,
        creator=lambda: conn,  # reuse existing authenticated connection
    )

    return engine, schema  # RETURN ONLY SCHEMA, NOT database.schema


def get_agent(verbose: bool = True):
    """
    Returns (chain, db):
    - chain: LangChain SQL agent (LLM → SQL → Execution)
    - db: SQLDatabase wrapper for Snowflake
    """

    engine, schema = _snowflake_engine_from_connector()

    # Only pass schema="TPCH_SF1" (NOT "DB.SCHEMA")
    db = SQLDatabase(engine=engine, schema=schema)

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    chain = SQLDatabaseChain.from_llm(
        llm,
        db,
        verbose=verbose
    )

    return chain, db
