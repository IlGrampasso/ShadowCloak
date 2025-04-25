import tkinter as tk
from .encryption import encrypt_action, decrypt_action
from .constants import update_explanation

# Function to show decryption fields
def show_decryption_fields():
    """Displays the fields for the decryption phase."""
    encrypted_data_label.grid(row=6, column=0, sticky="w")
    encrypted_data_input.grid(row=6, column=1, pady=5)
    nonce_label.grid(row=7, column=0, sticky="w")
    nonce_input.grid(row=7, column=1, pady=5)
    encrypted_key_label.grid(row=8, column=0, sticky="w")
    encrypted_key_input.grid(row=8, column=1, pady=5)

# Function to hide decrypt fields
def hide_decrypt_fields():
    """Hides the fields for the decryption phase."""
    encrypted_data_label.grid_remove()
    encrypted_data_input.grid_remove()
    nonce_label.grid_remove()
    nonce_input.grid_remove()
    encrypted_key_label.grid_remove()
    encrypted_key_input.grid_remove()

def main_window():
    """Main function to create and start the GUI."""
    # Creating the main Tkinter root window
    root = tk.Tk()
    root.title("Simple Cipher Tool")

    # Main frame
    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack()

    # Text box for input
    tk.Label(frame, text="Encryption: Enter the text you want to encrypt using AES.", fg="blue").grid(row=0, column=0, columnspan=2, sticky="w")
    input_box = tk.Text(frame, width=50, height=10)
    input_box.grid(row=1, column=0, columnspan=2, pady=5)

    # Button to encrypt
    #encrypt_button = tk.Button(frame, text="Encrypt", command=lambda: [encrypt_action(hide_decrypt_fields, input_box), update_explanation("encrypt", explanation_box)])

    encrypt_button = tk.Button(frame, text="Encrypt", command=lambda: [encrypt_action(hide_decrypt_fields, input_box, output_box), update_explanation("encrypt", explanation_box)])


    encrypt_button.grid(row=4, column=0, pady=5)

    # Button to decrypt
    #decrypt_button = tk.Button(frame, text="Decrypt",command=lambda: [decrypt_action(), update_explanation("decrypt", explanation_box)])
    decrypt_button = tk.Button(frame, text="Decrypt", command=lambda: [decrypt_action(output_box), update_explanation("decrypt", explanation_box)])

    decrypt_button.grid(row=4, column=1, pady=5)

    # Decryption fields
    tk.Label(frame, text="Decryption: Load a JSON file to fill in the fields below.", fg="blue").grid(row=5, column=0, columnspan=2, sticky="w")
    global encrypted_data_label, encrypted_data_input, nonce_label, nonce_input, encrypted_key_label, encrypted_key_input
    encrypted_data_label = tk.Label(frame, text="Encrypted Data:")
    encrypted_data_input = tk.Text(frame, width=50, height=2)
    nonce_label = tk.Label(frame, text="Nonce:")
    nonce_input = tk.Text(frame, width=50, height=2)
    encrypted_key_label = tk.Label(frame, text="Encrypted AES Key:")
    encrypted_key_input = tk.Text(frame, width=50, height=2)

    # Text box for output
    tk.Label(frame, text="Output:").grid(row=9, column=0, sticky="w")
    global output_box
    output_box = tk.Text(frame, width=50, height=10)
    output_box.grid(row=10, column=0, columnspan=2, pady=5)

    # Educational explanation box
    tk.Label(frame, text="Console:", fg="green").grid(row=11, column=0, sticky="w")
    global explanation_box
    explanation_box = tk.Text(frame, width=50, height=10, wrap=tk.WORD, state=tk.DISABLED, background='black', fg="green")
    explanation_box.grid(row=12, column=0, columnspan=2, pady=5)

    # Initially hide decryption fields
    hide_decrypt_fields()

    # Start the Tkinter main loop
    root.mainloop()
