# Mock Exam: Amazon Solution Architect Associate

## Question #1

Praesignis must comply with a regulatory requirement that all data stored in Amazon S3 must be encrypted, and the encryption keys must be managed and rotated exclusively by the Praesignis security team using their own key material. The solution must integrate with AWS services and provide audit trails of all key usage.

Which S3 encryption option satisfies these requirements?

A. SSE-C (Server-Side Encryption with Customer-Provided Keys)  
B. Client-Side Encryption using a self-managed library before uploading to S3  
C. SSE-S3 (Server-Side Encryption with Amazon S3 Managed Keys)  
D. SSE-KMS using Customer Managed Keys (CMKs) in AWS KMS  

### Answer

**Correct answer: D. SSE-KMS using Customer Managed Keys (CMKs) in AWS KMS**

**Explanation:**
**SSE-KMS with Customer Managed Keys (CMKs)** is the best choice because it allows Praesignis to manage the encryption keys within **AWS Key Management Service (KMS)** while integrating seamlessly with AWS services. Customer Managed Keys support key rotation, granular access control through IAM and key policies, and provide detailed audit logs of all key usage through **AWS CloudTrail**. If required, AWS KMS also supports importing the organization's own key material (BYOK), allowing the security team to use their own cryptographic material while retaining the benefits of KMS integration.

* **A. SSE-C** requires customers to provide the encryption key with every request. AWS does not store or manage the keys, making it difficult to integrate with AWS services and limiting centralized auditing and key management.
* **B. Client-Side Encryption** gives full control over encryption but requires the application to manage encryption, decryption, and key lifecycle. It does not provide the seamless AWS service integration or centralized KMS audit capabilities required.
* **C. SSE-S3** uses AWS-managed keys, so the customer has no control over key management or rotation, making it unsuitable for the stated regulatory requirements.

