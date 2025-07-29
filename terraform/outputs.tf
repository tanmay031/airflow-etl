output "ec2_public_ip" {
  description = "Public IP of the Airflow EC2 instance"
  value       = module.ec2_airflow.public_ip
}

output "s3_bucket_name" {
  description = "S3 bucket name for ETL data lake"
  value       = module.s3_datalake.bucket_name
}
