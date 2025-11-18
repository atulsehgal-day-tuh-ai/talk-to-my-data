"""
This script establishes a connection to a Snowflake database and retrieves the current account, user, 
and role information. It uses environment variables to securely fetch the connection credentials.
Modules:
    - snowflake.connector: Provides the Snowflake Python Connector to interact with the Snowflake database.
    - os: Used to access environment variables for secure credential management.
Environment Variables:
    - SNOWFLAKE_USER: The username for the Snowflake account.
    - SNOWFLAKE_ACCOUNT: The Snowflake account identifier.
    - SNOWFLAKE_AUTHENTICATOR: The authentication method for connecting to Snowflake.
    - SNOWFLAKE_ROLE: The role to be used for the session.
Steps:
    1. Establish a connection to the Snowflake database using the credentials from environment variables.
    2. Create a cursor object to execute SQL queries.
    3. Execute a query to fetch the current account, user, and role information.
    4. Print the results of the query.
    5. Close the cursor and the connection to release resources.
Note:
    Ensure that the required environment variables are set before running this script.
    Example:
        export SNOWFLAKE_USER="your_username"
        export SNOWFLAKE_ACCOUNT="your_account"
        export SNOWFLAKE_AUTHENTICATOR="your_authenticator"
        export SNOWFLAKE_ROLE="your_role"
"""

from utils.config_loader import load_env
load_env()

import os
print("SNOWFLAKE_USER:", os.getenv("SNOWFLAKE_USER"))
print("SNOWFLAKE_ACCOUNT:", os.getenv("SNOWFLAKE_ACCOUNT"))
print("SNOWFLAKE_AUTHENTICATOR:", os.getenv("SNOWFLAKE_AUTHENTICATOR"))
print("SNOWFLAKE_PASSWORD:", "✅ Loaded" if os.getenv("SNOWFLAKE_PASSWORD") else "❌ EMPTY")

import snowflake.connector

conn = snowflake.connector.connect(
    user=os.getenv("SNOWFLAKE_USER"),
    password=os.getenv("SNOWFLAKE_PASSWORD"),
    account=os.getenv("SNOWFLAKE_ACCOUNT"),
    authenticator=os.getenv("SNOWFLAKE_AUTHENTICATOR"),
    role=os.getenv("SNOWFLAKE_ROLE"),
)

cur = conn.cursor()
cur.execute("SELECT CURRENT_ACCOUNT(), CURRENT_USER(), CURRENT_ROLE();")
print(cur.fetchall())
cur.close()
conn.close()
