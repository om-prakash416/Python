import requests
from bs4 import BeautifulSoup
import pandas as pd


def scrape_headlines(url):
    try:
       
        response = requests.get(url)
        response.raise_for_status()  

       
        soup = BeautifulSoup(response.text, "html.parser")

       
        headlines = soup.select("h3")  

      
        headlines_list = []
        for headline in headlines:
            text = headline.get_text(strip=True)
            if text:  
                headlines_list.append(text)

      
        df = pd.DataFrame(headlines_list, columns=["Headline"])
        df.to_csv("headlines.csv", index=False)
        print("Headlines saved to 'headlines.csv'.")
    except Exception as e:
        print(f"Error occurred: {e}")

# URL of website to scrape
news_url = "https://www.bbc.com/news"
scrape_headlines(news_url)
