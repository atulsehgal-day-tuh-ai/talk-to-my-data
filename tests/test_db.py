from src.db_connector import run_query

print(run_query("SHOW TABLES IN SCHEMA SNOWFLAKE_SAMPLE_DATA.TPCH_SF1;"))
