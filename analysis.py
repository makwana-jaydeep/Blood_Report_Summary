import requests
import streamlit as st

API_KEY = st.secrets["API_KEY"]

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
        "max_tokens": 500,
        "temperature": 0.7
    }

    response = requests.post(API_URL, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"].strip()
    else:
        return f"Error: API request failed with status {response.status_code} - {response.text}"

# Example usage (can be used in Streamlit app):
if __name__ == "__main__":
    result = analysis("Hemoglobin: 9.2 g/dL, WBC: 13,000 /µL, Platelets: 100,000 /µL")
    print(result)
