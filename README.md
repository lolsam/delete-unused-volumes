# Automate deletion of unattached EBS volumes

EBS volumes cost $0.10 per GB/month.
This Lambda function will:
  - Go through all regions in your account
  - Delete EBS volumes that are unattached (labeled "available").

1. Give Lambda permission to perform EBS actions
2. Create a Lambda function and paste the code
3. Configure CloudWatch to execute the Lambda function every day
