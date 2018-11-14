Run Length Encoding (RLE) Lossy Compression
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Run Length Encoding (RLE) is a simple data compression scheme. This scheme compresses strings by replacing consecutive characters by the number of occurrences of the character followed by that character.
Steps::

a) Pick the first character from source string.

b) Append the picked character to the destination string.

c) Count the number of subsequent occurrences of the picked character and append the count to destination string.

d) Pick the next character and repeat steps b) c) and d) if end of string is NOT reached.

Files Description::

text _and_image_rle_compression.py  === main file for image and text compression


image_data.py        === image for test purpose

How to run:
# install python3 

#open terminal and run

python3   text _and_image_rle_compression.py
