VOICE DICTIONARY APP (Streamlit + Google Text-to-Speech)

DESCRIPTION:
-------------
This is a web dictionary application built using Streamlit and Google Text-to-Speech (gTTS).
It allows users to:
- View a list of saved words and their meanings.
- Search for the meaning of a word.
- Hear pronunciation of the word and its meaning.
- Add new words and their meanings to the dictionary.
- Exit the application with a thank-you message.


FEATURES:
----------
✓ View dictionary entries  
✓ Search for word meanings  
✓ Listen to word pronunciation (with gTTS)  
✓ Add new words  
✓ Exit screen with farewell message  

FILES:
-------
- `voice_dictionary.py` : Main Python script for the Streamlit app.
- `dictionary.txt` : Stores all dictionary entries in the format `word <tab><tab> meaning`.
- `dict_1_logo.png` : Logo image displayed on top of the app interface.

REQUIREMENTS:
--------------
Install the following packages before running:
- streamlit
- gtts
- Python 3.6+

Install these files using pip:


HOW TO RUN:
------------
1. Make sure Python and pip are installed.
2. Place the following files in the same directory:
   - `voice_dictionary.py`
   - `dictionary.txt` (can be empty initially)
   - `dict_1_logo.png`
3. Open terminal/command prompt in that directory.
4. Run the app using: python -m streamlit run voice_dictionary.py


USAGE INSTRUCTIONS:
--------------------
- Start Page: 	Displays all existing words.
- Click "Click continue" to move to the main menu.
- Search Mode:	Type a word to find its meaning and hear pronunciation.
- Add Mode: 	Enter a new word and its meaning. It will be saved to the dictionary file.
- Exit Program: Displays a thank-you message and ends interaction.

NOTES:
-------
- The pronunciation feature uses Google TTS and requires internet access.
- Dictionary data is stored persistently in `dictionary.txt`.
- Duplicate word entries are prevented.
- Use refresh (Streamlit rerun) after adding new words.


AUTHOR:
--------
Made by Muhammad Shameer Asim

