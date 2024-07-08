import streamlit as st
from helpers.toast_messages import get_random_toast
from helpers.youtube_utils import extract_video_id_from_url, get_transcript_text
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.chains import LLMChain

# Set the page configuration for the Streamlit app

st.set_page_config(
    page_title="Summariser",
    page_icon="📒",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Check if the user is new or returning using session state
# If the user is new, show a random toast message
if 'first_time' not in st.session_state:
    message, icon = get_random_toast()
    st.toast(message, icon=icon)
    st.session_state.first_time = False

# Main page UI setup
st.title("Summariser 📒", anchor=False)
st.write("""
Ever watched a YouTube video and wanted to summarise the content in text? If yes then paste it in the below:

**How does it work?** 🤔
1. Insert the YouTube video URL of your recently watched video.
2. Enter your [OpenAI API Key](https://platform.openai.com/account/api-keys).

⚠️ Important: The video **must** have captions in English for this to work.

""")

# Example video expander
with st.expander("💡 Example video"):
    with st.spinner("Loading video.."):
        st.video("https://www.youtube.com/watch?v=jNQXAC9IVRw&pp=ygUabW9zdCBwb3B1bGFyIHlvdXR1YmUgdmlkZW8%3D", format="video/mp4", start_time=0)

# User input form for YouTube URL and OpenAI API Key
with st.form("user_input"):
    YOUTUBE_URL = st.text_input("Enter the YouTube video link:", value="https://www.youtube.com/watch?v=jNQXAC9IVRw&pp=ygUabW9zdCBwb3B1bGFyIHlvdXR1YmUgdmlkZW8%3D")
    OPENAI_API_KEY = st.text_input("Enter your OpenAI API Key:", placeholder="sk-XXXX", type='password')
    submitted = st.form_submit_button("Summarise my YouTube video")

# Optional custom prompt for summarization
custom_prompt = st.text_area("Custom Prompt (recommended but optional)")

# Function to summarize the text using OpenAI API
def summarize_text(text, openai_api_key, custom_prompt=None):
    try:
        if custom_prompt:
            prompt = custom_prompt
        else:
            # Default prompt if custom prompt is not provided
            prompt = """
            You are an assistant designed to summarize text. Please provide a concise summary of the following text:

            {text}
            """

        # Prepare the prompt template for summarization
        system_message_prompt = SystemMessagePromptTemplate.from_template(prompt)
        human_message_prompt = HumanMessagePromptTemplate.from_template("{text}")
        chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
        
        # Initialize the language model chain for summarization
        chain = LLMChain(
            llm=ChatOpenAI(openai_api_key=openai_api_key),
            prompt=chat_prompt,
        )
        return chain.run(text)
    except Exception as e:
        if "AuthenticationError" in str(e):
            st.error("Incorrect API key. Please check it.")
            st.stop()
        else:
            st.error(f"An error occurred during summarization: {str(e)}")
            st.stop()

# Process the form submission
if submitted:
    if not YOUTUBE_URL:
        st.info("Please provide a valid YouTube video link. Head over to [YouTube](https://www.youtube.com/) to fetch one.")
        st.stop()
    elif not OPENAI_API_KEY:
        st.info("Please fill out the OpenAI API Key to proceed. If you don't have one, you can obtain it [here](https://platform.openai.com/account/api-keys).")
        st.stop()      
    
    # Extract video ID and fetch the transcript using the provided YouTube URL
    with st.spinner("Summarizing the video...🤓"):
        video_id = extract_video_id_from_url(YOUTUBE_URL) # Extract video ID from the YouTube URL
        video_transcription = get_transcript_text(video_id) # Get transcript text using the video ID
        summary = summarize_text(video_transcription, OPENAI_API_KEY) # Summarize the transcription
        st.success("Summary created successfully!")

        # Display summarized text
        st.subheader("Video Summary")
        st.write(summary)