# create a array based table in bigquery and once the table is created, 
# add a new column after every load(share the configuration),
# and load a file(csv or json) which have blank values in some records ,handle this load 

from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()


table_id = "dataset.table_name"

# Create table
schema = [
    bigquery.SchemaField("id", "INTEGER", mode="REQUIRED"),
]

table = bigquery.Table(table_id, schema=schema)
table = client.create_table(table)  # Make an API request.

# Load new JSON file

job_config = bigquery.LoadJobConfig(
    autodetect=True, source_format=bigquery.SourceFormat.CSV, null_marker=" "
) #Activate auto-detect schema, treat empty space as null

uri = "gs://path/to/file.csv"
load_job = client.load_table_from_uri(
    uri, table_id, job_config=job_config
)  # Make an API request.
load_job.result() 
destination_table = client.get_table(table_id)