- [Streamified](#streamified)
  - [Problem Link](#problem-link)
  - [Solution](#solution)
  - [Insights](#insights)
  - [Reference](#reference)
  - [FLAG](#flag)
---

# Streamified
## Problem Link
<a href="https://utctf.live/challenges#Streamified-7" target="_blank">Streamified</a>
<br />
<br />

## Solution
<img src="https://github.com/user-attachments/assets/847ba067-52f8-474e-9414-36635473cb1f" width="50%"><br />
Download the attached file (`bitstring.txt`).<br />
<br />
<br />

<img src="https://github.com/user-attachments/assets/ad38a56e-1eaf-4eff-9be0-6df1bd1a10a3" width="100%">

```
$ file bitstring.txt
```
```
$ cat bitstring.txt
```
Opening `bitstring.txt` reveals a 625-character binary string (consisting of 0s and 1s).<br />
Notice that 625 is 25×25, indicating it might represent a QR code. To verify, convert these bits into a 25×25 black-and-white image with Python.<br />
<br />
<br />


<img src="https://github.com/user-attachments/assets/d922f2dd-226b-4617-a5c3-76cf7f126f56" width="100%">

```
$ vi solve.py
```
```
from PIL import Image

# Read bit string from 'bitstring.txt' (make sure the file has exactly 625 bits)
with open("bitstring.txt", "r") as f:
    bit_str = f.read().strip()  # Remove any trailing newline or spaces

# The image will be 25 x 25 = 625 bits
size = 25

# Create a new 1-bit image ('1' mode in Pillow)
# color=1 means the background is white (1)
img = Image.new("1", (size, size), color=1)

# Fill the image pixel by pixel
for i in range(size):
    for j in range(size):
        # If the bit is '1', set pixel to 0 (black)
        # If the bit is '0', set pixel to 1 (white)
        bit = bit_str[i * size + j]
        if bit == '1':
            img.putpixel((j, i), 0)  # black
        else:
            img.putpixel((j, i), 1)  # white

# Save the resulting image
img.save("output.png")
print("25x25 image ('output.png') created successfully!")
```
```
$ python3 solve.py
```
The resulting image (output.png) is a QR code. Scanning the code reveals the flag.<br />
<br />
<br />


<img src="https://github.com/user-attachments/assets/c6f884c9-2623-49a2-847f-34c9673fb516" width="10%">
<br />
<br />
<br />


## Insights
- Whenever encountering a string whose length is a perfect square (e.g., 625 = 25×25), consider the possibility of a QR code or some other 2D data representation.
<br />
<br />

## Reference
- 
<br />
<br />

## FLAG
utflag{b!t_by_b!t}