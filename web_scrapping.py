import requests
from bs4 import BeautifulSoup
import assistantwiki
def search_and_display(spoken_text):
    user_query = spoken_text
    print(user_query)
    URL = "https://www.google.co.in/search?q=" + user_query

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
    }

    if user_query == "Could not understand audio":
        return user_query
    elif "how are you" in user_query:
        return user_query
    else:
        try:
            page = requests.get(URL, headers=headers)
            soup = BeautifulSoup(page.content, 'html.parser')
            result = soup.find('div', class_='Z0LcW').get_text()
            return result
        except Exception as e:
            return assistantwiki.wiki_search(spoken_text)
            
