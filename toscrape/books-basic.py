# Try gettin
import requests
from BeautifulSoup import BeautifulSoup

def main():
    r = requests.get("http://books.toscrape.com/")
    soup = BeautifulSoup(r.text)

    print soup

if __name__ == '__main__':
    main()