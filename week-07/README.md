# Week 7 - Serverless & Event-Driven Architecture

## Overview

This lab migrated PropertyLite's read operation from an always-on
EC2 instance to a serverless architecture using API Gateway,
AWS Lambda, and DynamoDB.

It also introduced Amazon SQS and dead-letter queues.

## Architecture

```mermaid
flowchart TD
    A[Client / curl / Postman]
    B[Amazon API Gateway]
    C[AWS Lambda - get-property]
    D[Amazon DynamoDB - Properties]
    E[JSON Response]

    A -->|GET /properties/{id}| B
    B --> C
    C -->|GetItem| D
    D -->|Property record| C
    C --> E
    E --> A
