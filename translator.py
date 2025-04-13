from googletrans import Translator
from bs4 import BeautifulSoup
import requests
import asyncio
import nest_asyncio
nest_asyncio.apply()

def get_text_from_url(url):
    
    url = str(url)
    # Only process URLs from www.startupticker.ch
    if "www.startupticker.ch" not in url:
        #print(f"URL '{url}' is not from www.startupticker.ch. Skipping.")
        return ""
    
    translator = Translator()
    
    try:
        headers = {
            "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                           "AppleWebKit/537.36 (KHTML, like Gecko) "
                           "Chrome/90.0.4430.93 Safari/537.36")
        }
        response = requests.get(url, timeout=10, headers=headers)
        if response.status_code != 200:
            #print(f"Failed to retrieve {url}: HTTP {response.status_code}")
            return ""
        
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Extract text from specific containers
        intro_element = soup.find("div", class_="item-intro")
        description_element = soup.find("div", class_="item-description")
        
        intro_text = intro_element.get_text(separator=" ", strip=True) if intro_element else ""
        description_text = description_element.get_text(separator=" ", strip=True) if description_element else ""
        
        # Combine and clean the text
        full_text = (intro_text + " " + description_text).strip()
        if not full_text:
            #print("No text extracted from the target elements.")
            return ""
        
        # Detect language and translate only if needed
        try:
            detection = asyncio.run(translator.detect(full_text))
        except Exception as det_err:
            #print(f"Language detection failed: {det_err}")
            detection = None

        if detection and detection.lang != 'en':
            #print(f"Translating text from {detection.lang} to English...")
            try:
                translation = asyncio.run(translator.translate(full_text, dest='en'))
                full_text = translation.text
            except Exception as trans_err:
                print(f"Translation failed: {trans_err}")
        
        return full_text
    except Exception as e:
        print(f"An error occurred while processing {url}: {e}")
        return ""
