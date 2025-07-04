# app.py

import streamlit as st
from backend.extract_text import extract_text_from_pdf
from backend.chunker import chunk_text
from backend.vector_store import store_chunks, retrieve_chunks
from backend.query_model import format_prompt, get_mistral_answer

st.set_page_config(page_title="Legal Document Analyzer", layout="wide")
st.title("⚖️ Legal Document Analyzer (RAG + ChromaDB + Mistral via Ollama)")

uploaded_file = st.file_uploader("Upload a legal PDF document", type=["pdf"])

if uploaded_file:
    # Extract and chunk text
    full_text = extract_text_from_pdf(uploaded_file)
    chunks = chunk_text(full_text)

    # Store and retrieve relevant chunks
    store_chunks(chunks)
    topics = ["Parties Involved", "Case Summary", "Verdict", "Relevant Acts"]

    st.subheader("📑 Auto Case Analysis")

    for topic in topics:
        relevant_chunks = retrieve_chunks(topic)
        prompt = format_prompt(relevant_chunks, topic)
        response = get_mistral_answer(prompt)
        st.markdown(f"**{topic}**")
        st.text_area(label=topic, value=response, height=200, key=topic)

    # Custom query
    st.subheader("💬 Ask a Custom Legal Question")
    query = st.text_input("Your legal question here:")
    if query:
        custom_chunks = retrieve_chunks(query)
        custom_prompt = format_prompt(custom_chunks, query)
        custom_response = get_mistral_answer(custom_prompt)
        st.text_area("Response", value=custom_response, height=200, key="custom_response")
