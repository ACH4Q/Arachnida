import argparse
import os
import requests
from PIL import Image

def analyze_image_metadata(filepath):
    print("-" * 30)
    print(f"analyzing : {filepath}") 
    
def main():
    parser = argparse.ArgumentParser(
        description="Parssing the metadata of the picture"
    )
    parser.add_argument(
        'files',
        nargs='+',
        help="One or more image file paths to analyze."
    )
    args = parser.parse_args()

    for file in args.files:
            print(f"Proccessing {file}")
            analyze_image_metadata(file)


if (__name__ == "__main__"):
    main()