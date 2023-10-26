import json
import os
import pandas as pd
import streamlit as st
from dotenv import load_dotenv 
import openai
from langchain.text_splitter import CharacterTextSplitter
from base import prompt

#from base import OPENAI_API_KEY, prompt
from logic import extract_audio

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def translate_audio(audio_filepath, filename):
   file_path = f"transcript/{filename}.txt"  # Define the file path without the leading '/'

   if not os.path.exists(file_path):
      audio_file = open(audio_filepath, "rb")
      transcript = openai.Audio.transcribe("whisper-1", audio_file)
      st.write(transcript)

      # Open the file in write mode ("w") using os.path.join to create a valid path
      with open(file_path, "w") as file:
         # Write the string to the file
         file.write(transcript["text"])

      # Create a download link for the file
      st.markdown(f"Download the transcript: [Download {filename}.txt]({file_path})")

      return transcript["text"].replace(".", ".\n")
   else: 
      with open(file_path, "r") as trans:
         st.write("<h3>Memory</h3>", unsafe_allow_html=True)
         text = {"text": trans.read()}
         #st.write(text)
         st.markdown(f"Download the transcript: [Download {filename}.txt]({file_path})")
      return text["text"].replace(".", ".\n")



   
def text_split(text):
   text_splitter = CharacterTextSplitter(separator="\n", chunk_size =3000,
      chunk_overlap = 200, length_function = len)
   chunks = text_splitter.split_text(text)
   return chunks


def write_points(chunks):
    text_list = []
    for chunk in chunks:
        # Create a list of messages
        messages = [
            {"role": "user", "content": prompt(chunk)}
        ]

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=messages,
            max_tokens=1000,
            temperature=0.7,
            api_key=OPENAI_API_KEY
        )

        generated_text = response['choices'][0]['message']['content']
        ##st.write(generated_text)
        text_list.append(generated_text)
     
    st.write(text_list)
    return  text_list


def main():
    openai.api_key =  OPENAI_API_KEY
    st.set_page_config(page_title="YOUTUBE VIDEO REPURPOSER 1.0",page_icon="🎀",
                       initial_sidebar_state="auto",)
    st.header("YOUTUBE VIDEO REPURPOSER 1.0")
    st.text("Transcribe YouTube Video to Social media")   
    text = None
    with st.sidebar:
      status_progress = "Extracting Audio  Process...1/3"
      url_link= st.text_input("Enter Youtube URL")
    if url_link is None or url_link == "":
      st.chat_input("Chat with our Model", disabled=True)
    else:
      with st.spinner(status_progress):
       filename = extract_audio(url_link.strip(), "resources/")

      with st.spinner("Converting Audio Process...2/3"):
         if filename:
          text =   translate_audio(f"resources/{filename}",filename[:-4])
         
      with st.spinner("Chunking Text ...."):
         if text:
            splittext = text_split(text)
            ##st.write(splittext)

      with st.spinner("Writing Points .... 3/3"):
         st.write("## **Social Media Points**")
         write_points(splittext)
     
         

if __name__ == '__main__':
    main()
