import requests
from bs4 import BeautifulSoup
import re

WEBHOOK_URL = "https://discord.com/api/webhooks/1419716880675110984/Fj7mxvrIFXBxkZS8lLpC6ApSYF_ORwjMS_8_gVTC6JDidhAezO9LeXbWAIzrunepJSbh"
# List of Amazon book links
urls = [
    "https://www.amazon.in/gp/product/1974717623?ref_=dbs_m_mng_rwt_calw_tpbk_24&storeType=ebooks&qid=1758290977&sr=8-1",
    "https://www.amazon.in/gp/product/1974722880?ref_=dbs_m_mng_rwt_calw_tpbk_27&storeType=ebooks&qid=1758290977&sr=8-1",
    "https://www.amazon.in/gp/product/1974725103?ref_=dbs_m_mng_rwt_calw_tpbk_28&storeType=ebooks&qid=1758290977&sr=8-1",
    "https://www.amazon.in/gp/product/1974727157?ref_=dbs_m_mng_rwt_calw_tpbk_29&storeType=ebooks&qid=1758290977&sr=8-1",
    "https://www.amazon.in/gp/product/1974732363?ref_=dbs_m_mng_rwt_calw_tpbk_31&storeType=ebooks&qid=1758290977&sr=8-1",
    "https://www.amazon.in/gp/product/1974734749?ref_=dbs_m_mng_rwt_calw_tpbk_32&storeType=ebooks&qid=1758290977&sr=8-1",
    "https://www.amazon.in/gp/product/1974739090?ref_=dbs_m_mng_rwt_calw_tpbk_34&storeType=ebooks&qid=1758290977&sr=8-1",
    "https://www.amazon.in/gp/product/1974741087?ref_=dbs_m_mng_rwt_calw_tpbk_35&storeType=ebooks&qid=1758290977&sr=8-1",
    "https://www.amazon.in/gp/product/1974745848?ref_=dbs_m_mng_rwt_calw_tpbk_37&storeType=ebooks&qid=1758290977&sr=8-1",
    "https://www.amazon.in/gp/product/1974749649?ref_=dbs_m_mng_rwt_calw_tpbk_38&storeType=ebooks&qid=1758290977&sr=8-1",
    "https://www.amazon.in/gp/product/1974752739?ref_=dbs_m_mng_rwt_calw_tpbk_39&storeType=ebooks&qid=1758290977&sr=8-1",
    "https://www.amazon.in/gp/product/1974755886?ref_=dbs_m_mng_rwt_calw_tpbk_40&storeType=ebooks&qid=1758290977&sr=8-1",
    "https://www.amazon.in/gp/product/197470159X?ref_=dbs_m_mng_rwt_calw_tpbk_0&storeType=ebooks&qid=1758290888&sr=8-1",
    "https://www.amazon.in/gp/product/1974701859?ref_=dbs_m_mng_rwt_calw_tpbk_1&storeType=ebooks&qid=1758290888&sr=8-1",
    "https://www.amazon.in/gp/product/197470257X?ref_=dbs_m_mng_rwt_calw_tpbk_2&storeType=ebooks&qid=1758290888&sr=8-1",
    "https://www.amazon.in/gp/product/197470436X?ref_=dbs_m_mng_rwt_calw_tpbk_3&storeType=ebooks&qid=1758290888&sr=8-1",
    "https://www.amazon.in/gp/product/1974707725?ref_=dbs_m_mng_rwt_calw_tpbk_4&storeType=ebooks&qid=1758290888&sr=8-1",
    "https://www.amazon.in/gp/product/197471053X?ref_=dbs_m_mng_rwt_calw_tpbk_5&storeType=ebooks&qid=1758290888&sr=8-1",
    "https://www.amazon.in/gp/product/1974710661?ref_=dbs_m_mng_rwt_calw_tpbk_6&storeType=ebooks&qid=1758290888&sr=8-1",
    "https://www.amazon.in/gp/product/1974719790?ref_=dbs_m_mng_rwt_calw_tpbk_8&storeType=ebooks&qid=1758290888&sr=8-1",
    "https://www.amazon.in/gp/product/1974722937?ref_=dbs_m_mng_rwt_calw_tpbk_9&storeType=ebooks&qid=1758290888&sr=8-1",
    "https://www.amazon.in/gp/product/1974725162?ref_=dbs_m_mng_rwt_calw_tpbk_10&storeType=ebooks&qid=1758290888&sr=8-1",
    "https://www.amazon.in/gp/product/1974727165?ref_=dbs_m_mng_rwt_calw_tpbk_11&storeType=ebooks&qid=1758290888&sr=8-1",
    "https://www.amazon.in/gp/product/1974732371?ref_=dbs_m_mng_rwt_calw_tpbk_12&storeType=ebooks&qid=1758290888&sr=8-1",
    "https://www.amazon.in/gp/product/1974736652?ref_=dbs_m_mng_rwt_calw_tpbk_13&storeType=ebooks&qid=1758290888&sr=8-1",
    "https://www.amazon.in/gp/product/1974740641?ref_=dbs_m_mng_rwt_calw_tpbk_14&storeType=ebooks&qid=1758290888&sr=8-1",
    "https://www.amazon.in/gp/product/1974704866?ref_=dbs_m_mng_rwt_calw_tpbk_0&storeType=ebooks&qid=1758290901&sr=8-1",
    "https://www.amazon.in/gp/product/1421582716?ref_=dbs_m_mng_rwt_calw_tpbk_1&storeType=ebooks&qid=1758290901&sr=8-1",
    "https://www.amazon.in/gp/product/1974703770?ref_=dbs_m_mng_rwt_calw_tpbk_2&storeType=ebooks&qid=1758290901&sr=8-1",
    "https://www.amazon.in/gp/product/1974713318?ref_=dbs_m_mng_rwt_calw_tpbk_3&storeType=ebooks&qid=1758290901&sr=8-1",
    "https://www.amazon.in/gp/product/1974724077?ref_=dbs_m_mng_rwt_calw_tpbk_4&storeType=ebooks&qid=1758290901&sr=8-1",
    "https://www.amazon.in/gp/product/1974734250?ref_=dbs_m_mng_rwt_calw_tpbk_5&storeType=ebooks&qid=1758290901&sr=8-1",
    "https://www.amazon.in/gp/product/1974721558?ref_=dbs_m_mng_rwt_calw_tpbk_0&storeType=ebooks&qid=1758556702&sr=8-1",
    "https://www.amazon.in/gp/product/1974727173?ref_=dbs_m_mng_rwt_calw_tpbk_1&storeType=ebooks&qid=1758556702&sr=8-1",
    "https://www.amazon.in/gp/product/1974734757?ref_=dbs_m_mng_rwt_calw_tpbk_2&storeType=ebooks&qid=1758556702&sr=8-1",
    "https://www.amazon.in/gp/product/1974741273?ref_=dbs_m_mng_rwt_calw_tpbk_3&storeType=ebooks&qid=1758556702&sr=8-1",
    "https://www.amazon.in/gp/product/1974745635?ref_=dbs_m_mng_rwt_calw_tpbk_4&storeType=ebooks&qid=1758556702&sr=8-1",
    "https://www.amazon.in/gp/product/197475278X?ref_=dbs_m_mng_rwt_calw_tpbk_5&storeType=ebooks&qid=1758556702&sr=8-1",
    # Add more links here
]

# Headers to mimic a browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
}


def fetch_book_details(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    # Book title
    title_element = soup.select_one("#productTitle")
    title = title_element.get_text(strip=True) if title_element else "Not found"

    # Book price
    price = None
    numeric_price = None
    price_element = soup.select_one(".a-price")
    if price_element:
        symbol = price_element.select_one(".a-price-symbol")
        whole = price_element.select_one(".a-price-whole")
        fraction = price_element.select_one(".a-price-fraction")
        if symbol and whole:
            price = symbol.get_text(strip=True) + whole.get_text(strip=True)
            if fraction:
                price += "." + fraction.get_text(strip=True)

            # Safe conversion to float
            try:
                numeric_price = float(whole.get_text(strip=True).replace(",", ""))
                if fraction:
                    numeric_price += float(fraction.get_text(strip=True)) / (
                        10 ** len(fraction.get_text(strip=True))
                    )
            except:
                numeric_price = None

    if not price:
        price = "Not found"

    return title, price, numeric_price


def post_to_discord(title, price, url):
    data = {"content": f"**{title}**\nPrice: {price}\nLink: {url}"}
    response = requests.post(WEBHOOK_URL, json=data)
    if response.status_code == 204:
        print(f"Posted to Discord: {title}")
    else:
        print(f"Failed to post: {title}, Status Code: {response.status_code}")


cheap_books = []

for url in urls:
    title, price, numeric_price = fetch_book_details(url)

    if numeric_price is not None and numeric_price <= 350:
        cheap_books.append(f"{title} - {price}\n{url}")

    post_to_discord(title, price, url)

if cheap_books:
    cheap_message = "**@here Books priced ₹350 or below:**\n" + "\n\n".join(cheap_books)
    requests.post(WEBHOOK_URL, json={"content": cheap_message})
