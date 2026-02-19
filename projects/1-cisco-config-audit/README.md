This folder contains small Python scripts to run a verification command across multiple Cisco devices and save the output per device.
It’s written as a learning project, starting with a basic script and then adding exception handling for reliability at scale.

Use Case (Example)

In large environments (50+ devices), it’s common to verify whether a particular configuration section exists across many routers/switches.
Example command used in this project:

show running-config | section crypto ssl policy


Note: A Cisco advisory (e.g., CVE-2025-20363) can be one real-world reason to run this check, but the scripts are reusable for any “run a show command across many devices” task.

Scripts
1) crypto_ssl_policy_audit.py (Basic)

What it does

Prompts for username/password securely (getpass)

Connects to each device in the IP list

Runs the verification command

Saves output to <IP>.txt


2) crypto_ssl_audit_with_exception.py (With Exception Handling)

What it does

Same behaviour as the basic script

The enhanced script ) includes exception handling to prevent the program from stopping if a device fails.
It handles:
NetmikoAuthenticationException – Incorrect credentials
NetmikoTimeoutException / TimeoutError – Device unreachable or SSH blocked
Generic Exception – Any unexpected errors

Examples of the error when you don't use an exception

<img width="916" height="395" alt="image" src="https://github.com/user-attachments/assets/3705729a-f6db-4047-a204-bd0fdae5faa4" />
