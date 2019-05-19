### Automate deletion of unattached EBS volumes

EBS volumes cost $0.10 per GB/month.
This Lambda function will:
  - Go through all regions in your account. 
  - Delete EBS volumes that are unattached (labeled "available").
  
### Steps: 

1. Give Lambda permission to perform EBS actions (JSON file). 
2. Create a Lambda function and paste the code. 
3. Configure CloudWatch to execute the Lambda function every day (event rule). 

Lots of potential cost savings with this as unused EBS volumes can be overlooked. 
