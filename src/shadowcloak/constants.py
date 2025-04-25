'''
# Function to update the educational guide
def update_explanation(step):
    explanations = {
        "encrypt": "You have encrypted the data with AES. The AES key has been protected using ECDH key exchange.",
        "decrypt": "You have decrypted the AES key using ECDH and are now retrieving the original data.",
        "load_file": "You have loaded a JSON file, and the fields have been automatically filled in based on the saved encryption details."
    }
    explanation_box.config(state=tk.NORMAL)
    explanation_box.delete("1.0", tk.END)
    explanation_box.insert(tk.END, explanations.get(step, ""))
    explanation_box.config(state=tk.DISABLED)'''

import tkinter as tk

def update_explanation(step, explanation_box):
    explanations = {
        "encrypt": "You have encrypted the data with AES. The AES key has been protected using ECDH key exchange.",
        "decrypt": "You have decrypted the AES key using ECDH and are now retrieving the original data.",
        "load_file": "You have loaded a JSON file, and the fields have been automatically filled in based on the saved encryption details."
    }
    explanation_box.config(state=tk.NORMAL)
    explanation_box.delete("1.0", tk.END)
    explanation_box.insert(tk.END, explanations.get(step, ""))
    explanation_box.config(state=tk.DISABLED)
