# Variables
variable "SLACK_API_TOKEN" {}
variable "ASKBOB_ID" {}
variable "ASKBOB_SECRET" {}
variable "SLACK_CHANNEL" {}
variable "ENV" {}
variable "CRON_EXPRESSION" {}

# KMS Part

resource "aws_kms_grant" "kms_grant" {
  name              = "bailiff-grant-${var.ENV}"
  key_id            = "${data.aws_kms_key.kms_key.id}"
  grantee_principal = "${aws_iam_role.iam_role.arn}"
  operations        = [ "Encrypt", "Decrypt", "DescribeKey", "CreateGrant" ]
}


# IAM Part

resource "aws_iam_role" "iam_role" {
  name = "bailiff-role-${var.ENV}"
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
  name        = "bailiff_read_ec2_${var.ENV}"
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
  function_name    = "bailiff-${var.ENV}"
  role             = "${aws_iam_role.iam_role.arn}"
  handler          = "main.event_handler"
  source_code_hash = "${base64sha256(file("../../package/package.zip"))}"
  runtime          = "python3.6"
  timeout          = 20

  kms_key_arn      = "${data.aws_kms_key.kms_key.arn}"
  environment {
    variables = {
      SLACK_API_TOKEN = "${var.SLACK_API_TOKEN}",
      SLACK_CHANNEL = "${var.SLACK_CHANNEL}",
      ASKBOB_ID = "${var.ASKBOB_ID}",
      ASKBOB_SECRET = "${var.ASKBOB_SECRET}"
    }
  }
}

resource "aws_lambda_permission" "bailiff-cloudwatch" {
  statement_id   = "Executebailifffromcloudwatch"
  action         = "lambda:InvokeFunction"
  function_name  = "${aws_lambda_function.bailiff_lambda.function_name}"
  principal      = "events.amazonaws.com"
  source_arn     = "${aws_cloudwatch_event_rule.bailiff-schedule.arn}"
}

# CloudWatch Part

resource "aws_cloudwatch_event_target" "bailiff" {
  target_id = "bailiff-${var.ENV}"
  rule      = "${aws_cloudwatch_event_rule.bailiff-schedule.name}"
  arn       = "${aws_lambda_function.bailiff_lambda.arn}"

}
resource "aws_cloudwatch_event_rule" "bailiff-schedule" {
  name        = "bailiff-schedule-${var.ENV}"
  description = "Triggers bailiff on a regular basis"

  schedule_expression = "${var.CRON_EXPRESSION}"
  event_pattern = <<PATTERN
{
  "detail-type": [
    "Bailiff triggered by cron"
  ]
}
PATTERN
}
