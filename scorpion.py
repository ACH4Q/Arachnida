import argparse
import os
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS

def analyze_image_metadata(filepath):
    print("-" * 50)
    print(f"Analyzing: {filepath}")

    try:
        file_stat = os.stat(filepath)
        print(f"File Size: {file_stat.st_size / 1024:.2f} KB")
        print(f"Last Modified: {datetime.fromtimestamp(file_stat.st_mtime)}")
        print("\n")

        image = Image.open(filepath)
        exif_data = image._getexif()

        if not exif_data:
            print("No EXIF metadata found.")
            return

        print("EXIF Metadata:")
        for tag_id, value in exif_data.items():
            tag_name = TAGS.get(tag_id, tag_id)
            if isinstance(value, bytes):
                value = value.decode('utf-8', errors='ignore')
            print(f"  {tag_name}: {value}")

    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
    except Exception as e:
        print(f"An error occurred while processing '{filepath}': {e}")
    finally:
        print("-" * 50 + "\n")

def main():
    parser = argparse.ArgumentParser(
        description="Parsing the metadata of the picture"
    )
    parser.add_argument(
        'files',
        nargs='+',
        help="One or more image file paths to analyze."
    )
    args = parser.parse_args()

    for file in args.files:
        analyze_image_metadata(file)

if __name__ == "__main__":
    main()