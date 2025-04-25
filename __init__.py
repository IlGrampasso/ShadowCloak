from .gui import main_window
from .encryption import encrypt_action, decrypt_action
from utils import save_encryption_state, load_encryption_state
from constants import update_explanation

from src.shadowcloak.gui import main_window

if __name__ == "__main__":
    main_window()