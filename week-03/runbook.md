# Week 3 — EC2 Compute and EBS

## Overview

This week focused on deploying the PropertyLite API to an AWS EC2 instance, creating an EBS snapshot, troubleshooting SSH connectivity, and cleaning up AWS resources.

---

## Lab 3.1 — Deploy PropertyLite to EC2

### 1. Launch the EC2 Instance

I opened the AWS EC2 console and launched a new instance with the following configuration:

- **Name:** `property-api-01`
- **AMI:** Amazon Linux 2023
- **Instance type:** `t3.micro`
- **Key pair:** `training-key`
- **Key format:** RSA `.pem`

The `training-key.pem` file was downloaded and stored in my local `~/.ssh` directory.

### 2. Configure the Security Group

I created a security group with these inbound rules:

| Type | Port | Source | Purpose |
|---|---:|---|---|
| SSH | 22 | My IP | Secure SSH access |
| Custom TCP | 8080 | Anywhere | PropertyLite API |

SSH was restricted to my current public IP instead of allowing access from anywhere.

### 3. Configure User Data

I used an EC2 user data bootstrap script to automatically configure the server when it launched.

The script:

1. Updated the Amazon Linux packages.
2. Installed Python 3 and pip.
3. Installed Flask 3.0.3.
4. Created `/opt/property-api`.
5. Created the PropertyLite `app.py` application.
6. Created the sample `rets_property_sample.csv` dataset.
7. Started the API in the background.

This allowed the EC2 instance to configure and start PropertyLite automatically during boot.

### 4. Connect to the Instance

I restricted the private key permissions with:

```bash
chmod 400 ~/.ssh/training-key.pem
