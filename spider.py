import argparse
import os
import requests
from bs4 import BeautifulSoup

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
    try :
        print(f"Requesting web {args.URL}")
        reponse = requests.get(args.URL , timeout=10)
        reponse.raise_for_status()
    except requests.RequestException as e:
        print(f"Error in fetching request : {e}")

    print("fetching html file request")
    soup = BeautifulSoup(reponse.content,'html.parser')
    images_tags = soup.find_all('img')
    images_ext = ('.gif', '.jpeg', '.jpg', '.png', '.bmp')
    for im_tag in images_tags :
        src = im_tag.get(src)
        if not src :
            continue
        
        # if :
        #     src.lower(endswith(images_ext))
        print (f"image was found")


if __name__ == "__main__":
    main()
    print("Spider finished")