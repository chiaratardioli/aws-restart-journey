<h1 align="center">🖼️ Elegant Frame Gallery - Static Website on AWS</h1>

<p align="center">
  <strong>A cloud‑hosted, fast, and scalable static website for a Swiss photo frame company</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/AWS-S3%20%7C%20CloudFront%20%7C%20IAM-orange?logo=amazon-aws" alt="AWS Services">
  <img src="https://img.shields.io/badge/HTML-CSS-blue?logo=html5" alt="HTML/CSS">
  <img src="https://img.shields.io/badge/status-live-success" alt="Project Status">
</p>

---

## 📋 Table of Contents
- [Company Overview](#company-overview)
- [Current Challenges](#current-challenges)
- [Why AWS?](#why-aws)
- [Our Solution: Static Website](#our-solution-static-website)
- [Architecture & AWS Services](#architecture--aws-services)
- [Project Steps](#project-steps)
- [Website Enhancement Ideas](#website-enhancement-ideas)
- [Conclusion](#conclusion)
- [Repository Contents](#repository-contents)

---

## 🏢 Company Overview

**Elegant Frame Gallery** is a Swiss-based company specializing in high-quality photo frames for retail and commercial customers. They offer a wide range of stylish frames for homes, offices, galleries, and commercial spaces.

- **Headquarters:** St. Gallen, Switzerland  
- **Branches:** Throughout Switzerland  
- **Users:** ~1,000 concurrent users (and growing fast)  
- **Mission:** Provide products that enhance and preserve meaningful moments through design, quality, and craftsmanship.

---

## ⚠️ Current Challenges

| Challenge | Description |
|-----------|-------------|
| **No Cloud Migration** | Manual/on‑premises systems for bookings and orders |
| **Scalability** | Need to handle increased traffic and product data |
| **Website Performance** | Slow image loading affects user experience & sales |
| **Content Management** | Manual updates of product info and images = time‑consuming |
| **Availability** | Website must be accessible 24/7 |
| **Security** | Protect customer data and site integrity |

---

## ☁️ Why AWS?

Amazon Web Services provides the perfect solution for Elegant Frame:

- **Reliable storage** – Amazon S3 securely stores product images and files
- **High performance** – Fast delivery of content improves UX
- **Scalability** – Automatically handles growth in traffic and products
- **Cost efficiency** – Pay‑as‑you‑go model, ideal for a growing business
- **Static website hosting** – Simple, reliable, and low‑maintenance

---

## 🖥️ Our Solution: Static Website

We built and deployed a **static website** for Elegant Frame Gallery using AWS. The site includes:
- Home, Brand, Catalogues, Contacts, and Shop pages
- Pure HTML & CSS (no server‑side processing)
- Hosted on Amazon S3 with public access via bucket policy
- Delivered globally through Amazon CloudFront for speed and low latency

**Technologies used:** HTML, CSS, Amazon S3.

---

## 🏗️ Architecture & AWS Services

| Service | Purpose |
|---------|---------|
| **Amazon S3** | Stores all website files (HTML, CSS, images, PDFs) |
| **Amazon CloudFront** | CDN for fast global content delivery |
| **AWS IAM** | Manages secure access for team members |
| **AWS Certificate Manager** | Provides free SSL certificates for HTTPS |

*Future enhancements may add DynamoDB, Lambda, Cognito, etc.*

---

## 📝 Project Steps

1. **Create website files** – `index.html`, CSS, and image assets.
2. **Log in to AWS Console** and open Amazon S3.
3. **Create an S3 bucket**  
   - Unique bucket name  
   - Choose region  
   - **Disable Block Public Access** (for static hosting)
4. **Enable static website hosting** in bucket properties.
5. **Upload all website files** (HTML, CSS, images) to the bucket.
6. **Add a bucket policy** to make content publicly readable.
7. **Test the website endpoint** – access via the S3 website URL.
8. **Verify** that the site loads correctly.

---

## 💡 Website Enhancement Ideas

The current static site is a solid foundation. Future improvements can include:

- **User authentication** – Add sign‑in/booking with Amazon Cognito
- **Dynamic features** – Connect booking forms using AWS Lambda
- **Database backend** – Store customer data in Amazon DynamoDB or RDS
- **B2B extension** – Serve specific content to business clients via CloudFront
- **Analytics** – Track visitor behavior with Amazon QuickSight or Google Analytics

---

## ✅ Conclusion

By migrating to AWS, Elegant Frame Gallery now enjoys:

- ⚡ **Fast & scalable website** – S3 + CloudFront ensure quick loads and handle traffic spikes
- 🌍 **Always available** – Global delivery with high reliability
- 🛠️ **Simple to manage** – Staff can update products/images without technical expertise
- 🔒 **Secure by design** – HTTPS, IAM policies protect data
- 💰 **Cost‑effective** – Pay only for what you use
- 🚀 **Future‑ready** – Easy to add logins, databases, or B2B portals later

---

## 📁 Repository Contents

- `index.html` – Main website page
- `css/` – Stylesheets
- `images/` – Product and gallery images
- `README.md` – This documentation (HTML format)

---

<p align="center">
  <sub>Built with ❤️ using AWS for Elegant Frame Gallery</sub>
</p>
