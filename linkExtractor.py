import requests
from bs4 import BeautifulSoup
import pyfiglet


def get_urls():
    pyparser = pyfiglet.figlet_format("linkExtractor")
    print(pyparser)
    doc = pyfiglet.figlet_format(
        "Simple script that searches a given page and extracts a list of linked URLs. With each URL a list of keywords associated with this URL is returned.", font='term')
    print(doc)
    url = input("Enter the URL to extract: ")
    keywords = []
    url_list = []

    # make request
    if url.startswith('http'):
        r = requests.get(url)
    else:
        print("Please enter a valid URL:\nExample: https://website.com")
        return -1

    print(f'Status Code: {r.status_code}')

    # parse html content
    soup = BeautifulSoup(r.content, 'html.parser')
    for link in soup.find_all('a', href=True):
        link_url = link['href']
        link_text = link.get_text(strip=True)
        keywords_list = link_text.split()

        # add link and keyword to list
        if link_url.startswith('http'):
            url_list.append(link_url)
            keywords.append(keywords_list)

    print_urls = input("Do you want to view the generated URL list? (y/n) ")
    if print_urls == "y" or print_urls == "Y":
        print(f'URLs: {url_list}\n')

    print_keywords = input(
        "Do you want to view the generated Keywords? (y/n) ")
    if print_keywords == "y" or print_keywords == "Y":
        print(f'Keywords: {keywords}')

    return url_list, keywords


get_urls()
