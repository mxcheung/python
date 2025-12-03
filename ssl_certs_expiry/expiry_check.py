from cryptography import x509
from cryptography.hazmat.backends import default_backend

def get_local_certificate_expiry(path):
    with open(path, "rb") as f:
        cert_bytes = f.read()

    cert = x509.load_pem_x509_certificate(cert_bytes, default_backend())
    return cert.not_valid_after

print(get_local_certificate_expiry("certificate.pem"))