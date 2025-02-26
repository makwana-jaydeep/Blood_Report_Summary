from translate import translate_text
import asyncio
from analysis import analysis
from text_extraction import text_extraction
import streamlit as st

def process_pdf(file):
    try:
        text = text_extraction(file)  
        return text
    
    except Exception as e:
        st.error(f"Error processing the file: {str(e)}")  
        return None

def display_result(text):
    try:
        if text:
            
            response = analysis(text)  
            clear_res = response
            st.write(clear_res) 
            st.write(asyncio.run(translate_text(clear_res))) 
        else:
            st.warning("Please upload a valid PDF file.") 
    except Exception as e:
        st.error(f"Error generating result: {str(e)}")


st.title("Blood Report Analyzer")
uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:
    extracted_text = text_extraction(uploaded_file)
    display_result(extracted_text)
