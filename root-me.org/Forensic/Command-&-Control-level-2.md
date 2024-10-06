- [Command \& Control - level 2](#command--control---level-2)
  - [Problem Link](#problem-link)
  - [Solution](#solution)
  - [FLAG](#flag)
---

# Command & Control - level 2
## Problem Link
<a href="https://www.root-me.org/en/Challenges/Forensic/Command-Control-level-2">Command & Control - level 2</a>
<br />
<br />

## Solution
<img src="https://github.com/user-attachments/assets/7519683a-c4e0-451c-992e-0b8e6f7dc7c5" width="100%">
Click the "Start the challenge" button to download the problem file.<br />
<br />
<br />


<img src="https://github.com/user-attachments/assets/ebbfcc4e-9878-4022-a16b-191383073621" width="70%">

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


## FLAG
WIN-ETSA91RKCFP