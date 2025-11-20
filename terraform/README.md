# Terraform Infrastructure for Airflow ETL

This Terraform setup deploys the required AWS infrastructure for the Airflow ETL project.

---

## AWS Configuration Information (variables.tf)

The Terraform configuration uses two key variables to control how and where resources are deployed:

- **region** — Specifies the AWS region where all infrastructure will be created.  
  The default value `eu-north-1` ensures that all resources (EC2, S3, IAM) are provisioned within the Stockholm region.

- **profile** — Specifies the AWS CLI profile Terraform should use for authentication.  
  The default value `prahman` tells Terraform to use the AWS credentials stored under the `prahman` profile in `~/.aws/credentials`.

These variables allow you to easily switch AWS profiles or deploy to a different region without modifying any other Terraform files.

---

## Basic Usage Steps

1. Initialize Terraform:
```
terraform init
```

2. Review planned resource creation:
```
terraform plan
```

3. Deploy the infrastructure:
```
terraform apply
```

4. Destroy the infrastructure when needed:
```
terraform destroy
```

Terraform will automatically use the AWS region and CLI profile mentioned above.
