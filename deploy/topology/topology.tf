
# KMS Part

resource "aws_kms_grant" "kms_grant" {
  name              = "bailiff-grant"
  key_id            = "${data.aws_kms_key.kms_key.id}"
  grantee_principal = "${aws_iam_role.iam_role.arn}"
  operations        = [ "Encrypt", "Decrypt", "DescribeKey", "CreateGrant" ]
}


# IAM Part

resource "aws_iam_role" "iam_role" {
  name = "bailiff-role"
  force_detach_policies = true

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

resource "aws_iam_policy" "read_ec2_policy" {
  name        = "bailiff_read_ec2"
  path        = "/"
  description = "Allows bailiff to read all ec2 objects"

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "ec2:Describe*"
      ],
      "Effect": "Allow",
      "Resource": "*"
    }
  ]
}
EOF
}

resource "aws_iam_role_policy_attachment" "readec2-attach" {
    role       = "${aws_iam_role.iam_role.name}"
    policy_arn = "${aws_iam_policy.read_ec2_policy.arn}"
}

# Lambda Part

resource "aws_lambda_function" "bailiff_lambda" {
  filename         = "../../package/package.zip"
  function_name    = "bailiff"
  role             = "${aws_iam_role.iam_role.arn}"
  handler          = "main.event_handler"
  source_code_hash = "${base64sha256(file("../../package/package.zip"))}"
  runtime          = "python3.6"

  kms_key_arn      = "${data.aws_kms_key.kms_key.arn}"
  environment {
    variables = {
      SLACK_API_TOKEN = "test_token"
    }
  }
}
