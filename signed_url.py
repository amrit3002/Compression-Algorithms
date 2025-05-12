# pip install boto3 on bash


import datetime
import boto3
from botocore.signers import CloudFrontSigner
import rsa  # Install with: pip install rsa

# Replace with your CloudFront Key Pair ID
KEY_PAIR_ID = "APKAEXAMPLEID"
PRIVATE_KEY_PATH = "path/to/pk-xxxxxxxx.pem"

def rsa_signer(message):
    with open(PRIVATE_KEY_PATH, "rb") as key_file:
        private_key = rsa.PrivateKey.load_pkcs1(key_file.read())
    return rsa.sign(message, private_key, "SHA-1")

# Create a signed URL
cloudfront_signer = CloudFrontSigner(KEY_PAIR_ID, rsa_signer)

url = "https://your-cloudfront-domain.com/report.pdf"
expiration = datetime.datetime.utcnow() + datetime.timedelta(minutes=10)

signed_url = cloudfront_signer.generate_presigned_url(url, date_less_than=expiration)
print("Signed URL:", signed_url)

