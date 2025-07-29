resource "aws_instance" "airflow_server" {
  ami                    = var.ami_id
  instance_type          = var.instance_type
  key_name               = var.key_name
  iam_instance_profile   = var.iam_instance_role
  vpc_security_group_ids = [var.sg_id]

  tags = {
    Name    = "Airflow-ETL-Server"
    Project = "Airflow-ETL-Portfolio"
  }
}
