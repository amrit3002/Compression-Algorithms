def rle_compress(data):
    compressed = ""
    i = 0

    while i < len(data):
        count = 1
        while i + 1 < len(data) and data[i] == data[i + 1]:
            count += 1
            i += 1
        compressed += data[i] + str(count)
        i += 1
    
    return compressed if len(compressed) < len(data) else data  # Return original if compression is ineffective

def rle_decompress(compressed):
    decompressed = ""
    i = 0

    while i < len(compressed):
        char = compressed[i]
        count = int(compressed[i + 1])
        decompressed += char * count
        i += 2

    return decompressed

# Example usage
data = "AAABBBCCCCCDDDDD"
compressed_data = rle_compress(data)
decompressed_data = rle_decompress(compressed_data)

print("Original Data:", data)
print("Compressed Data:", compressed_data)
print("Decompressed Data:", decompressed_data)
