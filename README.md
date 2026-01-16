# LayoutConverter ⌨️

A Python-based utility to quickly fix text typed in the wrong keyboard layout (e.g., typing "ghbdtn" instead of "привіт").

## ✨ Features
* **Ukrainian Support**: Converts between Ukrainian and English layouts.
* **Russian Support**: Converts between Russian and English layouts.
* **Hotkey Activation**: Uses `F2` to trigger the conversion instantly.
* **Case Sensitivity**: Preserves uppercase and lowercase letters during conversion.
## Technical Details
The scripts use the following logic:

Key Mapping: Hardcoded dictionaries map English characters to their Cyrillic counterparts (e.g., 'q' to 'й').

Clipboard Management: Uses pyperclip to interact with the system buffer and handle text transfer.

Automation: Uses the keyboard library to simulate Ctrl+C and Ctrl+V commands and listen for the F2 hotkey.

Stability: Includes a short delay (time.sleep(0.05)) to ensure the clipboard updates correctly before processing.

Note: On some systems (like Linux), the keyboard library requires root/sudo privileges to capture global hotkeys.

## 🚀 Getting Started

### Prerequisites
You need Python installed on your system. You also need to install the following dependencies:
```bash
pip install -r requirements.txt
