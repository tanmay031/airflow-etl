# AWS Region
variable "region" {
  type        = string
  description = "AWS region where resources will be deployed"
  default     = "eu-north-1"
}

# AWS CLI Profile
variable "profile" {
  type        = string
  description = "AWS CLI profile to use for authentication"
  default     = "prahman"
}

# EC2 AMI ID
variable "ami_id" {
  type        = string
  description = "Ubuntu 22.04 AMI ID for the selected region"
  default     = "ami-0914547665e6a707c"
}

# EC2 Instance Type
variable "instance_type" {
  type        = string
  description = "Instance type for Airflow EC2 server"
  default     = "t2.micro"
}

# Key Pair for SSH Access
variable "key_name" {
  type        = string
  description = "Existing AWS key pair name to SSH into EC2 instance"
  default     = "terraform-bastion-key"
}

# S3 Bucket Name
variable "s3_bucket_name" {
  type        = string
  description = "S3 bucket name for storing raw and processed ETL data"
  default     = "etl-datalake-portfolio"
}
