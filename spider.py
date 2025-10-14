# spider.py
import argparse
import os
import requests

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


if __name__ == "__main__":
    main()
    print("Spider finished.")