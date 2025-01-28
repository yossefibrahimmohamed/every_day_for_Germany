import os
import sys
import customtkinter as ctk
import random
import asyncio
from googletrans import Translator

# Function to get the correct path to the icon file
def resource_path(relative_path):
    """Get the absolute path to the resource, works for dev and for PyInstaller."""
    try:
        # PyInstaller creates a temp folder and stores the path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Create the main window
root = ctk.CTk()
root.title("German to Arabic Translator")
root.geometry("600x300")  # w x h Adjusted size for better view

# Set the icon using the resource_path function
icon_path = resource_path("Data/pg.ico")
root.iconbitmap(icon_path)

# Create a translator instance
translator = Translator()

# Load German words from a file
try:
    with open(resource_path("Data/dictionary.txt"), "r", encoding="utf-8") as file:
        german_words = [line.strip() for line in file.readlines()]
except FileNotFoundError:
    german_words = ["Hund", "Katze", "Haus", "Baum", "Auto"]  # Fallback list

# Function to randomly select a German word and translate it to Arabic
async def translate_random_word():
    german_word = random.choice(german_words)
    try:
        translation = await translator.translate(german_word, src="de", dest="ar")
        german_label.configure(text=german_word, text_color="white", font=ctk.CTkFont("Arial", 40))
        arabic_label.configure(text=translation.text, text_color="black", font=ctk.CTkFont("Arial", 40))
    except Exception as e:
        german_label.configure(text="Error", text_color="white")
        arabic_label.configure(text=f"Error: {e}", text_color="black")

# Wrapper function to run the async translate function
def translate_random_word_wrapper():
    asyncio.run(translate_random_word())

# German output section
german_frame = ctk.CTkFrame(master=root, fg_color="gray")  # Gray background
german_frame.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True)

# Arabic output section
arabic_frame = ctk.CTkFrame(root, fg_color="white")  # White background
arabic_frame.pack(side=ctk.RIGHT, fill=ctk.BOTH, expand=True)

# Label to display the random German word
german_label = ctk.CTkLabel(german_frame, text="", text_color="white", font=ctk.CTkFont("Arial", 40))
german_label.pack(expand=True)

# Arabic translation label
arabic_label = ctk.CTkLabel(arabic_frame, text="", text_color="black", font=ctk.CTkFont("Arial", 40), wraplength=250, justify="center")
arabic_label.pack(expand=True)

# Translate the word once when the program runs
translate_random_word_wrapper()

# Run the main loop
root.mainloop()