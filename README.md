# News Article Translation Tool

This tool automates the process of fetching news article links from a specified source and then translating the contents of those articles into English and Vietnamese. The process is divided into two main scripts: `GetLink.py` for fetching article links, and `main.py` for processing those links to extract and translate the article contents.

## Getting Started

These instructions will guide you through the setup process and execution of the tool.

### Prerequisites

Before running the scripts, ensure you have Python 3 installed on your system. You can download Python 3 from [here](https://www.python.org/downloads/).

### Installation

Install all the necessary Python packages listed in requirements.txt by running the following command:

```sh 
pip install -r requirements.txt 

### Usage

Step 1: Fetching Article Links

Run GetLink.py to scrape and save the links for each news page. This script outputs a file containing all the scraped links.

```sh 

python3 GetLink.py


Step 2: Translating Articles

Once you have obtained the list of links, run main.py to process these links and get the translation of articles. The script will output the translated articles, formatted as specified, into a designated directory.

```sh 

python3 main.py
