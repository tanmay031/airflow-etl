module "iam_ec2_s3" {
  source = "./modules/iam"
}

module "security_group" {
  source = "./modules/security_groups"
}

module "s3_datalake" {
  source          = "./modules/s3"
  s3_bucket_name  = var.s3_bucket_name
}

module "ec2_airflow" {
  source            = "./modules/ec2"
  ami_id            = var.ami_id
  instance_type     = var.instance_type
  key_name          = var.key_name
  iam_instance_role = module.iam_ec2_s3.iam_instance_profile_name
  sg_id             = module.security_group.sg_id
}
