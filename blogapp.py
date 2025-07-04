# -*- coding: utf-8 -*-
"""blog _app.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pUWUGAJ-hC08Gkw_pvxWRfcJbhuRz2Tb
"""

import streamlit as st
from llama_cpp import Llama

# Path to your GGUF model — must be in a local folder named "models"
model_path = "/content/drive/My Drive/models/llama-2-7b-chat.Q3_K_S.gguf"


# Load the model once when app starts
@st.cache_resource
def load_model():
    return Llama(model_path=model_path ,n_ctx=2048)

llm = load_model()

# Function to generate a blog post
def generate_blog(topic, length, audience):
    prompt = f"""
    You are a professional blog writer.
    Write a {audience.lower()} blog article based on the following topic:
    "{topic}"
    The blog should be approximately {length} words long.
    """
    response = llm(prompt, max_tokens=512, temperature=0.7)
    return response['choices'][0]['text']

# Streamlit UI
st.set_page_config(page_title="Generate Blogs", layout='centered')
st.title("📝 AI Blog Generator")

st.markdown("Generate custom blog posts using the LLaMA 2 model.")

# Input fields
topic = st.text_input("Enter the blog topic")
col1, col2 = st.columns(2)

with col1:
    word_count = st.text_input("Approximate number of words", "300")

with col2:
    audience = st.selectbox("Writing the blog for", ["Researchers", "Data Scientist", "Common People"])

# Button to generate
if st.button("Generate"):
    if topic.strip() == "":
        st.warning("Please enter a blog topic.")
    else:
        with st.spinner("Generating..."):
            output = generate_blog(topic, word_count, audience)
            st.subheader("✍️ Blog Output")
            st.write(output)