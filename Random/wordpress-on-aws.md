# WordPress on AWS

This document briefly compares different ways to run WordPress on AWS.

## Amazon Lightsail

**Best for:** small websites, beginners, simple deployments.

**Characteristics**
- Very easy setup using a WordPress blueprint.
- Fixed monthly pricing.
- Includes:
  - virtual server
  - storage
  - static IP
  - DNS
- Limited scalability compared to EC2.

**Typical architecture**
```
Internet
↓
Lightsail instance
├─ WordPress
├─ Web server
├─ PHP
└─ Database
```

**Pros**
- Simple
- Low cost

**Cons**
- Less flexible
- Limited scalability

---

## Amazon EC2

**Best for:** developers who want full control.

**Characteristics**
- Full control over the server.
- Manual installation of:
  - WordPress
  - web server
  - database
- Can scale with other AWS services.

**Typical architecture**
```
Internet
↓
EC2 instance
├─ WordPress
├─ Apache/Nginx
├─ PHP
└─ MySQL
```

**Pros**
- Highly flexible
- Configurable

**Cons**
- Requires more setup and maintenance

---

## Managed AWS Architecture

**Best for:** high-traffic or production websites.

Often uses multiple AWS services:

- Amazon EC2 – application servers
- Amazon RDS – managed database
- Amazon S3 – media storage
- Elastic Load Balancing – traffic distribution
- Amazon CloudFront – content delivery network

**Typical architecture**
```
Users
↓
CloudFront (CDN)
↓
Load Balancer
↓
EC2 instances (WordPress)
↓
RDS database
↓
S3 storage
```

**Pros**
- Highly scalable
- High availability

**Cons**
- More complex
- Higher cost
