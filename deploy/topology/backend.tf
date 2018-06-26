terraform {
  backend "s3" {
    bucket = "bailiff"
    key    = "topology"
    region = "eu-west-1"
  }
}

provider "aws" {
    version = "~> 1.24"
}

data "aws_kms_key" "kms_key" {
  key_id = "alias/bailiff_key"
}


