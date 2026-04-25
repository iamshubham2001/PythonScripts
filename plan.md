## Best Learning Order
- Basics (3–5 days)
- Scripts (5–7 days)
- APIs (3 days)
- Boto3 (5 days)
- Projects (ongoing)

## PHASE 1: Core Python (Don’t overdo this)

# Focus only on what’s useful:

# Must learn:
- Variables, data types
- Lists, dictionaries (VERY important)
- Loops (for, while)
- Conditions (if/else)
- Functions
- File handling

-> Example use:

- Read logs
- Parse configs
- Automate tasks

## PHASE 2: Scripting Mindset (This is where real learning starts)

Start writing scripts like:

1. File automation
# read file and count errors
with open("log.txt") as f:
    for line in f:
        if "error" in line:
            print(line)

2. OS Automation

Use:

import os

Examples:

Create files
Delete files
Run shell commands

3. Run Linux Commands

Use:

import subprocess

Example:

subprocess.run(["ls", "-l"])

## PHASE 3: Work with APIs (VERY IMPORTANT)

Most DevOps work = API calls

Use:

import requests

Example:

import requests
r = requests.get("https://api.github.com")
print(r.json())


## PHASE 4: AWS Automation

Use:
- Boto3

Example:

import boto3

ec2 = boto3.client('ec2')
response = ec2.describe_instances()
print(response)



## PHASE 5: Automation Projects (MANDATORY)

Do these 5 projects:

✅ Project 1

Script to:
- Check disk usage
- Send alert

✅ Project 2

Script to:
- Restart service if down

✅ Project 3

Script to:
- Upload file to S3

✅ Project 4

Script to:
- Create EC2 instance

✅ Project 5

Log analyzer:
- Read logs
- Count errors
- Output summary