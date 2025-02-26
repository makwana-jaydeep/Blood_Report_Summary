import requests
import re
import streamlit as st

API_KEY = st.secrets["API_KEY"]
def analysis(report):
    
    TOGETHER_API_KEY = API_KEY
    API_URL = "https://api.together.xyz/v1/completions"

    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }



    prompt = f"""
    I have a blood test report with the following values: {report}. 
    give me this format analysis of this report ,
    Concerns : for report ( 3 lines max),
    Suggestions : according to you diet and all ( 3 lines max)
    Emergency: doctor visit needed or not (just yes needed or not needed)
    """   
    data = {
        "model": "deepseek-ai/DeepSeek-R1",
        "prompt": prompt,
        "max_tokens": 1000
    }

    response = requests.post(API_URL, json=data, headers=headers)
    if response.status_code == 200:
        raw_text = response.json()["choices"][0]["text"]  
        clean_text = re.sub(r".*?</think>\s*", "", raw_text, flags=re.DOTALL)  
        return clean_text.strip()
    else:
        return "Error: API request failed."

if __name__ == "__main__":
    analysis("how are you")