# ShadowCloak

ShadowCloak is an educational tool designed for encrypting and decrypting data using AES (Advanced Encryption Standard) and ECDH (Elliptic-Curve Diffie-Hellman) key exchange. It provides an intuitive graphical user interface built with `tkinter`.

## **Key Features**
- **Data Encryption:**
  - Encrypts data securely using AES-GCM.
  - Protects the AES key through ECDH key exchange.
- **Data Decryption:**
  - Decrypts encrypted data to retrieve the original input text.
  - Supports loading encrypted data from a JSON file.
- **Educational Guide:**
  - Displays helpful messages to explain each step of the encryption and decryption processes.

## **Requirements**
- Python 3.8 or later
- Required libraries:
  - `tkinter` (included with Python standard library)
  - `cryptography`
  - `PyNaCl`

To install the required libraries, run:
```bash
pip install -r requirements.txt
