output "sg_id" {
  description = "Security group ID"
  value       = aws_security_group.airflow_sg.id
}
