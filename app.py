import streamlit as st
from groq import Groq

# Load your API key securely from Streamlit secrets
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

# Initialize Groq client once
client = Groq(api_key=GROQ_API_KEY)

st.title("Mental Health Assistant (Powered by Groq LLM)")

user_question = st.text_area("Ask a mental health related question:")

if st.button("Get Answer"):
    if not user_question.strip():
        st.warning("Please enter a question first.")
    else:
        # Prompt template with instructions
        template = """
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

        # Fill template with user question
        formatted_prompt = template.format(question=user_question)

        with st.spinner("Contacting Groq API..."):
            try:
                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "user",
                            "content": formatted_prompt,
                        }
                    ],
                    model="llama-3.3-70b-versatile",
                )
                answer = chat_completion.choices[0].message.content
                st.subheader("Answer:")
                st.write(answer)

            except Exception as e:
                st.error(f"API error: {e}")
