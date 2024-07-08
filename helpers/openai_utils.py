import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.chains import LLMChain

def get_quiz_data(text, openai_api_key):
    # Define the prompt template that the AI will use to generate questions and answers
    template = f"""
    You are an assistant designed to create questions based on any given text. For each text segment you receive, your task is to generate 5 unique questions. Each question should be paired with 4 possible answers: one correct answer and three incorrect answers.

    To ensure clarity and ease of processing, format your response to resemble a Python list of lists.

    Your response should be structured as follows:

    1. An outer list containing 5 inner lists.
    2. Each inner list should represent a question and its answers, containing exactly 5 strings in this order:
       - The generated question.
       - The correct answer.
       - The first incorrect answer.
       - The second incorrect answer.
       - The third incorrect answer.

    Your response should look like this:
    [
        ["Generated Question 1", "Correct Answer 1", "Incorrect Answer 1.1", "Incorrect Answer 1.2", "Incorrect Answer 1.3"],
        ["Generated Question 2", "Correct Answer 2", "Incorrect Answer 2.1", "Incorrect Answer 2.2", "Incorrect Answer 2.3"],
        ...
    ]

    It is essential to follow this format as it is optimized for subsequent Python processing.
    """
    
    try:
        # Create the system message prompt using the template
        system_message_prompt = SystemMessagePromptTemplate.from_template(template)
        # Create the human message prompt that includes the input text
        human_message_prompt = HumanMessagePromptTemplate.from_template("{text}")
        # Combine both system and human messages into a chat prompt template
        chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
        
        # Initialize the language model chain with the OpenAI API key and the chat prompt
        chain = LLMChain(
            llm=ChatOpenAI(openai_api_key=openai_api_key),
            prompt=chat_prompt,
        )
        # Run the chain with the provided text and return the result
        return chain.run(text)
        
    except Exception as e:
        # Handle API key authentication errors
        if "AuthenticationError" in str(e):
            st.error("Incorrect API key. Please check it.")
            st.stop()
        else:
            # Handle other types of errors
            st.error(f"An error occurred: {str(e)}")
            st.stop()
