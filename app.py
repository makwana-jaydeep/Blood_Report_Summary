from translate import translate_text
from analysis import analysis
from text_extraction import text_extraction
import streamlit as st
import base64

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
            st.write(translate_text(clear_res)) 
        else:
            st.warning("Please upload a valid PDF file.") 
    except Exception as e:
        st.error(f"Error generating result: {str(e)}")


st.title("Blood Report Analyzer")
uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:
    with open("uploaded_report.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("PDF uploaded successfully!")

    # Create a button to view the uploaded PDF
    with open("uploaded_report.pdf", "rb") as pdf_file:
        base64_pdf = base64.b64encode(pdf_file.read()).decode("utf-8")
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="500"></iframe>'
    
    if st.button("Show Report PDF"):
        st.markdown(pdf_display, unsafe_allow_html=True)

    extracted_text = text_extraction(uploaded_file)
    display_result(extracted_text)
    
