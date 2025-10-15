import argparse
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def main():
    parser = argparse.ArgumentParser(description="Scrape images from a website")
    parser.add_argument('URL', help='The URL of the website to scrape')
    parser.add_argument('-r', '--recursive', action='store_true',
                        help='Recursively download images')
    parser.add_argument('-l', '--level', type=int, default=5,
                        help='Maximum recursion depth (default: 5)')
    parser.add_argument('-p', '--path', default='./data/',
                        help='Path to save downloaded files (default: ./data/)')

    args = parser.parse_args()
    print(f"Starting scrape on {args.URL}")
    os.makedirs(args.path, exist_ok=True)

    try:
        print(f"Requesting web {args.URL}")
        response = requests.get(args.URL, timeout=10)
        response.raise_for_status()

        print("Parsing HTML to find image links...")
        soup = BeautifulSoup(response.text, 'html.parser')
        img_tags = soup.find_all('img')

        image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp')

        for img_tag in img_tags:
            img_url = img_tag.get('src')
            if not img_url:
                continue

            if img_url.lower().endswith(image_extensions):
                print(f"  [+] Found image: {img_url}")
                full_img_url = urljoin(args.URL, img_url)
                try:
                    img_response = requests.get(full_img_url, timeout=10)
                    img_response.raise_for_status()
                    filename = os.path.basename(full_img_url)
                    filepath = os.path.join(args.path, filename)
                    with open(filepath, 'wb') as f:
                        f.write(img_response.content)
                    print(f"      -> Saved to {filepath}")
                except requests.RequestException as e:
                    print(f"      -> Failed to download image: {e}")

    except requests.RequestException as e:
        print(f"Error in fetching request: {e}")

if __name__ == "__main__":
    main()
    print("Spider finished")