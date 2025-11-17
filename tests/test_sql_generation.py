"""
Test script to verify:
1. SQL-only generation (LLM → SQL)
2. Full database.schema table naming
3. Successful execution of generated SQL in Snowflake
"""

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from utils.config_loader import load_env
load_env()

from llm_agent import get_agent


def test_sql_generation():
    print("\n🔍 Initializing SQL agent...")
    chain, db, database, schema = get_agent()

    print(f"Using database: {database}")
    print(f"Using schema: {schema}")

    nl_question = "What is the row count of lineitem?"
    print(f"\n🗣 Natural language question:\n{nl_question}")

    # --- 1) Generate SQL -----------------------------------------------------
    sql = chain.invoke({"query": nl_question})

    print("\n📝 Generated SQL:")
    print(sql)

    # Validation: ensure database + schema appear in SQL
    assert database in sql, "❌ Database not found in SQL!"
    assert schema in sql, "❌ Schema not found in SQL!"

    # --- 2) Run SQL in Snowflake --------------------------------------------
    print("\n🏃 Executing SQL in Snowflake...")
    try:
        rows = db.run(sql)
        print("\n📊 Query results:")
        print(rows)
        print("\n✅ SQL generation + execution successful.\n")

    except Exception as e:
        print("\n❌ SQL execution failed:")
        print(e)
        raise e


if __name__ == "__main__":
    test_sql_generation()
