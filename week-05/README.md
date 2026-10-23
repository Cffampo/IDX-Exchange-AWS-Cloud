# Week 5: Networking - VPC Deep Dive

## Overview

This lab explored AWS Virtual Private Clouds (VPCs), public and private subnets, route tables, Internet Gateways, NAT Gateways, and the bastion host pattern.

The objective was to create a custom VPC and securely connect to a private EC2 instance through a bastion host without exposing the private instance directly to the internet.

## Lab 5.1: Custom VPC

Created a custom VPC using the AWS Management Console and the **VPC and more** wizard.

### Configuration

- **VPC name:** `training-vpc`
- **IPv4 CIDR block:** `10.0.0.0/16`
- **Availability Zones:** 2
- **Public subnets:** 2
- **Private subnets:** 2
- **NAT Gateway:** 1, in a single Availability Zone
- **VPC endpoints:** None

### Networking Components

- **VPC:** Provides an isolated virtual network for AWS resources.
- **Public subnets:** Use a route table with a default route to the Internet Gateway.
- **Private subnets:** Do not provide direct inbound internet access to private instances.
- **Internet Gateway (IGW):** Allows appropriately configured resources in public subnets to communicate with the internet.
- **NAT Gateway:** Allows resources in private subnets to initiate outbound internet connections when routing and security rules permit.
- **Route tables:** Determine where network traffic is directed.

## Lab 5.2: Bastion Host Pattern

Launched two Amazon Linux 2023 EC2 instances using the `t3.micro` instance type.

### Bastion Host

The bastion host was deployed in a public subnet with a public IPv4 address.

Its security group allowed inbound SSH traffic on TCP port 22 from my IP address.

### Private Instance

The private instance was deployed in a private subnet without a public IPv4 address.

Its security group allowed inbound SSH traffic on TCP port 22 only from the bastion host's security group.

### SSH Connection

Successfully connected to the private instance through the bastion host.

The connection path was:

1. Connected from my laptop to the bastion host using SSH and the existing EC2 key pair.
2. Used SSH agent forwarding (`ssh -A`) to forward authentication to the bastion without copying my private key onto it.
3. Connected from the bastion host to the private instance using its private IPv4 address.

The private instance's private IP address during the successful connection was `10.0.134.100`.

This verified that the private instance could be accessed through the bastion without requiring a public IP address or allowing SSH directly from the internet.

## Lab 5.3: Private Instance Internet Access

The debugging exercise focuses on understanding why a private instance may not have outbound internet access.

The following items should be checked when diagnosing connectivity problems:

- The private subnet's route table has a default route (`0.0.0.0/0`) pointing to the NAT Gateway.
- The private subnet is explicitly associated with the correct route table.
- The NAT Gateway is deployed in a public subnet.
- The public subnet has a valid default route to the Internet Gateway.
- The NAT Gateway has an associated Elastic IP address.
- Network security rules permit the required traffic.

A subnet's behavior depends on its route table and associated networking resources, not simply on whether it is named public or private.

## Traffic Flow

### Inbound SSH

`Laptop → Internet → Internet Gateway → Public Subnet → Bastion Host → Private Subnet → Private Instance`

The bastion host is the entry point into the private network. Its security group restricts SSH access to my IP address, while the private instance's security group trusts SSH traffic from the bastion's security group.

### Outbound Internet Access

`Private Instance → Private Subnet Route Table → NAT Gateway → Internet Gateway → Internet`

This path is used for outbound internet connections initiated by the private instance. The NAT Gateway is not part of the inbound SSH path.

## Cleanup

After completing the connectivity test, the lab resources should be removed to minimize AWS costs.

- Terminate the bastion EC2 instance.
- Terminate the private EC2 instance.
- Delete the NAT Gateway.
- Release any unused Elastic IP allocated for the lab.
- Delete the custom VPC after its dependencies have been removed.
- Verify that no lab resources remain that could incur ongoing charges.

NAT Gateways incur hourly charges while provisioned, in addition to applicable data processing charges. EC2 instances and certain networking resources may also incur charges.

## Key Takeaways

- A VPC provides an isolated network for AWS resources.
- CIDR blocks define the IP address ranges available to a VPC and its subnets.
- Route tables explicitly control network traffic.
- An Internet Gateway enables internet connectivity for appropriately configured public resources.
- A NAT Gateway provides outbound internet access to private resources.
- A bastion host provides a controlled SSH entry point into a private network.
- Security groups can reference other security groups to enforce instance-to-instance access.
- SSH agent forwarding allows authentication through a bastion without copying a private key onto it.
- Removing billable resources promptly is important when working in a cost-sensitive AWS training environment.
