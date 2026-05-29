# Strong Consistency vs Eventual Consistency

Understanding consistency models is essential in distributed systems and cloud computing. This note explains the difference between **strong consistency**, **eventual consistency**, and **read-after-write consistency** using simple examples and AWS services.

---

# 1. Strong Consistency vs Eventual Consistency

| Feature                                 | Strong Consistency          | Eventual Consistency            |
| --------------------------------------- | --------------------------- | ------------------------------- |
| After a write, what does a read return? | Always the latest data      | May temporarily return old data |
| Data synchronization                    | Immediate                   | Delayed                         |
| User experience                         | Fully up-to-date            | Temporary stale reads possible  |
| Performance/scalability                 | Usually slower/more complex | Faster and highly scalable      |
| Example                                 | Banking transactions        | Social media likes/views        |

---

## Example Scenario

Suppose User A changes a file from **Version 1 → Version 2**.

### Strong Consistency

* User B immediately reads the file
* User B sees **Version 2**

### Eventual Consistency

* User B may still briefly see **Version 1**
* After synchronization completes, everyone sees **Version 2**

---

# 2. Read-After-Write Consistency

Read-after-write consistency is a specific type of consistency guarantee.

It means:

> After a successful write operation, any immediate read returns the latest written data.

---

## Example

You upload `photo.jpg` to Amazon S3.

### With Read-After-Write Consistency

* Upload succeeds
* You immediately request the file
* The file is instantly available

### Without Read-After-Write Consistency

* Upload succeeds
* Immediate reads may temporarily return:

  * `Object not found`
  * Older object versions

---

# Relationship Between Them

* **Read-after-write consistency** is a form of **strong consistency** for newly written data.
* **Eventual consistency** does not guarantee immediate visibility after writes.

---

# AWS Examples

| AWS Service     | Consistency Model                                            |
| --------------- | ------------------------------------------------------------ |
| Amazon S3       | Strong read-after-write consistency                          |
| Amazon DynamoDB | Eventual consistency by default, optional strong consistency |
| Amazon RDS      | Strong consistency                                           |

---

# Easy Memory Tricks

* **Strong consistency** → “What I write is what everyone reads immediately.”
* **Eventual consistency** → “Everyone will see the update soon, but not instantly.”
* **Read-after-write consistency** → “After I save something, I can immediately read it.”

---

# Key Takeaways

* Strong consistency prioritizes accuracy and immediate synchronization.
* Eventual consistency prioritizes scalability and performance.
* Distributed cloud systems often balance consistency, availability, and scalability.
* AWS services use different consistency models depending on their architecture and use cases.

---

# References

* AWS Documentation
* Amazon S3 Consistency Model
* Amazon DynamoDB Consistency Options
* Distributed Systems Fundamentals
