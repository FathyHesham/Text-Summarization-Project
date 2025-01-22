import os
import time
import streamlit as st
from model.summarizer_model import TextSummarization  
from model.generated_summaries import GenerateSummary  
from model.preprocessing import preprocessing_text
from model.load_chunk_document import chunk_document, load_documents
from custom_logging.custom_logger import Customlogger

# Initialize logger
logger = Customlogger.create_custom_logger("StreamlitApp")

# Streamlit App
def run_streamlit_app():
    st.title("Text Summarization App")
    st.write("Upload a document (PDF format) to generate a summary.")

    # User input for topic and word limit
    topic = st.text_input("Enter the topic for the summary:", placeholder="Enter your topic here")
    limited_word = st.number_input("Enter the word limit for the summary:", min_value=1, step=1, value=100)

    # Upload file
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None and topic.strip():
        try:
            # Save uploaded file temporarily
            file_path = f"temp_{uploaded_file.name}"
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            logger.info(f"Uploaded file saved as {file_path}.")

            # Load and process the document
            st.info("Loading and processing the document...")
            document = load_documents(file_path = file_path)
            cleaned_text = preprocessing_text(document = document)
            chunks = chunk_document(document = cleaned_text)
            st.success(f"Document processed into {len(chunks)} chunks.")

            # Summarization process
            st.info("Summarizing the document...")
            model = TextSummarization(documents = chunks)
            model.load_models()
            model_summary = model.build_summarize_model(document = chunks)
            summarize = model.summarize_document(chunks = model_summary)

            # Generate final summary
            st.info("Generating the final summary...")
            summary = GenerateSummary(documents = summarize)
            final_summary = summary.interact(topic = topic, word_limit = limited_word)

            # Display summary character-by-character
            st.subheader("Generated Summary:")
            for char in generate_summary(final_summary):
                st.write(char, end="")
                time.sleep(0.05)

        except Exception as e:
            logger.error(f"An error occurred: {e}")
            st.error(f"An error occurred: {e}")
        finally:
            # Clean up the temporary file
            if os.path.exists(file_path):
                os.remove(file_path)
                logger.info(f"Temporary file {file_path} removed.")
    else:
        if not topic.strip():
            st.warning("Please enter a valid topic.")

def generate_summary(text):
    """Generates a summary character by character."""
    if not text:
        yield "No summary generated."
        return
    for char in text:
        yield char