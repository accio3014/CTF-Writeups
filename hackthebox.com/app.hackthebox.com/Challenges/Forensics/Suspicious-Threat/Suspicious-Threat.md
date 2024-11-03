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
Click the "Start Instance" button to launch the server.<br />
<br />
<br />


<img src="https://github.com/user-attachments/assets/2cd3bf9b-b0be-477d-a587-69c5da657a97" width="100%">

```
host : 94.237.60.32:36419
username : root
password : hackthebox
```
```
$ ssh root@94.237.60.32 -p 36419
```
When the instance is started, the host appears. User the provided username and password form challenge information to cannect.<br />
<br />
<br />

<img src="https://github.com/user-attachments/assets/53c8641c-bc76-4759-8b4a-b9a6c1550212" width="100%">

```
$ vol -f ch2.dmp windows.info
```
This is the view after connecting to the server.<br />
<br />
<br />


<img src="https://github.com/user-attachments/assets/d9073642-1445-450b-ab4b-d1671cfb7f4d" width="100%">

```
$ ldd /bin/ls
```

Upon reviewing the challenge, an error related to library linking was noted. While using the "ldd" command to invertigate, a suspicious file named(libc.hook.so.6) was discovered in the output of the "ls" command.<br />
<br />
<br />

<img src="https://github.com/user-attachments/assets/c71bfd38-f6b5-4700-8fe5-080b492679dd" width="100%">

```
$ mv /lib/x86_64-linux-gnu/libc.hook.so.6 ./
$ ls -ahl
```

After moving the suspicious file from the library path to a different location and running the "ls" command again, an error message appeared. This indicates that the important folder mentioned in the problem will now be revealed.<br />
<br />
<br />


<img src="https://github.com/user-attachments/assets/a98470a0-09c5-4714-a7cf-75ecbc90d3e7" width="100%">
<img src="https://github.com/user-attachments/assets/4e6033b7-39c7-4cc2-8736-4be461726b85" width="100%">
<img src="https://github.com/user-attachments/assets/f25980fb-4076-4714-bd5c-7a38908cbb27" width="100%">

```
$ ls -ahl /var/
$ ls -ahl /var/pr3l04d_
$ cat /var/pro3l04d_/flag.txt
```

While checking all folders, a previously hidden folder(pr3l04d_) was found in the "/var" path.<br />
Upon examining its contents, "flag.txt" was located, and the flag was successfully obtained.<br />
<br />
<br />

## Insights
- The "ldd" command can be used to check the livraries linked to basic commands.
- Libraries can be used to hide or reveal specific folders and files.
<br />
<br />

## Reference
- 
<br />
<br />

## FLAG
HTB{Us3rL4nd_R00tK1t_R3m0v3dd!}