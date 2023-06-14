import streamlit as st

from youtube_transcript_api import YouTubeTranscriptApi

def extract_video_id(video_link):
    if "youtube.com" in video_link:
        v_id = video_link.split("v=")[-1]
    elif "youtu.be" in video_link:
        v_id = video_link.split("/")[-1]
    else:
        return None
    return v_id

def get_transcript(v_link):
    video_id = extract_video_id(v_link)
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
       # text = ""
      #  for line in transcript:
       #      text += line['text'] + " "
      #  return text
        return transcript
    except:
        return "Transcript not available or error occurred."
    
def main():
    st.title("YouTube Transcript App")
    video_link = st.text_input("Enter YouTube Video Link")
    if st.button("Get Transcript"):
        transcript = get_transcript(video_link)

        if isinstance(transcript, str):  # if transcript is a string (error message), print it as it is
            st.write(transcript)
        else:  # if transcript is a list of dictionaries, print each segment separately
            for segment in transcript:
                st.write(f"Start time: {segment['start']}")
                st.write(f"Duration: {segment['duration']}")
                st.write(f"Text: {segment['text']}")
                st.write("---")  # separator between segments

 
     #   st.write(transcript)
if __name__ == "__main__":
    main()
