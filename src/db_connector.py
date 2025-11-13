"""
This module provides functionality to connect to a Snowflake database and execute SQL queries.
Functions:
    - get_connection(): Establishes and returns a connection to the Snowflake database using credentials and settings from environment variables.
    - run_query(sql: str): Executes a given SQL query on the Snowflake database and returns the results.
Environment Variables:
    - SNOWFLAKE_USER: The username for the Snowflake account.
    - SNOWFLAKE_PASSWORD: The password for the Snowflake account.
    - SNOWFLAKE_ACCOUNT: The Snowflake account identifier.
    - SNOWFLAKE_WAREHOUSE: (Optional) The Snowflake warehouse to use. Defaults to "COMPUTE_WH".
    - SNOWFLAKE_DB: The name of the Snowflake database to connect to.
    - SNOWFLAKE_SCHEMA: The schema within the Snowflake database to use.
"""
from utils.config_loader import load_env
load_env()

import snowflake.connector
import os

def get_connection():
    return snowflake.connector.connect(
                    user=os.getenv("SNOWFLAKE_USER"),
                    password=os.getenv("SNOWFLAKE_PASSWORD"),
                    account=os.getenv("SNOWFLAKE_ACCOUNT"),
                    authenticator=os.getenv("SNOWFLAKE_AUTHENTICATOR"),
                    role=os.getenv("SNOWFLAKE_ROLE")
                    )

def run_query(sql: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result
