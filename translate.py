
import asyncio
from googletrans import Translator

async def translate_text(text):
    translator = Translator()
    
    translated = await translator.translate(text, src="en", dest="gu") 
    return translated.text 

if __name__ == "__main__":

    asyncio.run(translate_text())

