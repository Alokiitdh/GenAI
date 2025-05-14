from transformers import pipeline
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document

# Load pretrained model
summarizer_model = pipeline("summarization", model="facebook/bart-large-cnn")

# Split text into chunks
def split_text(text: str):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )
    return splitter.split_documents([Document(page_content=text)])

# Summarize each chunk and join
def summarize_chunks(chunks):
    summaries = []
    for chunk in chunks:
        result = summarizer_model(chunk.page_content, max_length=150, min_length=40, do_sample=False)
        summaries.append(result[0]['summary_text'])
    return " ".join(summaries)
