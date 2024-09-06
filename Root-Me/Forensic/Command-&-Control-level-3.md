- [Command \& Control - level 3](#command--control---level-3)
  - [Problem Link](#problem-link)
  - [Solution](#solution)
  - [FLAG](#flag)
---

# Command & Control - level 3
## Problem Link
<a href="https://www.root-me.org/en/Challenges/Forensic/Command-Control-level-3">Command & Control - level 3</a>
<br />
<br />

## Solution
<img src="https://github.com/user-attachments/assets/767dbb31-5ad0-4ea8-a48c-e64c55fca4d2" width="100%">
Click the "Download the challenge" button to download the problem file.<br />
<br />
<br />


<img src="https://github.com/user-attachments/assets/e8f7b65c-41d4-431e-823c-84bf66d7b2ca" width="70%">

```
$ bzip2 -d ch2.tbz2
$ tar -zxvf ch2.tar
```
The downloaded file was compressed in two different formats, so I extracted them. After extracting, I found a memory dump file.<br />
The problem's flag is the MD5 hash of the full path where the malware was executed, so need to analyze the dump file to find the flag.<br />
<br />
Use the Volatility3 tool to analyze the memory.<br />
<br />
<br />


<img src="https://github.com/user-attachments/assets/cde8b76e-ec5a-4a44-aefa-d461d096c71f" width="100%">

```
$ vol -f ch2.dmp windows.info
```
Using the windows.info option, I confirmed that the system is running Windows OS. <br />
Volatility has various options, and will make use of them to find the flag.<br />
<br />
<br />


<img src="https://github.com/user-attachments/assets/3a531288-f017-438d-9ee0-2b67113f24ef" width="100%">

```
$ vol -f ch2.dmp windows.pstree
```
Using the windows.pstree option to check the processes, noticed something unusual: after iexplore.exe was executed, cmd.exe was launched.<br />
This led me to suspect that the malware is disguising itself as iexplore.exe.
<br />
<br />


<img src="https://github.com/user-attachments/assets/47217069-a61d-45a4-b5e9-1d067be21fc4" width="100%">

```
$ vol -f ch2.dmp windows.cmdline.CmdLine | grep "2772"
```
Using an option that allows me to check the commands executed in cmd, searched for the PID 2722, which is the process suspected to be malware.<br />
Confirmed that it was not located in the default path for iexplore.exe, leading me to be certain it is malware.
<br />
<br />


<img src="https://github.com/user-attachments/assets/b8eea440-b19e-40a6-82a2-5b43bab056f9" width="100%">

```
$ md5 -s "C:\Users\John Doe\AppData\Roaming\Microsoft\Internet Explorer\Quick Launch\iexplore.exe"
```
The flag is the MD5 hash of the full path of the malware, I converted the full path of the process with PID 2722 into its MD5 hash, and successfully obtained the flag.
<br />
<br />


## FLAG
49979149632639432397b3a1df8cb43d