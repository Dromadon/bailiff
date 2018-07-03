terraform {
  backend "s3" {}
}

provider "aws" {
    version = "~> 1.24"
}

data "aws_caller_identity" "current" {}
