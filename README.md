Intelligent Cloud Monitoring & Security Alert System

This project automatically monitors logs stored in an S3 bucket and sends alerts through AWS SNS whenever an ERROR event is detected.

 Components Used
- AWS EC2 (for uploading log files)
- AWS S3 (log storage)
- AWS Lambda (log analyzer)
- AWS SNS (alert notifications)
- AWS IAM (permissions)
- EventBridge (triggers)

 How It Works
1. EC2 uploads logs to S3  
2. S3 upload triggers Lambda  
3. Lambda scans logs  
4. If `ERROR` is found → SNS sends email alert  

 Project Files
- `lambda_function.py` – Lambda alert function  
- `cloudwatch-agent-config.json` – EC2 monitoring config  
- `requirements.txt` – dependencies  
- `sample-error.log` – sample log for testing  

 Testing
```bash
echo "ERROR server crash" > sample-error.log
aws s3 cp sample-error.log s3://your-bucket-name/
