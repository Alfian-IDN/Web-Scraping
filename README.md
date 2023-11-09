# Movie Transcripts Scraper

This Python script is designed to scrape movie transcripts from 'https://subslikescript.com' and save them as text files. 
It navigates through multiple pages of the movie listings on the site, accesses individual movie transcript pages, and saves each transcript in a dedicated folder.

## How It Works

The script uses the `requests` library to make HTTP requests and `BeautifulSoup` from `bs4` to parse HTML content. 
It is designed to iterate over a range of pages, extract the movie transcript links, and then scrape the transcripts themselves.

### Features

- Navigate through multiple pages of movie listings.
- Scrape individual movie transcripts.
- Clean file titles to remove characters that are not valid in file names.
- Save transcripts to a specified directory.

### Prerequisites

- Python 3
- `bs4` (BeautifulSoup)
- `requests`
- `os`
- `re` (Regular Expressions)

### Usage

To use the script, follow these steps:

1. Clone this repository or download the script.
2. Ensure you have the required libraries installed. You can install them using `pip`:

   ```sh
   pip install beautifulsoup4 requests

### Code Explanation
1. scrape_and_save_transcript(url, folder_path): This function scrapes the transcript from the given url and saves it to folder_path(multiple-pages).
2. main(): This is the main driver function. It goes through the pages on the site, collects all the transcript links, and calls scrape_and_save_transcript for each link.
3. File name cleaning: The script uses a regular expression to remove any characters from the title that are not valid in file names.
Text extraction: The transcript text is extracted with all the whitespace condensed and saved into a .txt file with the movie's title as the file name.

