import streamlit as st
from groq import Groq

# TEST: Hardcode API key first to see output

client = Groq(api_key=GROQ_API_KEY)

CRISIS_MESSAGE = """
⚠️ It sounds like you might be going through a difficult time.
If you are thinking about suicide or self-harm, please reach out to a crisis hotline immediately:

📞 Thailand: 1323 (Mental Health Hotline)
📞 Myanmar: 09-765-999-123 (Shwe Yaung Hnin Si Helpline)
📞 International List: https://findahelpline.com
"""

CRISIS_KEYWORDS = [
    "kill myself", "end my life", "suicide", "want to die",
    "can't go on", "self harm", "cut myself"
]

def contains_crisis_keywords(text):
    return any(kw in text.lower() for kw in CRISIS_KEYWORDS)

TEMPLATE = """
You are a compassionate and safe mental health assistant.

Rules:
1. Only answer questions related to mental health.
2. If the question is not related to mental health, reply:
   "I can only provide information about mental health topics."
3. If the user expresses suicidal thoughts or self-harm intent, do not give advice — only respond with the provided crisis hotline message.
4. Always answer in a supportive, clear, and non-judgmental tone.
5. Use the given context if available; otherwise, base your answer on safe, general mental health knowledge.

User question: {question}
"""

st.set_page_config(page_title="Mental Health Chatbot", page_icon="💬")
st.title("💬 Mental Health Chatbot")

user_question = st.text_input("Your question:")

if user_question:  # triggers on Enter or when text changes
    if contains_crisis_keywords(user_question):
        st.warning(CRISIS_MESSAGE)
    else:
        with st.spinner("Thinking..."):
            formatted_prompt = TEMPLATE.format(question=user_question)
            chat_completion = client.chat.completions.create(
                messages=[{"role": "user", "content": formatted_prompt}],
                model="llama-3.3-70b-versatile",
            )
        st.write(chat_completion.choices[0].message.content)
