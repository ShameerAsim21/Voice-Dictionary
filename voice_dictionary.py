import streamlit as st
import re
import os
from gtts import gTTS
from io import BytesIO

DICTIONARY_FILE = 'dictionary.txt'

# Load dictionary from file
def load_dictionary(filename):
    dictionary = {}
    if not os.path.exists(filename):
        open(filename, 'w').close()
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            parts = re.split(r'\s{2,}|\t|:', line.strip())
            if len(parts) >= 2:
                word = parts[0].lower()
                meaning = ' '.join(parts[1:]).strip()
                dictionary[word] = meaning
    return dictionary

# Save word to file
def save_word_to_file(word, meaning):
    with open(DICTIONARY_FILE, 'a', encoding='utf-8') as file:
        file.write(f"{word}\t\t{meaning}\n")

# Convert text to speech and return audio bytes (in-memory)
def text_to_speech_binary(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    mp3_fp = BytesIO()
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    return mp3_fp.read()

# Main app
def main():
    if st.session_state.get("exit_now", False):
        st.markdown(
            """
            <div style='display: flex; justify-content: center; align-items: center; height: 90vh;'>
                <h1 style='text-align: center; font-size: 3em;'>😊 Thanks for using the dictionary!</h1>
            </div>
            """, unsafe_allow_html=True
        )
        st.stop()

    st.image("dict_1_logo.png", width=600)
    st.markdown("---")

    if "show_menu" not in st.session_state:
        st.session_state.show_menu = False

    dictionary = load_dictionary(DICTIONARY_FILE)

    # Show dictionary list initially
    if not st.session_state.show_menu:
        st.markdown("#### Dictionary List:")

        if dictionary:
            sorted_items = sorted(dictionary.items())
            for word, meaning in sorted_items:
                st.markdown(f"🔹 **{word.capitalize()}** — {meaning}")
        else:
            st.info("No words in dictionary yet.")

        if st.button("Click continue"):
            st.session_state.show_menu = True
            st.rerun()

    else:
        st.markdown("## What would you like to do?")
        choice = st.radio(
            "Choose an option:",
            ("🔍 Search for a Word", "➕ Add a New Word")
        )

        if choice == "🔍 Search for a Word":
            search_word = st.text_input("Enter a word to search:")

            if st.button("Search"):
                st.session_state.search_clicked = True
                st.session_state.found_word = search_word.lower()

            if st.session_state.get("search_clicked", False):
                word = st.session_state.found_word
                if word.strip() == "":
                    st.warning("Please enter a word.")
                    st.session_state.search_clicked = False
                elif word in dictionary:
                    meaning = dictionary[word]
                    st.success(f"{word.capitalize()}:")
                    st.write(meaning)

                    if st.button("🔊 Pronounce Word"):
                        st.session_state.pronounce_word = word

                    if st.button("🔊 Pronounce Meaning"):
                        st.session_state.pronounce_meaning = meaning
                else:
                    st.error("Word not found in dictionary.")
                    st.session_state.search_clicked = False

            # Pronounce word (after rerun)
            if st.session_state.get("pronounce_word"):
                audio_bytes = text_to_speech_binary(st.session_state.pronounce_word)
                st.audio(audio_bytes, format='audio/mp3')
                st.session_state.pronounce_word = None

            # Pronounce meaning (after rerun)
            if st.session_state.get("pronounce_meaning"):
                audio_bytes = text_to_speech_binary(st.session_state.pronounce_meaning)
                st.audio(audio_bytes, format='audio/mp3')
                st.session_state.pronounce_meaning = None

        elif choice == "➕ Add a New Word":
            new_word = st.text_input("New Word:")
            new_meaning = st.text_area("Meaning:")

            if st.button("Add Word"):
                if new_word.strip() == "" or new_meaning.strip() == "":
                    st.warning("Both word and meaning are required.")
                elif new_word.lower() in dictionary:
                    st.warning("This word already exists in the dictionary.")
                else:
                    save_word_to_file(new_word.lower(), new_meaning.strip())
                    st.success(f"Word '{new_word}' added successfully! Please refresh.")

    st.markdown("---")

    # Exit button
    if st.button("❌ Exit Program"):
        st.session_state.exit_now = True
        st.rerun()

    st.markdown("**Made by Muhammad Shameer Asim**")

if __name__ == "__main__": #run using: python -m streamlit run voice_dictionary.py
    main()
