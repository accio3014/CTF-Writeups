- [Suspicious Threat](#suspicious-threat)
  - [Problem Link](#problem-link)
  - [Solution](#solution)
  - [Insights](#insights)
  - [Reference](#reference)
  - [FLAG](#flag)
---

# Suspicious Threat
## Problem Link
<a href="https://app.hackthebox.com/challenges/Suspicious%2520Threat" target="_blank">Suspicious Threat</a>
<br />
<br />

## Solution
<img src="https://github.com/user-attachments/assets/8edd065a-9abf-4bae-844b-2c9a4a2fd5d5" width="100%">
Click the "Start Instance" button to launch the server.
<br />
<br />


<img src="https://github.com/user-attachments/assets/2cd3bf9b-b0be-477d-a587-69c5da657a97" width="100%">
- host : 94.237.60.32:36419
- account : root
- password : hackthebox
  
```
$ bzip2 -d ch2.tbz2
$ tar -zxvf ch2.tar
```
The downloaded file was compressed in two different formats, so I extracted them. After extracting, I found a memory dump file. The problem's flag is described as "workstation’s hostname," so I need to analyze the dump file to find the flag.<br />
<br />
Use the Volatility3 tool to analyze the memory.<br />
<br />
<br />

<img src="https://github.com/user-attachments/assets/4b5291ea-2473-48ed-bd17-0298c2b13d5b" width="100%">

```
$ vol -f ch2.dmp windows.info
```
Using the windows.info option, I confirmed that the system is running Windows 7. <br />
Since the Volatility tool supports various plugins, I will use a plugin that checks the contents of registry keys to find the flag.<br />
<br />
<br />


<img src="https://github.com/user-attachments/assets/310177d4-03c8-412e-8dcb-7e382d5f2be6" width="100%">

```
$ vol -f ch2.dmp windows.registry.printkey --key "ControlSet001\\Control\\ComputerName\\ComputerName"
```

For Windows, the hostname is usually stored in the <br />
ControlSet001\\Control\\ComputerName\\ComputerName <br />
path. By using the windows.registry.printkey option to check the registry key contents, I was able to find the flag.<br />
<br />
<br />

## Insights

## Reference
<a href="https://downloads.volatilityfoundation.org/releases/2.4/CheatSheet_v2.4.pdf" target="_blank">Volatility2 manual</a><br />
<a href="https://book.hacktricks.xyz/generic-methodologies-and-resources/basic-forensic-methodology/memory-dump-analysis/volatility-cheatsheet" target="_blank">Volatility3 manual</a><br />
<br />
<br />

## FLAG
WIN-ETSA91RKCFP