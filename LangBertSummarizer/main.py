from fastapi import FastAPI
from models import InputText
from Summrizer import split_text, summarize_chunks


app = FastAPI()

@app.post("/summarize")
def summarize(data: InputText):
    chunks = split_text(data.text)
    summary = summarize_chunks(chunks)
    return {"summary": summary}
