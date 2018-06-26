#KMS Part

resource "aws_kms_key" "kms_key" {
  description             = "Bailiff kms key"
  policy = <<EOF
{
  "Version": "2012-10-17",
  "Id": "key-default-1",
  "Statement": [
    {
      "Sid": "Enable IAM User Permissions for root",
      "Effect": "Allow",
      "Principal": {
        "AWS": "${data.aws_caller_identity.current.account_id}"
      },
      "Action": "kms:*",
      "Resource": "*"
    },
    {
      "Sid": "Enable IAM User Permissions for UDD account",
      "Effect": "Allow",
      "Principal": {
        "AWS": "${data.aws_caller_identity.current.arn}"
      },
      "Action": "kms:*",
      "Resource": "*"
    }
  ]
}
EOF
}

resource "aws_kms_alias" "kms_key_alias" {
  name          = "alias/bailiff_key"
  target_key_id = "${aws_kms_key.kms_key.key_id}"
}

