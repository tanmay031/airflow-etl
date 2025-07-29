resource "aws_iam_role" "ec2_s3_role" {
  name = "AirflowEC2S3AccessRole"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Principal = {
        Service = "ec2.amazonaws.com"
      }
      Action = "sts:AssumeRole"
    }]
  })
}

resource "aws_iam_role_policy" "ec2_s3_policy" {
  name = "AirflowEC2S3AccessPolicy"
  role = aws_iam_role.ec2_s3_role.id
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Action = ["s3:*"]
      Resource = "*"
    }]
  })
}

resource "aws_iam_instance_profile" "ec2_s3_profile" {
  name = "AirflowEC2S3Profile"
  role = aws_iam_role.ec2_s3_role.name
}
