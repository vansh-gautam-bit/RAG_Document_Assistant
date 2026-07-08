import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="RAG Document Assistant",
    page_icon="🤖",
    layout="wide",
)

st.title("🤖 Multi Format RAG Assistant")

st.divider()

uploaded_file = st.file_uploader(
    "Upload a document",
    type=["pdf", "txt", "docx", "md"],
)

if uploaded_file:

    if st.button("Upload"):

        files = {
            "files": (
                uploaded_file.name,
                uploaded_file.getvalue(),
                uploaded_file.type,
            )
        }

        response = requests.post(
            f"{API_URL}/upload/",
            files=files,
        )

        if response.status_code == 200:
            st.success("Document uploaded successfully!")

        else:
            st.error(response.text)

st.divider()

question = st.text_input(
    "Ask a question"
)

if st.button("Ask"):

    response = requests.post(
        f"{API_URL}/chat/",
        json={
            "question": question
        },
    )

    if response.status_code == 200:

        answer = response.json()["answer"]

        st.subheader("Answer")

        st.write(answer)

    else:

        st.error(response.text)