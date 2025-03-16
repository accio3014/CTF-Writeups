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

