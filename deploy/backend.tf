terraform {
  backend "s3" {
    bucket = "bailiff"
    key    = "terraform"
    region = "eu-west-1"
  }
}

provider "aws" {
    version = "~> 1.22"
}
