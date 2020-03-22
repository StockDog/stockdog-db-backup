import json
import os
import time
import datetime
import boto3

def lambda_handler(event, context):
    DATABASE_HOST = os.getenv("DATABASE_HOST")
    DATABASE_NAME = os.getenv("DATABASE_NAME")
    DATABASE_USER = os.getenv("DATABASE_USER")
    DATABASE_PASS = os.getenv("DATABASE_PASS")

    S3_BUCKET = os.getenv("S3_BUCKET")

    DATETIME = time.strftime('%Y%m%d-%H%M%S')

    file_name = f"/tmp/{DATETIME}.sql"

    dumpcmd = f"./mysqldump -h {DATABASE_HOST} -u{DATABASE_USER} -p{DATABASE_PASS} {DATABASE_NAME} > {file_name}"
    os.system(dumpcmd)

    # Upload the file
    s3_client = boto3.client('s3')
    response = s3_client.upload_file(file_name, S3_BUCKET, f'{DATETIME}.sql')
    return response
