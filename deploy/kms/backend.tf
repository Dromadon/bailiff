terraform {
  backend "s3" {
    bucket = "bailiff"
    key    = "kms"
    region = "eu-west-1"
  }
}

provider "aws" {
    version = "~> 1.24"
}

data "aws_caller_identity" "current" {}
