import streamlit as st
from dotenv import load_dotenv
load_dotenv() 
import sys
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
genai.configure(api_key='AIzaSyCz2KRx9F_tEGVXmlEf6MIHDZTmVUcfIY4')


prompt="""You are youtube video summerizer. you will be taking the transcript 
text and summerize the entire video and providing the important summary in points :"""

def extract_transcript_details(ulr_video):
    try:
        video_id=ulr_video.split('=')[1]
        print(video_id)
        transcript_text=YouTubeTranscriptApi.get_transcript(video_id)

        transcript='' 
        for i in transcript_text:
            transcript += " "+ i['text']
        
        return transcript
    
    except Exception as e:
        raise e

def generate_gemini_content(transcript_text,subject):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content(prompt + transcript_text)
    return response.text



st.title('Youtube Transcript to detailed notes cnverter')

youtube_link=st.text_input('enter youtube link: ')

if youtube_link:
    video_id=youtube_link.split('=')[1]
    print(video_id)

    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

if st.button('get Detailed Notes'):
    transcript_text=extract_transcript_details(youtube_link)

    if transcript_text:
        summary=generate_gemini_content(transcript_text,prompt)
        st.markdown("## Detailed Notes:")
        st.write(summary)

