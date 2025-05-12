import brotli

data = b"Hello Hello Hello Hello Hello!"

# Compressing data
compressed_data = brotli.compress(data)
print("Compressed Data:", compressed_data)

# Decompressing data
decompressed_data = brotli.decompress(compressed_data)
print("Decompressed Data:", decompressed_data.decode())
