import streamlit as st
from extractors.docx_parser import extract_text_from_docx
from extractors.pdf_parser import extract_text_from_pdf
from extractors.md_parser import extract_text_from_md
from generator.ai_test_generator_groq import generate_test_cases

st.title("🧪 PRD to Test Case Generator")

uploaded_file = st.file_uploader("📤 Upload your PRD file", type=["docx", "pdf", "md", "txt"])
api_key = st.text_input("🔑 OpenAI API Key", type="password")

if uploaded_file and api_key:
    file_type = uploaded_file.name.split(".")[-1].lower()

    if file_type == "docx":
        content = extract_text_from_docx(uploaded_file)
    elif file_type == "pdf":
        content = extract_text_from_pdf(uploaded_file)
    elif file_type == "md":
        content = extract_text_from_md(uploaded_file)
    elif file_type == "txt":
        content = uploaded_file.read().decode("utf-8")
    else:
        st.error("Unsupported file type.")
        st.stop()

    st.subheader("📄 Extracted PRD Content")
    st.text_area("Content", content[:3000], height=200)

    if st.button("🚀 Generate Test Cases"):
        with st.spinner("Generating..."):
            result = generate_test_cases(api_key, content)
            st.subheader("✅ Test Cases")
            st.text_area("Output", result, height=500)
