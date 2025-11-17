def clean_sql(sql: str) -> str:
    return (
        sql.replace("```sql", "")
           .replace("```", "")
           .strip()
    )
