import requests
import re
import streamlit as st

API_KEY = "tgp_v1_1i1l3At74wm-MMdUo2enqC8JyxC_U_45uzRHznVOQZU" 

def analysis(report):
    API_URL = "https://api.together.xyz/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = f"""
    I have a blood test report with the following values: {report}. 
    Give me this format analysis of this report:
    - Concerns: (max 3 lines)
    - Suggestions: (max 3 lines about diet/lifestyle)
    - Emergency: just write "Needed" or "Not Needed"
    """

    data = {
        "model": "deepseek-ai/DeepSeek-R1",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 1000,
        "temperature": 0.7
    }

    response = requests.post(API_URL, headers=headers, json=data)

    if response.status_code == 200:
        content = response.json()["choices"][0]["message"]["content"]
        clean_text = re.sub(r"<think>.*?</think>", "", content, flags=re.DOTALL).strip()
        return clean_text
    else:
        return f"Error: API request failed with status {response.status_code} - {response.text}"

if __name__ == "__main__":
    result = analysis("Hemoglobin: 9.2 g/dL, WBC: 13,000 /µL, Platelets: 100,000 /µL")
    print(result)
