variable "ami_id" {
  type        = string
  description = "Ubuntu AMI ID"
}

variable "instance_type" {
  type        = string
  description = "EC2 instance type"
}

variable "key_name" {
  type        = string
  description = "SSH key pair name"
}

variable "iam_instance_role" {
  type        = string
  description = "IAM instance profile name for EC2"
}

variable "sg_id" {
  type        = string
  description = "Security group ID for EC2 instance"
}
