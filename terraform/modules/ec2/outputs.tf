output "public_ip" {
  description = "Public IP of EC2 instance"
  value       = aws_instance.airflow_server.public_ip
}
