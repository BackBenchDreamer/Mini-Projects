import requests as rq
from bs4 import BeautifulSoup
import os

# Get the current working directory
current_dir = os.getcwd()

# Request user input
url = input("Enter Link: ")

# Check if URL starts with "http" or "https"
if "https" in url or "http" in url:
    data = rq.get(url)
else:
    data = rq.get("https://" + url)

# Parse the HTML
soup = BeautifulSoup(data.text, "html.parser")

# Extract the first 10 links
links = []
for link in soup.find_all("a"):
    links.append(link.get("href"))

# Define the path where the file will be saved
file_path = os.path.join(current_dir, "myLinks.txt")

# Write the links to the file
with open(file_path, 'a') as saved:
    print(links[:10], file=saved)

print(f"Links saved in {file_path}")