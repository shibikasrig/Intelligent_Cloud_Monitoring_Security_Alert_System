import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.client("s3")
    sns = boto3.client("sns")

    bucket = event["Records"][0]["s3"]["bucket"]["name"]
    file_name = event["Records"][0]["s3"]["object"]["key"]

    file_obj = s3.get_object(Bucket=bucket, Key=file_name)
    file_content = file_obj["Body"].read().decode("utf-8")

    if "ERROR" in file_content:
        sns.publish(
            TopicArn="arn:aws:sns:us-east-1:551507899771:intelligent-monitoring-alerts",
            Message=f"Alert! Error detected in log file: {file_name}\n\nContent:\n{file_content}",
            Subject="Cloud Monitoring Alert"
        )

    return {"status": "processed"}
