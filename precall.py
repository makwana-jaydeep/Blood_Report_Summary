import requests

def precall():
    TOGETHER_API_KEY = "838856825781a94df00e862c3e42d4d099e8f9387a70ba458fe8cf38bebad041"
    API_URL = "https://api.together.xyz/v1/completions"

    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }
    return headers
if __name__ == "__main__":
    precall()
