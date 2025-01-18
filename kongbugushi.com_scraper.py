import requests
from bs4 import BeautifulSoup
import time
import argparse


def scrape_content(url):
    try:
        time.sleep(1)
        
        response = requests.get(url)
        response.encoding = response.apparent_encoding
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        content_div = soup.find('div', id='content')
        if not content_div:
            return None
        
        content_list = content_div.find_all('p')
        content_text = '\n  '.join(p.get_text().strip() for p in content_list)
        
        return content_text
        
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def main(base_url):
    try:
        response = requests.get(base_url)
        response.encoding = response.apparent_encoding
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        booklist = soup.find('ul', id='booklist')
        if not booklist:
            print("booklist element not found")
            return

        book_title = soup.find('div', {"class": "panel-heading"}).find('h1').text.split("在线阅读")[0]
        
        with open(f'{book_title}.txt', 'w', encoding='utf-8') as f:
            for li in booklist.find_all('li'):
                chapter = li.find('a')
                if not chapter:
                    continue
                
                title = chapter.get('title')
                href = chapter.get('href')

                if title and href:
                    href = href.split('/')[-1]
                    if base_url[-1] == '/':
                        href = f'{base_url}{href}'
                    else:
                        href = f'{base_url}/{href}'
                
                    titleNew = "".join(title.strip().split("_"))
                    print(f"Scraping: {titleNew}")
                    f.write(f"{titleNew}\n\n")
                    
                    content = scrape_content(href)
                    if content:
                        f.write(content + '\n\n')
                    else:
                        #f.write("Error: Could not fetch content for this page\n\n")
                        print("Error: Could not fetch content for this page, stopping")
                        return
                        
    except requests.RequestException as e:
        print(f"Error fetching main page: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="The url to the table of content page of the novel to be downloaded")
    args = parser.parse_args()
    base_url = args.url
    if base_url.startswith('http://'):
        main(args.url)
    elif base_url.startswith('https://'):
        print('kongbugushi.com does not support https, use http instead')
    else:
        print('url must begins with http://www.kongbugushi.com')