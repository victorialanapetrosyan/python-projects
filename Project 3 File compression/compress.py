# out goal is to compress the demo.txt file and encode it
#  "compressed data" refers to information that has been encoded using a data compression algorithm to reduce its size. This process is used to save storage space, decrease transmission time over networks, and improve overall efficiency when dealing with large amounts of data.
# "encoding data" involves converting human readable text into a sequence of bytes for computer storage and transmission. The purpose of encoding is to prepare text data for saving to a file, sending over a network, or interacting with systems that expect byte-based input.
# there is a library which we can use for this:
import zlib
# this library has a compress() method
# we also need to import another library which helps us with encoding data
# This module provides functions for encoding and decoding data using various Base64 variants
import base64
# before we compress the file, we need to read it
data = open('demo.txt', 'r').read()

# our data needs to be in the form of bytes not strings
# specify the data, then the utf format
data_bytes = bytes(data,'utf-8')
# compress the data with the compress() function. This achieves optimal size of the data before encoding 
# use the b64encode() method to encode the byte objects
# Specify the data, and also specify the level of encoding which you want (no encoding)0-9(max level)
compressed_data = base64.b64encode(zlib.compress(data_bytes,9))
# let's write the encoded and compressed data to a new file
compressed_file = open('compressed.txt','w')
# the write function (from file handling) only writes strings to a file (our data is in bytes)
# so, let's decode the data so we can write it
    # decode() Converts a bytes object into a string object using a specified character encoding (e.g., UTF-8, ASCII, Latin-1).
decoded_data = compressed_data.decode('utf-8')
compressed_file.write(decoded_data)

# notice the file sizes of the demo.txt vs compressed.txt files


# now let's decompress the text in compressed.txt

# decode the data using b64decode() method
# b64decode() (from the base64 module):
    # Purpose: Decodes data that has been encoded using the Base64 scheme. Base64 is a binary-to-text encoding scheme that represents binary data in an ASCII string format. Returns the original decoded data as a bytes object
# so, our logic in line of code below is we would first decode the data, then decompress it
# Purpose of decompression:  restoring compressed data to its original, uncompressed form
decompressed_data = zlib.decompress(base64.b64decode(compressed_data))
print(decompressed_data)


