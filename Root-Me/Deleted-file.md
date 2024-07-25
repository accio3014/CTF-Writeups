- [Deleted file](#deleted-file)
  - [FLAG](#flag)
---

# Deleted file
<img src="https://github.com/user-attachments/assets/30604cc1-2106-44b4-b4d1-ac1b9d750ec1" width="100%">
Click the "Start the challenge" button to download the problem file.
<br />
<br />
<br />

<img src="https://github.com/user-attachments/assets/4deaa535-517b-4fe5-a242-24ab16826b3b" width="70%">

```
$ gzip -d ch39.gz
$ tar -zxvf ch39
```
Check the problem file, see that it is compressed twice in different formats. Use commands to extract it. usb.image file appears to be a FAT format disk file. <br />
Flag format is firstname_lastname. Typically, the first name of a foreigner is expected to be more than 10 letters long.
<br />
<br />
<br />

<img src="https://github.com/user-attachments/assets/c3da7179-d465-411a-9363-2885c9f8d96c" width="50%">

```
$ strings usb.image -n 10
```
Using the strings command to search for text that is 10 characters or longer, I found something suspicious, it the flag.
<br />
<br />
<br />

## FLAG
javier_turcot