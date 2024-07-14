# A Learning App: Turning YouTube Videos into Quizzes and Summaries with Streamlit

This app creates interactive quizzes from Youtube video captions (English only). By extracting captions using the [`youtube-transcript-api`](https://github.com/jdepoix/youtube-transcript-api) and subsequently processing the text with OpenAI's LLM (Model used: GPT-3.5-turbo-0125 (https://help.openai.com/en/articles/8555514-gpt-3-5-turbo-updates)). There is also the capabilitiy to summarise Youtube videos into text using custom prompts.

Benefits of summaries and quizzes across domains:

In education, they enhance learning efficiency and accessibility for students. In corporate training, they save time and ensure comprehension among employees, aiding in onboarding. For content creators, they boost engagement and offer monetisation opportunities. In research, they facilitate information synthesis and evaluation of findings. In personal development, they aid skill acquisition and time management. They also improve accessibility for non-native speakers and the hearing impaired. Additionally, in marketing they enable content repurposing and serve as effective lead generation tools.

## How It Works

1. **Caption Extraction:** Using the [`youtube-transcript-api`](https://github.com/jdepoix/youtube-transcript-api), captions are extracted from a given YouTube video URL.
2. **Quiz Generation:** The extracted captions are then fed into OpenAI's LLM using [`LangChain Python`](https://python.langchain.com/) with a predefined prompt template. The model generates questions based on the content, turning the video's key points into an interactive quiz.
3. **Summary:** The extracted captions are then fed into OpenAI's LLM similar (as with the quiz generation) but used to create a text summary. With custom prompts as an option.
4. **Streamlit Integration:** The quizzes are integrated and displayed in a Streamlit app, providing users with an interactive experience.

[![Application demo](https://github.com/user-attachments/assets/831cdaeb-4347-4c5a-aaa0-f92c3c2e77dd)]

## 🤝 Connect with Me
- 💼 **LinkedIn:** [Tauseef Rehman](https://www.linkedin.com/in/rehmantauseef/)

## Feedback & Collaboration
For feedback, suggestions, or potential collaboration opportunities, reach out at tauseefr84@gmail.com.
