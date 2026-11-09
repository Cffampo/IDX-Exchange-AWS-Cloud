# Week 8 — Infrastructure as Code (Terraform)

## Overview
This lab reproduced the Week 5 AWS VPC infrastructure using Terraform instead of manually creating resources through the AWS Console.

## Infrastructure Created
- VPC: `training-vpc-tf`
- CIDR block: `10.1.0.0/16`
- Region: `us-east-1`
- Availability Zones: `us-east-1a`, `us-east-1b`
- 2 public subnets
- 2 private subnets
- 1 Internet Gateway
- 1 NAT Gateway
- Public and private route tables

## Terraform Commands

### terraform init
Initializes the Terraform working directory and downloads the required AWS provider and VPC module.

### terraform plan
Previews the infrastructure changes Terraform intends to make. This allows you to review resources before creating or modifying anything.

### terraform apply
Applies the configuration and creates the infrastructure in AWS after confirmation.

### terraform destroy
Destroys the infrastructure managed by Terraform and removes the resources from AWS.

## Terraform State

Terraform state is stored in `terraform.tfstate`. It tracks the resources Terraform manages and their current configuration in AWS.

State is important because Terraform uses it to compare the desired infrastructure configuration against the resources that currently exist.

If resources are manually changed or deleted through the AWS Console, Terraform can detect differences called configuration drift.

Changes to Terraform-managed infrastructure should generally be made through Terraform rather than manually through the AWS Console.

## Results

- Successfully initialized Terraform.
- Reviewed the execution plan before applying changes.
- Created 19 AWS resources using `terraform apply`.
- Successfully destroyed all 19 resources using `terraform destroy`.
- Verified that Terraform completed cleanup successfully.

## Cleanup

All Terraform-managed AWS resources were destroyed immediately after the lab to avoid unnecessary AWS charges.

## Key Takeaways

- Declarative provisioning describes the desired infrastructure rather than manually specifying every creation step.
- Terraform manages infrastructure through configuration files.
- `terraform plan` provides a preview before changes are applied.
- Terraform state tracks managed infrastructure.
- Configuration drift can occur when infrastructure is changed outside Terraform.
- `terraform destroy` removes resources managed by the configuration.
