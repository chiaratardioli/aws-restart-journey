# Monitor an EC2 Instance with Amazon CloudWatch

This lab focused on monitoring and logging AWS resources using Amazon CloudWatch and Amazon SNS. The objective was to configure a monitoring solution 
capable of detecting high CPU utilization on an Amazon EC2 instance and automatically sending notifications through Amazon SNS.

The lab environment provided a preconfigured EC2 instance named **Stress Test** along with the required IAM permissions and Systems Manager access. 
During the lab, CloudWatch metrics and alarms were configured, CPU stress testing was performed, and a CloudWatch dashboard was created to 
visualize monitoring data.


## AWS Services

The following AWS resources were available in the lab environment:

- One preconfigured Amazon EC2 instance named **Stress Test**
- AWS Systems Manager Session Manager access
- IAM roles and backend configurations already provisioned
- Amazon CloudWatch
- Amazon SNS

![Lab Architecture](./images/SE-06-architecture.png)


## Task 1: Configure Amazon SNS

In this task, I created an Amazon SNS topic and subscribed an email endpoint to receive notifications from CloudWatch alarms.

#### 1. Create an SNS Topic

I navigated to the AWS Management Console and opened the Amazon SNS service.

I created a new topic with the following configuration:
- Type: `Standard`
- Name: `MyCwAlarm`

#### 2. Create an Email Subscription

After creating the topic, I added a subscription using my email address.
- Protocol: `Email`
- Endpoint: `<My email address>`

Once the subscription was created, the status remained **Pending confirmation** until I confirmed the subscription through the email sent by AWS.

After confirming the subscription, the status changed to **Confirmed**.

![SNS Topic with Subscription](./images/SE-06-sns-topic.png)


## Task 2: Create a CloudWatch Alarm

In this task, I configured a CloudWatch alarm to monitor CPU utilization for the Stress Test EC2 instance.

#### 1. View EC2 Metrics

I opened Amazon CloudWatch and navigated to:

```text
Metrics → All Metrics → EC2 → Per-Instance Metrics
````

I selected the **CPUUtilization** metric for the Stress Test instance.

Initially, the CPU utilization remained close to 0% because no workload was running on the instance.

![CloudWatch Metrics](./images/SE-06-cloudwatch-metrics.png)

#### 2. Configure the Alarm

I created a new CloudWatch alarm using the following settings:

- Metric: `CPUUtilization`
- Statistic: `Average`
- Period: `1 minute`
- Threshold Type: `Static`
- Condition: `Greater than 60`
- SNS Topic: `MyCwAlarm`

The alarm configuration triggered notifications whenever CPU utilization exceeded 60%.

![CloudWatch Alarm Configuration - part 1](./images/SE-06-cloudwatch-alarm-configuration-1.png)

![CloudWatch Alarm Configuration - part 2](./images/SE-06-cloudwatch-alarm-configuration-2.png)

![CloudWatch Alarm Configuration - part 3](./images/SE-06-cloudwatch-alarm-configuration-3.png)


#### 3. Alarm Details

The alarm was created with the following configuration:

- Alarm Name: `LabCPUUtilizationAlarm`
- Description: `CloudWatch alarm for Stress Test EC2 instance CPUUtilization`

![CloudWatch Alarm](./images/SE-06-cloudwatch-alarm-created.png)


## Task 3: Test the CloudWatch Alarm

In this task, I generated a CPU spike on the EC2 instance to validate that the CloudWatch alarm and SNS notifications were functioning correctly.

### Connect to the EC2 Instance

Using the provided Systems Manager connection link, I accessed the Stress Test instance terminal.

![EC2 Terminal Access](./images/SE-06-ec2-terminal-access.png)

### Run the CPU Stress Test

I executed the following command to increase CPU utilization:

```bash
sudo stress --cpu 10 -v --timeout 400s
```

This command generated CPU load for 400 seconds using 10 worker threads.

![Stress Command Execution](./images/SE-06-stress-command-execution.png)

### Monitor CPU Usage

In a second terminal session, I monitored system resource usage using the following command:

```bash
top
```

The output showed CPU utilization approaching 100%.

```text
top - 14:32:18 up 15 min,  2 users,  load average: 9.98, 9.75, 5.20
Tasks: 145 total,  11 running, 134 sleeping
%Cpu(s): 99.8 us,  0.2 sy,  0.0 ni,  0.0 id
```

![Top Command Monitoring](./images/SE-06-top-command-monitoring.png)

### Verify the CloudWatch Alarm

I returned to the CloudWatch console and monitored the alarm state.

After several minutes, the alarm state changed from:

```text
OK → In alarm
```

The CloudWatch graph showed CPU utilization exceeding the 60% threshold.

![CloudWatch Alarm Triggered](./images/SE-06-cloudwatch-alarm-triggered.png)

### Verify Email Notification

I checked my email inbox and confirmed that Amazon SNS successfully sent an alert notification.

![SNS Email Notification](./images/SE-06-sns-email-notification.png)

### Result

The CloudWatch alarm successfully detected the CPU spike and triggered an SNS email notification.

## Task 4: Create a CloudWatch Dashboard

In this task, I created a CloudWatch dashboard to visualize CPU utilization metrics.

### Create Dashboard

I navigated to:

```text
CloudWatch → Dashboards → Create dashboard
```

I configured the dashboard with the following settings:

| Setting        | Value           |
| -------------- | --------------- |
| Dashboard Name | LabEC2Dashboard |
| Widget Type    | Line Graph      |

![Dashboard Creation](./images/SE-06-dashboard-creation.png)

### Add CPUUtilization Metric

I added the EC2 metric:

```text
EC2 → Per-Instance Metrics → CPUUtilization
```

for the Stress Test instance.

![Dashboard Metrics](./images/SE-06-dashboard-metrics.png)

### Save Dashboard

After adding the widget, I saved the dashboard.

The dashboard provided a centralized view of CPU utilization metrics for the monitored EC2 instance.

![Final Dashboard](./images/SE-06-final-dashboard.png)

## Results and Observations

During the lab, the monitoring workflow operated successfully from end to end:

* Amazon SNS delivered notification emails correctly
* CloudWatch monitored EC2 CPU utilization in near real time
* The CloudWatch alarm transitioned into the **In alarm** state when the threshold was exceeded
* The EC2 stress test successfully simulated abnormal CPU usage
* The CloudWatch dashboard displayed CPU metrics visually

The lab demonstrated how AWS monitoring and notification services can be combined to improve operational visibility and 
detect unusual system behavior.

## Conclusions

In this lab, I implemented a monitoring solution for an Amazon EC2 instance using Amazon CloudWatch and Amazon SNS.

I completed the following tasks:

* Created an Amazon SNS notification topic
* Configured a CloudWatch alarm
* Performed a CPU stress test on an EC2 instance
* Verified that SNS email notifications were delivered
* Created a CloudWatch dashboard for metric visualization

This lab demonstrated how AWS monitoring tools can be used to detect abnormal resource utilization and provide automated alerts for operational and security monitoring.
