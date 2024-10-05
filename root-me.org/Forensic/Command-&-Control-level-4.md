- [Command \& Control - level 4](#command--control---level-4)
  - [Problem Link](#problem-link)
  - [Solution](#solution)
  - [Reference](#reference)
  - [FLAG](#flag)
---

# Command & Control - level 4
## Problem Link
<a href="https://www.root-me.org/en/Challenges/Forensic/Command-Control-level-4">Command & Control - level 4</a><br />
<br />
<br />

## Solution
<img src="https://github.com/user-attachments/assets/c5b56b99-3b66-4412-a4e7-526942608d67" width="100%">
Click the "Download the challenge" button to download the problem file. For the "Command & Control" challenges, the flag can be found in the same file for all of them.<br />
<br />
<br />


<img src="https://github.com/user-attachments/assets/e8f7b65c-41d4-431e-823c-84bf66d7b2ca" width="70%">

```
$ bzip2 -d ch2.tbz2
$ tar -zxvf ch2.tar
```
The downloaded file was compressed in two different formats, so I extracted them. After extracting, I found a memory dump file.<br />
Since the flag format is in the form of "IP:PORT", Attempted network scanning using the Volatility3 tool. However, none of the IPs found in the results matched the flag.<br />
<br />
Used Volatility 2 instead of Volatility 3. This is because the results can very between versions, and there are certain plugins available only in VOlatility 2.<br />
<br />
<br />


<img src="https://github.com/user-attachments/assets/cb176d9e-844f-4652-8683-6373eb849098" width="100%">

```
$ vol2 -f ch2.dmp imageinfo
```
Since Volatility 2 requires knowing the exact OS information for proper analysis, First checked the exact version of the Windows OS to Proceed with the investigation.<br />
<br />
Find "Win7SP0x86" version.<br />
<br />
<br />


<img src="https://github.com/user-attachments/assets/be91aa16-c5b8-48e4-a878-27f7b2b2fb94" width="100%">

```
$ vol2 -f ch2.dmp --profile=Win7SP0x86 consoles
```
To obtain the target IP address that the hacker aimed for, Reviewed the process from a previous challenge and suspected the use of a cmd command<br />
Upon further investigation using the "consoles" plugin, Confirmed that a supicious program(tcprelay.exe) was indeed used.<br />
<br />
<br />


<img src="https://github.com/user-attachments/assets/7164efd9-5537-49a2-b541-54c063c02e67" width="100%">

```
$ vol -f ch2.dmp windows.cmdline.CmdLine | grep "2772"
```
After using "grep" with the name of the suspicious program, the IP and PORT were found, leading to descovery of the flag.<br />
<br />
<br />


## Reference
<a href="https://downloads.volatilityfoundation.org/releases/2.4/CheatSheet_v2.4.pdf">Volatility2 manual</a><br />
<a href="https://book.hacktricks.xyz/generic-methodologies-and-resources/basic-forensic-methodology/memory-dump-analysis/volatility-cheatsheet">Volatility3 manual</a><br />
<br />
<br />

## FLAG
192.168.0.22:3389