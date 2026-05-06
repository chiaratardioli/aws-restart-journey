## Create an AI Smart Assistant

## Introduction
The HR department receives over 500 daily requests about policies, benefits, and procedures, but responses are limited to business hours and capacity. An AI solution is needed to automate responses and improve availability.

![HR Requests](./images/SL-04-hr-requests.png)

## AWS Services
- **Amazon Bedrock**: to create the knowledge base and AI agent
-  **Amazon OpenSearch Service**: to store and retrieve vector embeddings for the knowledge base
- **AWS Lambda**: to execute actions (e.g., submit vacation requests) through the agent’s action group

[Link to course on Skillbuilder](https://skillbuilder.aws/learn/PT6HBMUFM8/aws-simulearn-create-an-ai-smart-assistant/9VN4PQCUR8)


## Solution

1. I create an Amazon Bedrock knowledge base using HR documents
2. I build an AI agent to answer employee questions
3. I attached the knowledge base to the agent for accurate responses
4. I added an action group to handle requests (e.g., vacation) using AWS Lambda
5. I tested the agent for question answering and task execution  

![Architecture](./images/SL-04-architecture.png)
![Agent Setup](./images/SL-04-agent-setup.png)

## Conclusion
The AI smart assistant automates HR support by providing accurate answers and handling requests, improving efficiency and availability.

