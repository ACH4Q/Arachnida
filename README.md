# Arachnida - Web Scraper & Metadata Analyzer

Arachnida is a cybersecurity project focused on web scraping and metadata analysis, implemented entirely in Bash scripting. It consists of two main tools: `spider`, a web crawler that downloads images from a website, and `scorpion`, a tool to extract and display metadata from those images.

This project was completed following the constraints of the "Cybersecurity Piscine," which prohibits the use of high-level scraping libraries like `wget` or `Scrapy` to ensure a fundamental understanding of the underlying processes.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Spider: The Image Scraper](#spider-the-image-scraper)
  - [Scorpion: The Metadata Analyzer](#scorpion-the-metadata-analyzer)
- [Project Structure](#project-structure)

## Features

### `spider.sh`
*   **Recursive Scraping**: Downloads images from a target URL and can recursively crawl linked pages.
*   **Depth Control**: Allows specifying the maximum recursion depth to prevent infinite loops and control the scope of the crawl.
*   **Custom Save Location**: Users can define a specific directory to save downloaded images.
*   **Supported Image Types**: Downloads images with `.jpg`, `.jpeg`, `.png`, `.gif`, and `.bmp` extensions.

### `scorpion.sh`
*   **Metadata Extraction**: Parses and displays EXIF and other metadata from image files.
*   **Batch Processing**: Can analyze multiple image files in a single command.
*   **Clear Output**: Presents metadata in a human-readable format for each file.

## Prerequisites

Before running the scripts, you need to ensure you have the following command-line tools installed. Most are standard on modern Linux and macOS systems.

*   `bash`: The shell to run the scripts.
*   `curl`: Used for making HTTP requests to download web pages and images.
*   `grep`, `sed`, `awk`: Standard text-processing utilities used for parsing HTML content.
*   `exiftool`: The primary dependency for `scorpion.sh`. It is a powerful tool for reading and writing image metadata.

**Installing `exiftool`:**

*   **On Debian/Ubuntu:**
    ```sh
    sudo apt-get update && sudo apt-get install libimage-exiftool-perl
    ```
*   **On Fedora/CentOS:**
    ```sh
    sudo dnf install perl-Image-ExifTool
    ```
*   **On macOS (using Homebrew):**
    ```sh
    brew install exiftool
    ```

## Installation

1.  **Clone the repository:**
    ```sh
    git clone <your-repository-url>
    cd arachnida
    ```

2.  **Make the scripts executable:**
    This step grants the necessary permissions to run the scripts from your terminal.
    ```sh
    chmod +x spider.sh scorpion.sh
    ```

## Usage

### Spider: The Image Scraper

The `spider.sh` script downloads images from a given URL.

**Syntax:**
```sh
./spider.sh [-r] [-l DEPTH] [-p PATH] URL
```

**Options:**
*   `-r`: Enable recursive downloading. The script will follow links on the page and download images from them.
*   `-l [DEPTH]`: (Requires `-r`) Set the maximum recursion depth. Defaults to `5`.
*   `-p [PATH]`: Specify the directory where images will be saved. Defaults to `./data/`.
*   `URL`: The full URL of the website you want to scrape.

**Examples:**

1.  **Download all images from a single page:**
    ```sh
    ./spider.sh https://example.com
    ```
    *(Images will be saved in the `./data/` directory.)*

2.  **Recursively download images up to a depth of 2:**
    ```sh
    ./spider.sh -r -l 2 https://example.com
    ```

3.  **Recursively download images and save them to a custom folder:**
    ```sh
    ./spider.sh -r -p ./my-scraped-images https://example.com
    ```

### Scorpion: The Metadata Analyzer

The `scorpion.sh` script analyzes the downloaded images and displays their metadata.

**Syntax:**
```sh
./scorpion.sh [FILE1] [FILE2] ...
```

**Example:**

1.  **Analyze all `.jpg` files in the default `data` directory:**
    ```sh
    ./scorpion.sh data/*.jpg
    ```

2.  **Analyze specific images:**
    ```sh
    ./scorpion.sh data/image1.png data/photo.jpeg
    ```

## Project Structure

```
.
├── spider.sh         # The web scraping script
├── scorpion.sh       # The metadata analysis script
├── data/             # Default directory for downloaded images
└── README.md         # This file
