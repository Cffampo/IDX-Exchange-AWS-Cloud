# Week 6 — Elastic Load Balancing & Auto Scaling Report

**Date:** November 3, 2026  
**Lab:** Lab 6.1 — ASG Behind an ALB  
**Status:** Partially completed

## 1. Objective

The goal of this lab was to deploy the PropertyLite application behind an Application Load Balancer (ALB), configure an Auto Scaling Group (ASG), and demonstrate automatic instance replacement and CPU-based scaling.

## 2. Infrastructure Configuration

The following resources were created or configured:

| Resource | Configuration | Result |
|---|---|---|
| VPC | `training-vpc`, 10.0.0.0/16 | Created |
| Subnets | 2 public, 2 private | Created |
| NAT Gateway | 1 in one AZ | Created |
| Launch Template | `property-api-template` | Created |
| Instance type | `t3.micro` | Configured |
| Target Group | `property-api-tg` | Created |
| Health check | HTTP, port 8080, `/health` | Configured |
| Application Load Balancer | `property-api-alb` | Created and Active |
| Auto Scaling Group | `property-api-asg` | Creation unsuccessful |

## 3. Security Group Configuration

Two security groups were configured:

- `property-alb-sg`: Allows inbound HTTP traffic on port 80.
- `property-api-sg-new`: Allows SSH on port 22 from my IP and application traffic on port 8080 from the ALB security group.

An existing security group was associated with an older VPC. Since security groups cannot be transferred between VPCs, a replacement security group was created in `training-vpc`.

## 4. Issues Encountered

During Auto Scaling Group creation, AWS returned the following error:

> One or more security groups in the launch template are not linked to the VPCs configured in the Auto Scaling group.

The issue occurred while configuring the launch template and VPC networking. Although a replacement security group was created in the correct VPC and the launch template was updated, the ASG creation continued to fail.

Due to the time and cost associated with troubleshooting, I decided not to continue deploying additional resources.

## 5. Testing Results

| Test | Result |
|---|---|
| ALB provisioning | Successful |
| Target group creation | Successful |
| Health check configuration | Completed |
| ASG creation | Failed |
| ALB `/health` endpoint | Not verified |
| ALB `/properties` endpoint | Not verified |
| Instance self-healing | Not tested |
| CPU stress test | Not performed |
| CloudWatch scale-out event | Not captured |

## 6. Cleanup

To avoid unnecessary AWS charges, I stopped the lab and began removing the deployed infrastructure.

- Confirmed no running EC2 instances remained.
- Deleted the Application Load Balancer.
- Deleted the NAT Gateway.
- Initiated cleanup of the remaining networking and supporting resources.

## 7. Lessons Learned

This lab reinforced several important AWS concepts:

- Application Load Balancers distribute incoming HTTP traffic across registered targets.
- Target groups use health checks to determine instance availability.
- Auto Scaling Groups maintain desired capacity and replace unhealthy instances.
- Security groups must be associated with compatible VPC networking configurations.
- ALBs require explicit security group permissions to communicate with application instances.
- NAT Gateways and load balancers generate ongoing charges while provisioned, making resource cleanup important.

## 8. Conclusion

I successfully created the VPC networking infrastructure, launch template, target group, and Application Load Balancer. However, I encountered a VPC and security group compatibility issue that prevented successful Auto Scaling Group creation.

The self-healing and CPU-based scaling portions of the lab remain incomplete. All testing results are reported accurately rather than assuming successful behavior without verification.
