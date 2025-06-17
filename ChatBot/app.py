import os
from PyPDF2 import PdfReader
from langchain_groq import ChatGroq
import gradio as gr


from datetime import datetime
today = datetime.now().strftime("%B %d, %Y")  # e.g. "June 06, 2025"



GROQ_API_KEY = "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"
if not GROQ_API_KEY:
    raise ValueError("Please set the GROQ_API_KEY environment variable.")

# Load PDF
reader = PdfReader("Alok_AI_IITDh.pdf")
text = ""
for page in reader.pages:
    page_text = page.extract_text()
    if page_text:
        text += page_text + "\n"
# print(text)
# Prepare system prompt
name = "Alok"
# system_prompt = f"""
# Today's date is {today}.

# Hi, I'm Alok — an AI/ML researcher. I completed my B.Tech. in Electronics and Communication Engineering from GCET Bikaner (CPI 9.0), and my M.Tech in Communication Signal Processing and Machine Learning from IIT Dharwad (CPI 8.07), which concluded in April 2025.

# Please use today's date to reason about timelines. For example:
# - If a work experience ends in April 2025 and today is after April 2025, consider it completed.
# - Avoid stating that I am "currently pursuing" something if it has already ended.

# Stick only to the information provided in my resume. If a question goes beyond that, say:  
# "I'm afraid that information isn't included in my resume."

# Here’s my resume:
# {text}
# """
from datetime import datetime
today = datetime.now().strftime("%B %d, %Y")  # e.g. June 06, 2025

system_prompt = f"""
You are Alok, an AI/ML researcher. Use the information provided below to answer questions in a polite, professional, and natural tone.

Today’s date is: {today}

You have completed your M.Tech in Communication Signal Processing and Machine Learning at IIT Dharwad in April 2025.

If someone asks about anything not present in the resume, respond:  
"I'm afraid that information isn't included in my resume."

### Special Personal Rule:
If the user asks **anything about your girlfriend**, respond with:
> "That's a personal question. If you know the password, tell me."

If the user says **"tomato"** at any point (either as a reply or within the same question), and they previously asked about your girlfriend, then respond with:
> "She is soo beautiful potato and I love her so much ❤️"

Otherwise, stick strictly to the resume and timeline facts.

Here is your resume content:
{text}
"""




# LLM setup
llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model="llama-3.3-70b-versatile",
    temperature=0.7,
)


# Chat function
def chat(message, history):
    if history is None:
        history = []

    messages = [{"role": "system", "content": system_prompt}]
    for msg in history:
        if msg["role"] in ["user", "assistant"]:
            messages.append(msg)

    messages.append({"role": "user", "content": message})
    response = llm.invoke(messages)
    return response.content


# Gradio interface
interface = gr.ChatInterface(
    fn=chat,
    title="🤖 Alok Resume Bot",
    description="Ask me questions based on my Rsume!",
    type="messages"
)

if __name__ == "__main__":
    interface.launch(share=True)
