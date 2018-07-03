terraform {
  backend "s3" {}
}

provider "aws" {
    version = "~> 1.24"
}

data "aws_kms_key" "kms_key" {
  key_id = "alias/bailiff_key_${var.ENV}"
}


