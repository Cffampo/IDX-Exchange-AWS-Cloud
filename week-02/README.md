# Week 2 — IAM & Security Foundations

## Lab 2.1 — Least-Privilege S3 Uploader Policy

### S3UploaderOnly-CarlFampo

This policy allows the IAM user to interact with objects in the training S3 bucket.

**Allowed actions:**

* `s3:PutObject` — allows objects to be uploaded to the bucket.
* `s3:GetObject` — allows objects to be retrieved from the bucket.

The resource is scoped to:

```text
arn:aws:s3:::my-training-bucket-CarlFampo/*
```

The `/*` specifies objects within the bucket rather than the bucket itself. The policy does not grant permission to list buckets, delete objects, create buckets, or access other S3 resources. This follows the principle of least privilege by granting only the permissions required for the intended S3 object operations.

### IAM User

A separate IAM user named `s3-test-user` was created with no console access. The `S3UploaderOnly-CarlFampo` policy was attached directly to the user.

An access key was created for the user and configured as the `s3test` AWS CLI profile.

The following command was used to test the user's permissions:

```bash
aws s3 ls --profile s3test
```

The command returned an `AccessDenied` error for `s3:ListAllMyBuckets`.

This was the expected result because the policy does not allow the user to list all S3 buckets. The result demonstrates least-privilege behavior.

## Lab 2.2 — IAM Access Analyzer

An IAM Access Analyzer was created using the default settings.

After the analyzer was created and given time to run, it showed **0 active findings**, which is the expected result for a fresh account with no detected external access findings.

## Debug Lab 2.3 — IAM Access Denied

The debugging exercise focused on understanding IAM policy evaluation and diagnosing an `AccessDenied` error.

The main checks include:

1. Verify that the S3 resource ARN matches the correct bucket.
2. Verify that object-level actions such as `s3:PutObject` and `s3:GetObject` use the `/*` object ARN.
3. Check for explicit `Deny` statements in applicable policies.
4. Check the S3 bucket policy for restrictions.
5. Use the IAM Policy Simulator to test the specific action against the specific resource.

An important distinction is that:

```text
arn:aws:s3:::bucket-name
```

refers to the bucket itself, while:

```text
arn:aws:s3:::bucket-name/*
```

refers to objects inside the bucket.

IAM policy evaluation also follows the rule that an explicit `Deny` overrides an `Allow`.

## Key Concepts

* IAM users represent individual identities.
* IAM groups can organize users and apply permissions collectively.
* IAM roles provide permissions that can be assumed by trusted identities or AWS services.
* Identity-based policies attach permissions to identities.
* Resource-based policies attach permissions to resources.
* Managed policies can be reused, while inline policies are directly embedded in a specific identity or resource.
* Least privilege means granting only the permissions required to perform a task.
* An explicit `Deny` always overrides an `Allow`.
