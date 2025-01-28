# every_day_for_Germany
Desktop applicaiton for learn Germany

App Picture 

<img width="1262" alt="Image" src="https://github.com/user-attachments/assets/7af351b1-3994-472e-81db-31de80e93a61" />


# German to Arabic Translator

## Description
This is a simple GUI-based application built using Python and the `customtkinter` library. The app randomly selects a German word from a predefined dictionary and translates it into Arabic using the `googletrans` library. It features a visually pleasing layout with two sections: one for the German word and the other for its Arabic translation.

---

## Features
- Randomly selects a German word.
- Translates the word into Arabic using Google Translate.
- Clean, user-friendly interface.
- Easily customizable dictionary of German words.
- Lightweight and responsive design.

---

## Installation

### Prerequisites
- **Python 3.8+**
- **Pip** (Python package installer)

### Step 1: Clone the Repository
```bash
git clone https://github.com/yossefibrahimmohamed/every_day_for_Germany.git
cd German-Arabic-Translator
```

### Step 2: Install Dependencies
Install the required Python libraries:
```bash
pip install customtkinter googletrans==4.0.0-rc1
```

### Step 3: Prepare the Files
Ensure the following folder structure is in place:
```
/German-Arabic-Translator
|-- main.py                     # The main script to run the app
|-- Data/
    |-- dictionary.txt          # Text file containing German words (one word per line)
    |-- pg.ico                  # Icon file for the app
```

- **`dictionary.txt`**: Add a list of German words, one per line.
- **`pg.ico`**: Add an icon for the application.

### Step 4: Run the Application
Run the app using the following command:
```bash
python main.py
```

---

## Usage
1. When the app starts, it displays a random German word and its Arabic translation.
2. The interface is divided into two sections:
   - **Left (Gray)**: Displays the German word.
   - **Right (White)**: Displays the Arabic translation.

---

## Packaging the App (Optional)
To create a standalone executable for distribution:

### Step 1: Install PyInstaller
```bash
pip install pyinstaller
```

### Step 2: Package the Application
Run the following command to bundle the app:
```bash
pyinstaller --onefile --add-data "Data:Data" --icon="Data/pg.ico" main.py
```

The packaged executable will be located in the `dist` folder.

---

## Troubleshooting
- **Missing `dictionary.txt`**: If the dictionary file is not found, the app uses a fallback list of German words.
- **Translation Errors**: Ensure you have an active internet connection, as the app requires online access to Google Translate.
- **Async Errors**: Use Python 3.8+ for compatibility with `asyncio`.

---

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with any improvements or additional features.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## Contact
For questions or suggestions, feel free to reach out:
- **Email**: [yossefmohamedsalah2001@gmail.com](mailto:yossefmohamedsalah2001@gmail.com)
- **GitHub**: [https://github.com/yossefibrahimmohamed/](https://github.com/yossefibrahimmohamed/)

