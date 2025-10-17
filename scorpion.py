import argparse
import os
import requests
from PIL import Image

def analyze_image_metadata(filepath):
    print("-" * 30)
    print(f"analyzing : {filepath}")

    try:
        file_stat = os.stat(filepath)
        print(f"File Size: {file_stat.st_size / 1024:.2f} KB")
        print(f"Last Modified: {datetime.fromtimestamp(file_stat.st_mtime)}")
        print("\\n")
        image = Image.open(filepath)
        exif_data = image._getexif()
        if not exif_data:
            print("No EXIF metadata found")
            return
        print("EXIF metadata")
        for tag_id, value in exif_data.items():
             tag_name = TAGS.get(tag_id,tag_id)

        if isinstance(value,bytes):
             value = value.decode('utf-8',errors='ignore')
        print(f"{tag_name} : {value}")
    except Exception as e:
            print(f"An error occurred while processing" '{filepath}' : {e})
    except FileNotFoundError:
            print(f"Error : the file'{filepath}' was not found")
    
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