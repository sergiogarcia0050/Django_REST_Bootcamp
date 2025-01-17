from cryptography.hazmat.primitives.serialization.pkcs12 import load_key_and_certificates
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization


from dotenv import load_dotenv
import os

load_dotenv()


#function to convert pfx to pem



def extract_pfx_to_pem(pfx_path: str, password: str, cert_path: str = "cert.pem", key_path: str = "key.pem"):
    """
    Extracts the private key and certificate from a PFX file and saves them as PEM files.

    :param pfx_path: Path to the .pfx file
    :param password: Password for the .pfx file
    :param cert_path: Output path for the extracted certificate file (default: cert.pem)
    :param key_path: Output path for the extracted private key file (default: key.pem)
    """
    try:
        # Read the PFX file
        # with open(pfx_path, "rb") as pfx_file:
        #     pfx_data = pfx_file.read()

        # # Load PFX file
        # pkcs12 = crypto.load_pkcs12(pfx_data, password.encode())

        # # Extract certificate
        # cert = crypto.dump_certificate(crypto.FILETYPE_PEM, pkcs12.get_certificate())

        # # Extract private key
        # key = crypto.dump_privatekey(crypto.FILETYPE_PEM, pkcs12.get_privatekey())

        # load the pfx file
        with open(pfx_path, "rb") as f:
            pfx_data = f.read()


        # load the private key and certificate from the pfx file
        private_key, certificate, additional_certs = load_key_and_certificates(
            pfx_data, password, default_backend()
        )

        private_key_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),)
        
        certificate_pem = certificate.public_bytes(encoding=serialization.Encoding.PEM)


        with open(key_path, "wb") as key_file:
                key_file.write(private_key_pem)

        with open(cert_path, "wb") as cert_file:
                 cert_file.write(certificate_pem)

        print("Private key and certificate exported successfully!")

        # Save certificate
        # with open(cert_path, "wb") as cert_file:
        #     cert_file.write(cert)

        # # Save private key
        # with open(key_path, "wb") as key_file:
        #     key_file.write(key)

        # print(f"Certificate saved to {cert_path}")
        # print(f"Private key saved to {key_path}")
        # return True

    except Exception as e:
        print(f"Error extracting PFX: {e}")
        return False



extract_pfx_to_pem( 'C:\\Users\\segarcia\\Desktop\\Django_REST_framework\\keys\\Firma Digital.pfx', b"901098244", "C:\\Users\\segarcia\\Desktop\\Django_REST_framework\\keys\\FCert.pem" ,"C:\\Users\\segarcia\\Desktop\\Django_REST_framework\\keys\\Fkey.pem")




# with open("path/to/private_key.pem", "rb") as key_file:
#     private_key = serialization.load_pem_private_key(
#         key_file.read(), password=b"your_password", backend=default_backend()
#     )

# with open("path/to/certificate.pem", "rb") as cert_file:
#     certificate = cert_file.read()

# wsse_security = Signature(private_key, certificate)