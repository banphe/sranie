import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi

def main():
    st.title("YouTube Transcript App")
    
    # Input field for YouTube video link
    video_link = st.text_input("Enter YouTube Video Link")
    
    # Button to retrieve transcript
    if st.button("Get Transcript"):
        # Retrieve and display the transcript
        transcript = get_transcript(video_link)
        st.write(transcript)

if __name__ == "__main__":
    main()

def get_transcript(video_link):
    video_id = extract_video_id(video_link)
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        text = ""
        for line in transcript:
            text += line['text'] + " "
        return text
    except:
        return "Transcript not available or error occurred."

def extract_video_id(video_link):
    # Extract the video ID from the YouTube link
    # This function may need to be adapted to handle different link formats
    video_id = video_link.split("v=")[-1]
    return video_id

#st.title('vsio w paradkie')
#st.write('This is a simple Streamlit app.')