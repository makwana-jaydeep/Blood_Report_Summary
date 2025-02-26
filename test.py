from googletrans import Translator

def translate_text(text):
    translator = Translator()
    translated = translator.translate(text, src="en", dest="gu")  # ❌ NO await
    return translated.text 

if __name__ == "__main__":
    result = translate_text("Hello, how are you?")
    print(result)
