import streamlit as st
from helpers.youtube_utils import extract_video_id_from_url, get_transcript_text
from helpers.openai_utils import get_quiz_data
from helpers.quiz_utils import string_to_list, get_randomized_options
from helpers.toast_messages import get_random_toast

# Check if user is new or returning using session state
# If user is new, show the toast message
if 'first_time' not in st.session_state:
    message, icon = get_random_toast()
    st.toast(message, icon=icon)
    st.session_state.first_time = False

# Main page UI setup
st.title("Test yourself 📒", anchor=False)
st.write("""
Ever watched a YouTube video and wondered how well you understood its content? Instead of just watching on YouTube, come to **Quizly** and test yourself!

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
    submitted = st.form_submit_button("Create my quiz!")

# Check if the user input is submitted or quiz data is already in session state
if submitted or ('quiz_data_list' in st.session_state):
    # Validate inputs
    if not YOUTUBE_URL:
        st.info("Please provide a valid YouTube video link. Head over to [YouTube](https://www.youtube.com/) to fetch one.")
        st.stop()
    elif not OPENAI_API_KEY:
        st.info("Please fill out the OpenAI API Key to proceed. If you don't have one, you can obtain it [here](https://platform.openai.com/account/api-keys).")
        st.stop()      
    with st.spinner("Creating your quiz...🤓"): # Show spinner while processing
        if submitted:
            # Extract video ID and fetch the transcript
            video_id = extract_video_id_from_url(YOUTUBE_URL) # function defined in youtube_utils.py
            video_transcription = get_transcript_text(video_id) # function defined in youtube_utils.py
            # Get quiz data from OpenAI
            quiz_data_str = get_quiz_data(video_transcription, OPENAI_API_KEY) # function defined in openai_utils.py
             # Convert quiz data string to list
            st.session_state.quiz_data_list = string_to_list(quiz_data_str) # function defined in quiz_utils.py

            # Initialize session state for user answers, correct answers, and randomized options
            if 'user_answers' not in st.session_state:
                st.session_state.user_answers = [None for _ in st.session_state.quiz_data_list]
            if 'correct_answers' not in st.session_state:
                st.session_state.correct_answers = []    
            if 'randomized_options' not in st.session_state:
                st.session_state.randomized_options = []

            # Process each quiz question to get randomized options and correct answers
            for q in st.session_state.quiz_data_list:
                options, correct_answer = get_randomized_options(q[1:])
                st.session_state.randomized_options.append(options)
                st.session_state.correct_answers.append(correct_answer)

        # Quiz form for displaying questions and capturing user responses
        with st.form(key='quiz_form'): # for each question in the quiz data 
            st.subheader("🧠 Quiz Time: Test Your Knowledge!", anchor=False)
            for i, q in enumerate(st.session_state.quiz_data_list):
                options = st.session_state.randomized_options[i] # get the randomized options from session state
                default_index = st.session_state.user_answers[i] if st.session_state.user_answers[i] is not None else 0 # get the default index from session state
                response = st.radio(q[0], options, index=default_index) # get the user's answer from session state
                user_choice_index = options.index(response) # get the index of the user's answer
                st.session_state.user_answers[i] = user_choice_index  # Update the stored answer

            results_submitted = st.form_submit_button(label='Unveil My Score!') # submit button

            if results_submitted: 
                score = sum([ua == st.session_state.randomized_options[i].index(ca) for i, (ua, ca) in enumerate(zip(st.session_state.user_answers, st.session_state.correct_answers))]) # Calculate the score for each user answer and store it in session state
                st.success(f"Your score: {score}/{len(st.session_state.quiz_data_list)}") # Display the score for each user answer and store it in session state

                if score == len(st.session_state.quiz_data_list):  # Check if all answers are correct
                    st.balloons() # Display balloons if all answers are correct
                else:
                    incorrect_count = len(st.session_state.quiz_data_list) - score # Calculate the number of incorrect answers
                    if incorrect_count == 1: # If the number of incorrect answers is 1
                        st.warning(f"Almost perfect! You got 1 question wrong. Let's review it:") # Display warning if the number of incorrect answers is 1  
                    else:
                        st.warning(f"Almost there! You got {incorrect_count} questions wrong. Let's review them:") # Display warning if the number of incorrect answers is more than 1

 # Show detailed review of each question
                for i, (ua, ca, q, ro) in enumerate(zip(st.session_state.user_answers, st.session_state.correct_answers, st.session_state.quiz_data_list, st.session_state.randomized_options)):
                    with st.expander(f"Question {i + 1}", expanded=False): # Expand the question
                        if ro[ua] != ca: # Check if the user's answer is correct
                            st.info(f"Question: {q[0]}")
                            st.error(f"Your answer: {ro[ua]}")
                            st.success(f"Correct answer: {ca}")