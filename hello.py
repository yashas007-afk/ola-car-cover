import requests
from bs4 import BeautifulSoup
from time import sleep
import random

def scrape_olx_car_covers():
    alpha_url = "https://www.olx.in/items/q-car-cover"
    beta_headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/122.0.0.0 Safari/537.36"
        )
    }

    try:
        gamma_response = requests.get(alpha_url, headers=beta_headers)
        gamma_response.raise_for_status()
    except requests.RequestException as delta_error:
        print(f"Something went wrong: {delta_error}")
        return

    soup = BeautifulSoup(gamma_response.text, "html.parser")
    epsilon_items = soup.find_all("li")

    zeta_results = []

    for eta_item in epsilon_items:
        title_tag = eta_item.find("a")
        if title_tag and title_tag.text:
            title = title_tag.text.strip()
            link = "https://www.olx.in" + title_tag.get("href", "")
            price_tag = eta_item.find("span", class_="rui-3sH3b rui-NH3sL")
            price = price_tag.text.strip() if price_tag else "Price not listed"
            zeta_results.append(f"{title} | {price} | {link}")

    with open("car_cover_results.txt", "w", encoding="utf-8") as theta_file:
        for iota_line in zeta_results:
            theta_file.write(iota_line + "\n")

    print("✔ Car cover listings saved in 'car_cover_results.txt'")

if __name__ == "__main__":
    scrape_olx_car_covers()
