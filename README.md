# Executable Debugger
![Home Screen](/images/HOME_SCREEN.png)

This program enables a user to input a file into our webapp. We execute the file in an AWS virtual machine instance and generate a log file of the running processes in the executable. The log file is generated on the screen to help experienced developers make an informed decision.

Created by Neal, Gautam, Sahil, and Rishi

## Why Did We Make This Developer Tool?

Information security is vital for corporations and government partners. Using open source file distributions can pose a potential risk for employers. Keeping our focus on security enables a safer internet for everyone.

## What Services Do We Use?

* Amazon EC2 for creating Virtual Machines
* Flask for Website Deployment
* psutils Python library for dynamic analysis of running executable processes

## How To Run Our Code?

1. Git clone this repository.
1. Input AWS credentials
1. Run main.py

## What Metrics Do You Receive?
* Static Analysis to search for potentially harmful strings, such https requests
* Information about process(es) created after running the exec

