from nacl.public import PrivateKey, Box
from nacl.utils import random
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from secrets import token_bytes
from tkinter import messagebox, filedialog
from .utils import save_encryption_state, load_encryption_state
import tkinter as tk


def encrypt_action(hide_decrypt_fields_callback, input_box, output_box):
    """
    Encrypts the input text using AES-GCM and protects the key with ECDH.
    :param hide_decrypt_fields_callback: A callback function to hide decryption fields
    :param input_box: The input box widget from the GUI
    :param output_box: The output box widget to display results
    """
    # Usa il callback per nascondere i campi di decifrazione
    hide_decrypt_fields_callback()

    # Ottieni il testo dalla casella di input
    input_text = input_box.get("1.0", tk.END).strip()

    if not input_text:
        messagebox.showwarning("Warning", "Enter text or upload a file!")
        return

    try:
        # Logica per crittografare il testo...
        aes_key = token_bytes(32)
        aes_gcm = AESGCM(aes_key)
        nonce = random(12)
        encrypted_data = aes_gcm.encrypt(nonce, input_text.encode('utf-8'), None)

        # Genera una coppia di chiavi ECDH
        local_private_key = PrivateKey.generate()
        remote_private_key = PrivateKey.generate()
        remote_public_key = remote_private_key.public_key

        # Crea la chiave condivisa
        box = Box(local_private_key, remote_public_key)
        shared_key = box.encrypt(aes_key)

        # Salva lo stato cifrato
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON File", "*.json")])
        if file_path:
            save_encryption_state(file_path, nonce, encrypted_data, shared_key, {
                "type": "ECDH",
                "local_private_key": local_private_key,
                "remote_public_key": remote_public_key
            })

        # Mostra i dati cifrati nella GUI
        output_box.config(state=tk.NORMAL)
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, f"Encrypted Data (AES-GCM):\n{encrypted_data.hex()}\n")
        output_box.insert(tk.END, f"Nonce:\n{nonce.hex()}\n")
        output_box.insert(tk.END, f"Shared Key:\n{shared_key.hex()}\n")
        output_box.config(state=tk.DISABLED)

    except Exception as e:
        messagebox.showerror("Error", f"Error during encryption: {str(e)}")



def decrypt_action(output_box):
    """
    Decrypts the encrypted data and displays the original input in the output box.
    :param output_box: The output box widget to display results
    """
    try:
        # Seleziona il file JSON con lo stato cifrato
        file_path = filedialog.askopenfilename(filetypes=[("JSON File", "*.json")])
        if not file_path:
            return

        # Carica lo stato della cifratura
        nonce, encrypted_data, shared_key, encryption_details = load_encryption_state(file_path)

        # Recupera le chiavi per la decifratura
        local_private_key = encryption_details["local_private_key"]
        remote_public_key = encryption_details["remote_public_key"]
        box = Box(local_private_key, remote_public_key)

        # Decifra la chiave AES
        aes_key = box.decrypt(shared_key)

        # Decifra il testo originale usando AES-GCM
        aes_gcm = AESGCM(aes_key)
        decrypted_data = aes_gcm.decrypt(nonce, encrypted_data, None)

        # Mostra il testo decifrato nel riquadro dell'output
        output_box.config(state=tk.NORMAL)
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, f"Decrypted Data:\n{decrypted_data.decode('utf-8')}")
        output_box.config(state=tk.DISABLED)

    except Exception as e:
        messagebox.showerror("Error", f"Error during decryption: {str(e)}")

