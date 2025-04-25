import json
from nacl.public import PrivateKey, PublicKey

def save_encryption_state(file_path, nonce, encrypted_data, shared_key, encryption_details):
    try:
        local_private_key_bytes = encryption_details["local_private_key"]._private_key
        remote_public_key_bytes = encryption_details["remote_public_key"]._public_key

        data_to_save = {
            "nonce": nonce.hex(),
            "encrypted_data": encrypted_data.hex(),
            "shared_key": shared_key.hex(),
            "encryption_type": encryption_details["type"],
            "local_private_key": local_private_key_bytes.hex(),
            "remote_public_key": remote_public_key_bytes.hex()
        }

        with open(file_path, "w") as f:
            json.dump(data_to_save, f)
        print(f"State saved in {file_path}")
    except Exception as e:
        print(f"Error saving state: {str(e)}")


def load_encryption_state(file_path):
    try:
        with open(file_path, "r") as f:
            saved_data = json.load(f)

        # Check for required fields
        missing_fields = [field for field in ["nonce", "encrypted_data", "shared_key", "encryption_type"] if field not in saved_data]
        if missing_fields:
            raise ValueError(f"Missing fields: {', '.join(missing_fields)}")

        # Extract data
        nonce = bytes.fromhex(saved_data["nonce"])
        encrypted_data = bytes.fromhex(saved_data["encrypted_data"])
        shared_key = bytes.fromhex(saved_data["shared_key"])

        # Recreate keys
        local_private_key = PrivateKey(bytes.fromhex(saved_data["local_private_key"]))
        remote_public_key = PublicKey(bytes.fromhex(saved_data["remote_public_key"]))

        encryption_details = {
            "type": saved_data["encryption_type"],
            "local_private_key": local_private_key,
            "remote_public_key": remote_public_key
        }

        return nonce, encrypted_data, shared_key, encryption_details
    except Exception as e:
        raise ValueError(f"Error loading state: {str(e)}")
