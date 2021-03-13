# Part 6: Cloud computing

This sections tests some general cloud computing knowledge to do with AWS and cloud infra in general.
It is expected that you will need to find the answers to some of these questions via Google.

Please write your answers in this file.

### Question 6.1

Which AWS region is the closest to Melbourne?

`Sydney`

### Question 6.2

What is the name of a cheap AWS EC2 instance that offers _at least_ 12 CPU cores and 16GB of RAM?
What are its specs (CPU cores, RAM) and cost per hour?

`a1.4xlarge, 16 cores, 32GB RAM, $0.408/hr`

How much will it cost to run this instance for two weeks?

`0.408 * 24 * 14 = 137.088`

### Question 6.3

Provide the AWS CLI command to copy all the contents of a S3 bucket to another S3 bucket on the same account.
The source bucket may contain nested files within "folders".

Source bucket: s3://mysource
Destination bucket: s3://mydest

```bash
# Your command here
aws s3 sync s3://mysource s3://mydest
```

### Question 6.4

Link to a section of library documentation showing how to stop an AWS EC2 instance using a Python client library (can be a howto, API reference, or tutorial).

https://boto3.amazonaws.com/v1/documentation/api/latest/guide/ec2-example-managing-instances.html

### Question 6.5

Describe, in 1-3 sentences

- What an AMI is and why it is useful for running EC2 instances
  
  `An Amazon Machine Image (AMI) provides the information required to launch an instance. You can launch multiple instances from a single AMI when you need multiple instances with the same configuration.`
- What IAM is and why it is useful when administering AWS
  
    `AWS Identity and Access Management (IAM) enables you to manage access to AWS services and resources securely. Using IAM, you can create and manage AWS users and groups, and use permissions to allow and deny their access to AWS resources.`
- Where you would add your SSH public key onto an EC2 instance in order to log in as the "ubuntu" user

    `.ssh/authorized_keys`

### Question 6.6

Create a new SSH key and paste both the public and private key into this file.

`ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDNz9krL9JTUDQKK3FJF+WZlnYuXYFLhiV+lv5a7KJG3VOuelwEFtzv6JhNHfpDS8MVvyyF31mi2oqNWtG4mdUmGUo40GfxUkuXWsEgt3cL98e/7Y1anverXDYzzE032RKGQ+XbCypUPj3FMHTd+hgXKcj38xILqkUWs6uPCW0zeNyZqprzJQb+I+KvdHS+q1fh5Dp7ucgmhBRsC5Y/x4g15FrWDYlaFno08gvda15IG6DsvWNKFxJ/KO9Yi7H79/sD0HMUZTxE9XterOdfYYTBAgdt6ar0yjSP7ZxqJpWz4O+Na9H8vumn+XW0blCCqlY+04/u129+GD8QAI8IYLzz9frM6s3cggNQsvIdB9GRYnISGYGnr9jUuoBevSvnVQKQ0r7g8uJIyVKUYgwzvWOVE05GIq4DHi1sncZfICrGgpa6p+0d7sEI4wqMCOakFnyuC12ToreLQAuuVol1jX1IgiOcxRYm26f4MAfDsyKckxguxvzmweL+BQs8Epelkk= bowen@bowen-laptop`

`-----BEGIN OPENSSH PRIVATE KEY-----
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
-----END OPENSSH PRIVATE KEY-----`

### Question 6.7

Write a bash one liner to create a new file called `foo.txt` which contains the text "Hello World!", followed by a newline

```bash
# Your command here
echo -e "Hello World! \n" > "foo.txt"
```

### Question 6.8

Write a bash one liner to create a new file which contains the text "Hello World!", followed by a newline, on a remote machine via SSH.

Remote machine hostname is `foo.com` and the user is `bar`. Assume you have all your SSH keys set up correctly on your machine and the target server.

```bash
# Your command here
echo -e "Hello World! \n" | ssh bar@foo.com -T "cat > /foo.txt"
```

### Question 6.9

Buildkite it a self-hosted CI system. Referring to the documentation via Google, is it possible to run a scheduled build at 2pm every Tuesday? Please link to the URL of the documentation where you found your answer.

`Yes`
https://buildkite.com/docs/pipelines/scheduled-builds
### Question 6.10

GitHub Actions is a CI system provided by GitHub, Referring to the documentation via Google, what is an environment variable that you could use to determine whether your bash script is running inside a Github Action?

`GITHUB_ACTIONS`

What kind of value would indicate that your script is running inside a GitHub Action?

`true`