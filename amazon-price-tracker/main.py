import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",

}

url = "https://www.amazon.com/dp/B08L3SW8DZ/ref=sbl_dpx_kitchen-electric-cookware_B08GC6PL3D_0?th=1"
response = requests.get(url=url, headers=headers)

soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

price = soup.find(name="span", class_="a-price-whole").get_text()
price_without_currency = price.split("$")[0]
price_as_float = float(price_without_currency)
print(price_as_float)

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 200
EMAIL_ADDRESS = "pythonpqrst@yahoo.com"
PASSWORD = "pqrst1234()"

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
        connection.starttls()
        result = connection.login(EMAIL_ADDRESS, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL_ADDRESS,
            to_addrs=EMAIL_ADDRESS,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )
