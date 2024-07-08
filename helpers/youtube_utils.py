import streamlit as st
from youtube_transcript_api import (
    YouTubeTranscriptApi, YouTubeRequestFailed, VideoUnavailable, InvalidVideoId, TooManyRequests,
    TranscriptsDisabled, NoTranscriptAvailable, NotTranslatable, TranslationLanguageNotAvailable,
    CookiePathInvalid, CookiesInvalid, FailedToCreateConsentCookie, NoTranscriptFound
)
from pytube import extract

# Function to extract the video ID from a given YouTube URL
def extract_video_id_from_url(url):
    """
    Extracts the video ID from a YouTube URL.
    
    Parameters:
    - url (str): The URL of the YouTube video.
    
    Returns:
    - str: The extracted video ID.
    
    Raises:
    - Displays an error message if the URL is invalid.
    """
    try:
        return extract.video_id(url)  # Attempt to extract the video ID
    except Exception:
        st.error("Please provide a valid YouTube URL.")  # Display an error message if extraction fails
        example_urls = [  # Example URLs to help users understand valid formats
            'http://youtu.be/g78b08j0b0nygy',
            'http://www.youtube.com/embed/SA2iWivDJiE',
            'http://www.youtube.com/4380tg8h430hir',
            'https://www.youtube.com/watch?v=358hg580gh9fh05-t240'
        ]
        st.info("Here are some valid formats: " + " ,".join(example_urls))  # Provide examples to the user
        st.stop()  # Stop further execution

# Function to fetch the transcript text of a video using its video ID
def get_transcript_text(video_id):
    """
    Fetches the transcript text of a YouTube video using its video ID.
    
    Parameters:
    - video_id (str): The ID of the YouTube video.
    
    Returns:
    - str: The concatenated transcript text.
    
    Raises:
    - Displays an error message for various exceptions related to transcript fetching.
    """
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)  # Fetch the transcript
        return " ".join([item["text"] for item in transcript])  # Join the transcript text into a single string
    except YouTubeRequestFailed:
        st.error("YouTube Request Failed: An error occurred while fetching the transcript. Please try another video.")
        st.stop()
    except VideoUnavailable:
        st.error("Video Unavailable: The requested video is unavailable. Please try another video.")
        st.stop()
    except InvalidVideoId:
        st.error("Invalid Video ID: Please provide a valid YouTube video ID.")
        st.stop()
    except TooManyRequests:
        st.error("Too Many Requests: You have exceeded the rate limit for fetching transcripts. Please try again later.")
        st.stop()
    except NoTranscriptAvailable:
        st.error("No Transcript Available: The requested video does not have a transcript available.")
        st.stop()
    except NotTranslatable:
        st.error("Not Translatable: The transcript of the video cannot be translated into the requested language.")
        st.stop()
    except TranslationLanguageNotAvailable:
        st.error("Translation Language Not Available: The requested translation language is not available for the transcript.")
        st.stop()
    except CookiePathInvalid:
        st.error("Cookie Path Invalid: The provided cookie path is invalid.")
        st.stop()
    except CookiesInvalid:
        st.error("Cookies Invalid: The provided cookies are invalid or expired.")
        st.stop()
    except FailedToCreateConsentCookie:
        st.error("Failed To Create Consent Cookie: There was an issue with creating a consent cookie for the YouTube API.")
        st.stop()
    except TranscriptsDisabled:
        st.error("Transcripts Disabled: Subtitles are disabled for this video. Please try another video.")
        st.stop()
    except NoTranscriptFound:
        st.error("No Transcript Found: The video doesn't have English subtitles. Please ensure the video you're selecting is in English or has English subtitles available.")
        st.stop()
    except Exception as e:
        st.error(f"An unexpected error occurred: {str(e)}. Please try again.")  # Handle any other unexpected exceptions
        st.stop()
