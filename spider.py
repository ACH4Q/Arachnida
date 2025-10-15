import argparse
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def scrape_page(url, current_depth, args, visited_urls):
    if current_depth > args.level or url in visited_urls:
        return

    print(f"[{current_depth}] Scraping: {url}")
    visited_urls.add(url)

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp')
        img_tags = soup.find_all('img')
        for img_tag in img_tags:
            img_url = img_tag.get('src')
            if not img_url:
                continue

            if img_url.lower().endswith(image_extensions):
                full_img_url = urljoin(url, img_url)
                try:
                    img_response = requests.get(full_img_url, timeout=10)
                    img_response.raise_for_status()
                    filename = os.path.basename(full_img_url).split('?')[0]
                    filepath = os.path.join(args.path, filename)
                    with open(filepath, 'wb') as f:
                        f.write(img_response.content)
                    print(f"  -> Downloaded {filename}")
                except requests.RequestException as e:
                    print(f"  -> Failed to download image {full_img_url}: {e}")

        if args.recursive:
            base_netloc = urlparse(url).netloc
            link_tags = soup.find_all('a')
            for link_tag in link_tags:
                link_url = link_tag.get('href')
                if not link_url:
                    continue

                full_link_url = urljoin(url, link_url)
                if urlparse(full_link_url).netloc == base_netloc:
                    scrape_page(full_link_url, current_depth + 1, args, visited_urls)

    except requests.RequestException as e:
        print(f"  -> Could not process page {url}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Scrape images from a website.")
    parser.add_argument('URL', help='The URL of the website to scrape.')
    parser.add_argument('-r', '--recursive', action='store_true',
                        help='Recursively download images.')
    parser.add_argument('-l', '--level', type=int, default=5,
                        help='Maximum recursion depth (default: 5).')
    parser.add_argument('-p', '--path', default='./data/',
                        help='Path to save downloaded files (default: ./data/).')

    args = parser.parse_args()
    print(f"Starting scrape on {args.URL}")
    os.makedirs(args.path, exist_ok=True)

    visited_urls = set()
    scrape_page(args.URL, 0, args, visited_urls)

if __name__ == "__main__":
    main()
    print("Spider finished.")