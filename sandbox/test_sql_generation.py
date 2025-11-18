"""
Streamlit app: NL question -> SQL (via LangChain) -> run on Snowflake -> show results.
"""

# --- Path and environment setup ---------------------------------------------
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.config_loader import load_env

load_env()

import pandas as pd

from src.llm_agent import get_agent

question = "how many orders in last 1 year?"

generate_sql, db = get_agent()

sql = generate_sql(question)

print(sql)
print(db)


#rows = db.run(sql)

#print(rows)

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
        print(value)
    else:
        # Generic table case
        df = pd.DataFrame(rows)
        st.subheader("Results")
        st.dataframe(df)