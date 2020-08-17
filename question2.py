# How do you handle the load a file having size > 2gb from google cloud storage to a bigquery table by python


from google.cloud import bigquery


client = bigquery.Client()

# First, set the table ID for destination table
table_id = "dataset.table_name"

# Setup configurtion which allow large result and using legacy SQL
job_config = bigquery.QueryJobConfig(
    allow_large_results=True, destination=table_id, use_legacy_sql=True
)

sql_query = """
    SELECT column
    FROM [bigquery-data:tables.table];
"""

# Start the query with the specified configuration.
query_job = client.query(sql_query, job_config=job_config)  
query_job.result() 