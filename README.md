# Arachnida - Web Scraper & Metadata Analyzer

Arachnida is a cybersecurity project focused on the fundamentals of web scraping and file metadata analysis. It consists of two Python command-line tools: `spider`, a recursive image scraper, and `scorpion`, a metadata extractor. This project was developed to understand how data can be retrieved from the web and how seemingly hidden information can be extracted from files.

## Table of Contents

- [Project Description](#project-description)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Spider: The Image Scraper](#spider-the-image-scraper)
  - [Scorpion: The Metadata Analyzer](#scorpion-the-metadata-analyzer)
- [How It Works](#how-it-works)

## Project Description

This project is split into two distinct but related parts:

1.  **Spider (`spider.py`)**: A powerful command-line tool that crawls a given website and recursively downloads images. It is designed to be respectful of bandwidth and allows for fine-grained control over recursion depth and download location.

2.  **Scorpion (`scorpion.py`)**: A utility to analyze the downloaded files (or any other images). It extracts and displays valuable metadata, including EXIF data from photographs, which can reveal information such as camera model, date, time, and even GPS coordinates.

This project explicitly avoids external scraping libraries like `Scrapy` or `wget` to ensure the core logic of HTTP requests, HTML parsing, and recursion is built from the ground up.

## Features

### Spider
- **Recursive Scraping**: Can crawl a website by following links to discover and download more images.
- **Depth Control**: Allows users to specify the maximum recursion depth to prevent infinite loops and control the scope of the crawl.
- **Image Filtering**: Downloads only common image formats (`.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`).
- **Custom Save Location**: Users can specify a directory where all downloaded images will be saved.
- **Robust Error Handling**: Gracefully handles network errors, bad URLs, and HTTP error codes.

### Scorpion
- **Metadata Extraction**: Reads and displays basic file information (size, modification date).
- **EXIF Data Parsing**: Extracts and prints all available EXIF (Exchangeable Image File Format) data from JPEG images.
- **Human-Readable Output**: Converts numerical EXIF tag IDs into human-readable names (e.g., `271` -> `Make`).
- **Multi-File Support**: Can analyze multiple image files in a single command.

## Requirements

- Python 3.6+
- `pip` (Python package installer)

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/arachnida.git
    cd arachnida
    ```

2.  **Install the required Python libraries:**
    This project depends on `requests`, `BeautifulSoup4`, and `Pillow`. You can install them using the following command:
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: You will need to create a `requirements.txt` file with the following content:)*
    ```
    requests
    beautifulsoup4
    Pillow
    ```

## Usage

Both tools are run from the command line.

### Spider: The Image Scraper

The `spider.py` script downloads images from a given URL.

**Syntax:**
```bash
python spider.py [-r] [-l DEPTH] [-p PATH] URL
```

**Arguments:**
- `URL`: The full URL of the website you want to scrape.
- `-r`, `--recursive`: (Optional) Enable recursive downloading. The spider will follow links on the same domain.
- `-l DEPTH`, `--level DEPTH`: (Optional) Set the maximum recursion depth. Defaults to `5`.
- `-p PATH`, `--path PATH`: (Optional) Specify the directory to save images. Defaults to `./data/`.

**Examples:**

- **Download all images from a single page:**
  ```bash
  python spider.py http://books.toscrape.com
  ```

- **Recursively download images up to a depth of 2, saving them in a folder named `scraped_images`:**
  ```bash
  python spider.py -r -l 2 -p scraped_images/ http://books.toscrape.com
  ```

### Scorpion: The Metadata Analyzer

The `scorpion.py` script displays metadata for one or more image files.

**Syntax:**
```bash
python scorpion.py FILE [FILE ...]
```

**Arguments:**
- `FILE`: One or more paths to the image files you want to analyze.

**Example:**

- **Analyze a single image downloaded by the spider:**
  ```bash
  python scorpion.py data/cover.jpg
  ```

- **Analyze multiple images at once:**
  ```bash
  python scorpion.py data/image1.jpg data/image2.png
  ```

- **Analyze all `.jpg` files in a directory:**
  ```bash
  python scorpion.py data/*.jpg
  ```

## How It Works

- **Spider** uses the `requests` library to fetch the HTML content of a webpage. It then uses `BeautifulSoup` to parse the HTML, finding all `<img>` tags to identify image URLs and `<a>` tags for recursive crawling. It intelligently handles both relative and absolute URLs.

- **Scorpion** uses the `Pillow` (PIL Fork) library to open image files. It leverages `os.stat` to get file system metadata and `Pillow`'s built-in methods to extract the EXIF dictionary from images, which it then formats for clear presentation.
