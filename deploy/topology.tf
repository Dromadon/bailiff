#KMS Part

resource "aws_kms_key" "kms_key" {
  description             = "Bailiff kms key"
}

resource "aws_kms_alias" "kms_key_alias" {
  name          = "alias/bailiff"
  target_key_id = "${aws_kms_key.kms_key.key_id}"
}

resource "aws_kms_grant" "kms_grant" {
  name              = "bailiff-grant"
  key_id            = "${aws_kms_key.kms_key.key_id}"
  grantee_principal = "${aws_iam_role.iam_role.arn}"
  operations        = [ "Encrypt", "Decrypt", "DescribeKey", "CreateGrant" ]
}


# IAM Part

resource "aws_iam_role" "iam_role" {
  name = "bailiff-role"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

# Lambda Part

resource "aws_lambda_function" "bailiff_lambda" {
  filename         = "../package/package.zip"
  function_name    = "bailiff"
  role             = "${aws_iam_role.iam_role.arn}"
  handler          = "main.main"
  source_code_hash = "${base64sha256(file("../package/package.zip"))}"
  runtime          = "python3.6"

  kms_key_arn      = "${aws_kms_key.kms_key.arn}"
  environment {
    variables = {
      SLACK_API_TOKEN = "test_token"
    }
  }
}
