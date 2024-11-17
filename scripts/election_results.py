import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_ballotpedia_results():
    url = "https://ballotpedia.org/Presidential_election,_2024"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    data = []

    # Example: Extract all tables (adjust parsing based on page structure)
    tables = soup.find_all("table")
    for table in tables:
        for row in table.find_all("tr"):
            cells = [cell.text.strip() for cell in row.find_all(["td", "th"])]
            data.append(cells)

    # Convert to DataFrame and save
    df = pd.DataFrame(data)
    df.to_csv("data/election_results_raw.csv", index=False)
    print("Election results saved to 'data/election_results_raw.csv'.")

if __name__ == "__main__":
    scrape_ballotpedia_results()