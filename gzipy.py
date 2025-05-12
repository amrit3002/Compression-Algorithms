import gzip

data = b"Hello Hello Hello Hello Hello!"  # Sample data to compress

# Compressing data
compressed_data = gzip.compress(data)
print("Compressed Data:", compressed_data)

# Decompressing data
decompressed_data = gzip.decompress(compressed_data)
print("Decompressed Data:", decompressed_data.decode())
