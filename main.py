import os
import sys
import pyttsx3
import customtkinter as ctk
import random
import threading
from deep_translator import GoogleTranslator

# Function to get the correct path to the icon file
def resource_path(relative_path):
    """Get the absolute path to the resource, works for dev and for PyInstaller."""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Create the main window
root = ctk.CTk()
root.title("German to Arabic Translator")
root.geometry("600x300")  # Adjusted size for better view
icon_path = resource_path("Data/pg.ico")
root.iconbitmap(icon_path)

engine = pyttsx3.init() # Initialize text-to-speech engine

# Load words from dictionary
try:
    with open(resource_path("Data/dictionary.txt"), "r", encoding="utf-8") as file:
        german_words = [line.strip() for line in file.readlines()]
except FileNotFoundError:
    german_words = ["Hund", "Katze", "Haus", "Baum", "Auto"]  # Fallback list

# Function to randomly select a German word and translate it to Arabic
def translate_word():
    german_word = random.choice(german_words)
    try:
        translated_text = GoogleTranslator(source="de", target="ar").translate(german_word)
        german_label.configure(text=german_word)  # Display German word
        arabic_label.configure(text=translated_text)  # Display Arabic translation
    except Exception as e:
        german_label.configure(text="Error")
        arabic_label.configure(text=f"Error: {e}")

# Function to speak the displayed German word
def speak_word():
    word = german_label.cget("text")  # Get the displayed word
    if word and word != "Error":
        threading.Thread(target=lambda: (engine.say(word), engine.runAndWait()), daemon=True).start()

# UI Layout
german_frame = ctk.CTkFrame(master=root, fg_color="gray")
german_frame.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True)

arabic_frame = ctk.CTkFrame(root, fg_color="white")
arabic_frame.pack(side=ctk.RIGHT, fill=ctk.BOTH, expand=True)

# Labels
german_label = ctk.CTkLabel(german_frame, text="", text_color="white", font=ctk.CTkFont("Arial", 40))
german_label.pack(expand=True)

arabic_label = ctk.CTkLabel(arabic_frame, text="", text_color="black", font=ctk.CTkFont("Arial", 40), wraplength=250, justify="center")
arabic_label.pack(expand=True)

# Buttons
speak_button = ctk.CTkButton(german_frame, text="▶", text_color="white", font=ctk.CTkFont("Arial", 30),width=50,fg_color="gray",command=speak_word)
speak_button.place(relx=0.9, rely=0.95, anchor='se')

translate_button = ctk.CTkButton(german_frame, text="🔄", font=ctk.CTkFont("Arial", 30),width=50,fg_color="gray",command=translate_word)
translate_button.place(relx=0.1, rely=0.95, anchor='sw')

# Load a word at startup
translate_word()
# Run main loop
root.mainloop()
