resource "aws_s3_bucket" "etl_bucket" {
  bucket = var.s3_bucket_name

  tags = {
    Name    = "ETL-DataLake"
    Project = "Airflow-ETL-Portfolio"
  }
}

resource "aws_s3_bucket_versioning" "versioning" {
  bucket = aws_s3_bucket.etl_bucket.id
  versioning_configuration {
    status = "Enabled"
  }
}
