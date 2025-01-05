# kongbugushi.com_scraper
A python script to download novels from kongbugushi.com

因为鬼叔的超脑系列实在找不到txt，干脆写了个脚本自己把它爬下来

## Prerequisites

```
python 3.x
requests
beautifulsoup4
```

## Usage

Run the script from command line with the URL of the novel's table of contents page:

```bash
python kongbugushi_scraper.py "http://www.kongbugushi.com/your-novel-url"
```

The script will create a txt file named after the book title and download all chapters sequentially.

## Disclaimer
This script extracts and downloads information from kongbugushi.com which does not currently have ToS prohibiting this. Users are responsible for verifying the copyright status of content they download and complying with applicable laws in their jurisdiction.
