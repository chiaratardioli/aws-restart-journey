# AWS Systems Manager Lab Report

## Introduction
AWS Systems Manager is a collection of capabilities used to centralize operational data and automate tasks across Amazon Web Services (AWS) resources. It enables the configuration and management of Amazon EC2 instances, on-premises servers, virtual machines, and other resources at scale.  

This lab demonstrates how Systems Manager can be used to manage infrastructure efficiently without requiring direct access (e.g., SSH), improving automation, security, and scalability.

## Objectives
The objectives of this lab were to:
- Verify configurations and permissions
- Run tasks on managed instances
- Update application settings
- Access an instance command line securely

## Environment Setup
The lab was conducted using the AWS Management Console. A pre-configured environment was provided, including:
- A Virtual Private Cloud (VPC)
- A managed EC2 instance
- AWS Systems Manager with required permissions

---

## Task 1: Generate Inventory Lists

Fleet Manager was used to collect inventory data from the managed EC2 instance.

An inventory association named **Inventory-Association** was created to gather:
- Operating system details  
- Installed applications  
- Instance metadata  

The collected data was accessible through the **Inventory tab**, allowing inspection of installed software without connecting via SSH.

📸 **Screenshot 1 – Inventory Association Setup**  
![Inventory Setup](images/inventory-setup.png)

📸 **Screenshot 2 – Instance Inventory View**  
![Inventory View](images/inventory-view.png)

**Outcome:**  
Inventory collection was successfully configured, enabling centralized visibility of instance configurations.

---

## Task 2: Install Application Using Run Command

Run Command was used to install a custom application (Widget Manufacturing Dashboard) on the EC2 instance.

This process executed a predefined document that:
- Installed Apache web server  
- Installed PHP and AWS SDK  
- Deployed the web application  
- Started the web server  

After execution, the application was accessed via the instance’s public IP address in a browser.

📸 **Screenshot 3 – Run Command Configuration**  
![Run Command](images/run-command.png)

📸 **Screenshot 4 – Command Execution Success**  
![Command Success](images/command-success.png)

📸 **Screenshot 5 – Web Application Running**  
![Web App](images/web-app.png)

**Outcome:**  
The application was successfully installed and deployed without direct instance access.

---

## Task 3: Manage Configuration with Parameter Store

Parameter Store was used to manage application configuration.

A parameter was created:
- **Name:** `/dashboard/show-beta-features`  
- **Value:** `True`  

The application dynamically read this parameter and enabled additional features (a third chart).

📸 **Screenshot 6 – Parameter Creation**  
![Parameter Store](images/parameter-store.png)

📸 **Screenshot 7 – Application with Beta Feature Enabled**  
![Beta Feature](images/beta-feature.png)

(Optional) After deleting the parameter, the feature disappeared.

📸 **Screenshot 8 – Application Without Beta Feature**  
![No Beta](images/no-beta.png)

**Outcome:**  
Application behavior was successfully modified without redeployment.

---

## Task 4: Access Instance Using Session Manager

Session Manager was used to securely access the EC2 instance via a browser-based shell.

Commands executed included:
- Listing application files  
- Retrieving metadata  
- Describing EC2 instances  

This method required no SSH keys or open ports.

📸 **Screenshot 9 – Session Manager Start Session**  
![Session Start](images/session-start.png)

📸 **Screenshot 10 – Command Execution in Session**  
![Session Commands](images/session-commands.png)

**Outcome:**  
Secure, auditable access to the instance was achieved without traditional SSH.

---

## Results and Discussion

This lab demonstrated the advantages of AWS Systems Manager:
- Centralized infrastructure management  
- Reduced need for SSH access  
- Improved security and auditing  
- Automation of operational tasks  
- Dynamic configuration management  

---

## Conclusion

In this lab, AWS Systems Manager was successfully used to:
- Verify configurations and permissions  
- Execute remote commands  
- Modify application settings dynamically  
- Access instances securely without SSH  

The lab highlights how Systems Manager enhances efficiency, security, and scalability in cloud environments.

## Additional resources
- [What is AWS Systems Manager?](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html)
- [AWS Systems Manager Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html)
