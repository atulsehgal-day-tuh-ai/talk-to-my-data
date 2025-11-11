

"""
This module provides functionality to create an SQLDatabaseChain instance 
using a Snowflake database connection and a language model from LangChain.
Functions:
----------
- get_sql_chain():
    Establishes a connection to a Snowflake database using credentials and 
    configuration from environment variables. It initializes a ChatOpenAI 
    language model and returns an SQLDatabaseChain instance for executing 
    SQL queries.
Environment Variables:
----------------------
- SNOWFLAKE_USER: The username for the Snowflake account.
- SNOWFLAKE_PASSWORD: The password for the Snowflake account.
- SNOWFLAKE_ACCOUNT: The Snowflake account identifier.
- SNOWFLAKE_DB: The name of the Snowflake database.
- SNOWFLAKE_SCHEMA: The schema within the Snowflake database.
- SNOWFLAKE_WAREHOUSE: (Optional) The Snowflake warehouse to use. Defaults to 'COMPUTE_WH'.
Dependencies:
-------------
- langchain.chat_models.ChatOpenAI: For initializing the language model.
- langchain.chains.SQLDatabaseChain: For creating the SQL chain.
- langchain.sql_database.SQLDatabase: For connecting to the Snowflake database.
- os: For accessing environment variables.
"""

from langchain.chat_models import ChatOpenAI
from langchain.chains import SQLDatabaseChain
from langchain.sql_database import SQLDatabase
import os

def get_sql_chain():
    db_uri = f"snowflake://{os.getenv('SNOWFLAKE_USER')}:{os.getenv('SNOWFLAKE_PASSWORD')}@" \
             f"{os.getenv('SNOWFLAKE_ACCOUNT')}/{os.getenv('SNOWFLAKE_DB')}/{os.getenv('SNOWFLAKE_SCHEMA')}?" \
             f"warehouse={os.getenv('SNOWFLAKE_WAREHOUSE','COMPUTE_WH')}"
    db = SQLDatabase.from_uri(db_uri)
    llm = ChatOpenAI(model="gpt-4o", temperature=0)
    return SQLDatabaseChain.from_llm(llm, db, verbose=True)