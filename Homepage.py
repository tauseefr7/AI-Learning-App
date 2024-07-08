import streamlit as st

with st.sidebar:
    st.header("About the Author")
    st.write("""
    **Tauseef Rehman** is deeply passionate about technology and coding, constantly exploring the 
             latest advancements and refining his skills. His journey led him to create this innovative 
             tool, designed to transform the learning experience by making it more interactive, engaging, 
             and enjoyable. Through this tool, Tauseef aims to inspire others to embrace the wonders 
             of technology and discover the joy of continuous learning.

    Keep exploring and have fun!
    """)

    st.divider()
    st.subheader("🔗 Connect with Me", anchor=False)
    st.markdown(
        """
        [![LinkedIn "in" Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/LinkedIn_Logo_2013.svg/100px-LinkedIn_Logo_2013.svg.png)
](https://www.linkedin.com/in/rehmantauseef/)
\n 
or 
\n tauseefr84@gmail.com
"""
    )

st.title("Home Page")
st.write("""This application can summarise YouTube videos and automatically creates quizzes. Offering several benefits across various domains: 
\n             
             1. 🎓 Education
Enhanced Learning: Students can quickly understand key points from educational videos, making study sessions more efficient. 
             \n Assessment: Quizzes based on video content can help reinforce learning and provide immediate feedback.
             \n Accessibility: Summaries make content accessible to those with limited time or those who prefer reading over watching videos.
\n
             2. 🏢 Corporate Training
Time Efficiency: Employees can get the gist of training videos without spending hours watching them, increasing productivity.
\n Knowledge Checks: Quizzes can ensure that employees understand the training material, aiding in better retention and compliance.
\n Onboarding: New hires can quickly catch up with essential information through summaries and quizzes.
\n
             3. 🎥 Content Creators
Engagement: Creators can offer summaries and quizzes to their audience, increasing interaction and engagement.
\n Monetisation: Offering value-added services like quizzes and summaries can create additional revenue streams.
\n
             4. 📊 Research
Information Synthesis: Researchers can use summaries to quickly review vast amounts of video content, aiding in literature reviews and data collection.
\n Evaluation: Quizzes can be used to test understanding of research findings presented in video format.
\n
             5. 🌱 Personal Development
Skill Building: Learners can efficiently consume educational content and test their knowledge, aiding in skill acquisition.
\n Time Management: Summaries help individuals manage their time better by focusing on key points instead of consuming full-length videos.
\n
             6. ♿ Accessibility
Language Barriers: Non-native speakers can benefit from text summaries and quizzes to better understand video content.
\n Hearing Impaired: Summaries provide an alternative way to access information for those with hearing impairments.
\n             
             7. 📢 Marketing
Content Repurposing: Marketers can use summaries and quizzes to create multiple forms of content from a single video, enhancing their content strategy.
\n Lead Generation: Interactive quizzes can be used as lead magnets, collecting user data in exchange for quiz results.
\n             
             8. ⚙️ Productivity
Quick Reviews: Professionals can stay updated with industry trends by quickly reviewing summaries of relevant videos.
\n Skill Assessment: Quizzes can help identify knowledge gaps, enabling targeted learning.""")
