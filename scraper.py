import sys
import requests
from bs4 import BeautifulSoup

def scrape_cisco_jobs():
    url = "https://jobs.cisco.com/"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        job_listings = soup.find_all(class_='job-listing')
        for job in job_listings:
            title = job.find(class_='job-title').text.strip()
            location = job.find(class_='job-location').text.strip()
            print(f"Title: {title}\nLocation: {location}\n")
    else:
        print("Failed to retrieve Cisco jobs website.")

if __name__ == "__main__":
    scrape_cisco_jobs()
