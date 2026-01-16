__version__ = "1.0.0"
import keyboard
import pyperclip
import time

# Key mapping dictionary for Ukrainian and English layouts.
layout_map = {
    'q': 'й', 'w': 'ц', 'e': 'у', 'r': 'к', 't': 'е', 'y': 'н', 'u': 'г', 
    'i': 'ш', 'o': 'щ', 'p': 'з', '[': 'х', ']': 'ї', 'a': 'ф', 's': 'і', 
    'd': 'в', 'f': 'а', 'g': 'п', 'h': 'р', 'j': 'о', 'k': 'л', 'l': 'д', 
    ';': 'ж', "'": 'є', 'z': 'я', 'x': 'ч', 'c': 'с', 'v': 'м', 'b': 'и', 
    'n': 'т', 'm': 'ь', ',': 'б', '.': 'ю'
}

# Reverse dictionary.
reverse_layout_map = {v: k for k, v in layout_map.items()}

def convert_text():
    # Copying text.
    keyboard.press_and_release('ctrl+c')
    
    # Waiting for the buffer to update.
    time.sleep(0.05)  # Додаємо затримку для стабільного копіювання
    text = pyperclip.paste()
    
    if not text:
        return

    # Converting text.
    new_text = ""
    for char in text:
        lower_char = char.lower()
        if lower_char in layout_map:
            res = layout_map[lower_char]
            new_text += res.upper() if char.isupper() else res
        elif lower_char in reverse_layout_map:
            res = reverse_layout_map[lower_char]
            new_text += res.upper() if char.isupper() else res
        else:
            new_text += char

    # Pasting converted text.
    pyperclip.copy(new_text)
    keyboard.press_and_release('ctrl+v')

# Setting up the hotkey.
keyboard.add_hotkey('f2', convert_text)

print("Program is running. Press F2 to convert text.")
keyboard.wait()