- [Docker layers](#docker-layers)
  - [Problem Link](#problem-link)
  - [FLAG](#flag)
---

# Docker layers
## Problem Link
<a href="https://www.root-me.org/en/Challenges/Forensic/Docker-layers">Docker layers</a>
<br />
<br />


<img src="https://github.com/user-attachments/assets/40791dd9-6087-4771-abf0-15f09f956d0a" width="100%">
Click the "Start the challenge" button to download the problem file.<br />
<br />
<br />


<img src="https://github.com/user-attachments/assets/019f0dbe-df3c-4251-9897-55407062081d" width="70%">

```
$ tar -zxvf ch29.tar
```
The file provided in the problem is compressed as a tar file, so you'll need to extract it.<br />
After extracting, you'll find that there are more compressed files inside.<br />
<br />
<br />


<img src="https://github.com/user-attachments/assets/3697c370-94c8-4402-97dc-a9af5181efac" width="100%">

```
$ grep -ir "pass"
```
After reviewing the problem, I noticed a section about the password. I checked inside the Docker container for anything starting with "pass".<br />
The reason I didn't search for "password" directly is that, in Linux, it's more common to use terms like "passwd" or other words that start with "pass" rather than the full word "password". That's why I searched using "pass".<br />
After checking the search results, I saw a command that uses AES encryption, and I found files named pass.txt and flag.enc.<br />
<br />
<br />


<img src="https://github.com/user-attachments/assets/60feff2a-225e-425b-b2ee-52ce3f4c11f6" width="100%">

```
$ find ./ -iname "pass.txt"
$ find ./ -iname "flag.enc"
$ tar -zxvf 316bbb8c58be42c73eefeb8fc0fdc6abb99bf3d5686dd5145fc7bb2f32790229.tar
$ tar -zxvf 3309d6da2bd696689a815f55f18db3f173bc9b9a180e5616faf4927436cf199d.tar
$ cat pass.txt
$ cat flag.enc
```
I tried to find the pass.txt and flag.enc files, but they didn’t show up in the search. I realized they might be compressed in a tar file, so I began extracting the files in sequence.<br /> 
Eventually. After checking the contents, I found information related to a password and an encrypted message.<br />
Now, I need to decrypt this message to get the flag.<br />
<br />
<br />


<img src="https://github.com/user-attachments/assets/6c8e94d9-bd6a-4eb8-851b-a2f33a820c3d" width="100%">

```
$ openssl enc -d -aes-256-cbc -iter 10 -pass pass:$(cat ./pass.txt) -in flag.enc -out flag.txt
$ cat flag.txt
```
Using the encryption command as a reference, I proceeded with decryption and successfully retrieved the flag.<br />
<br />
<br />


## FLAG
Well_D0ne_D0ckER_L@y3rs_Inspect0R