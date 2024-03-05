# Real Estate Data Aggregator

## Overview
"Real Estate Data Aggregator" is a Python application designed to streamline the process of gathering and analyzing real estate data from Zigbang, a leading real estate listing platform in Seoul, South Korea. This project combines web scraping, JSON data handling, and integration with Google Sheets to provide a comprehensive overview of the real estate market.

## Key Features
- **Dynamic Web Scraping**: Automated extraction of real estate listings from Zigbang using Selenium WebDriver.
- **User-Driven Searches**: Allows users to specify search criteria, including location, type of place, and keyword.
- **JSON Data Serialization**: Converts scraped data into JSON format for ease of manipulation and storage.
- **Google Sheets Integration**: Utilizes the Google Sheets API for organizing and analyzing data in a user-friendly format.
- **Responsive Design**: Incorporates Bootstrap for a mobile-responsive user interface.

## Technical Stack
- **Back End**: Python, Flask, SQLAlchemy
- **Front End**: HTML5, CSS3 (Bootstrap), JavaScript
- **APIs**: Google Maps JavaScript API, Google Geocoding API
- **Database**: SQLite
- **Tools & Libraries**: gspread, oauth2client, Selenium WebDriver

## Getting Started
To set up the project locally:

1. Clone the repository:
    ```sh
    git clone https://github.com/Kimchimantium/Zigbang-Aggregator
    ```
2. Navigate to the project directory:
    ```sh
    cd real-estate-data-aggregator
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
- Ensure you have a valid Google API key and service account credentials for Google Sheets API.
- Run the application:
    ```python
    python main.py
    ```
- Follow the console prompts to input your search criteria and view results.

## Development Insights
This project provided insights into integrating various technologies to solve real-world problems. Key learnings include:
- Handling dynamic web content with Selenium WebDriver.
- Securely managing API keys and OAuth credentials.
- Processing and organizing large datasets with Python.

## Conclusion
"Real Estate Data Aggregator" exemplifies how automation and data processing can significantly enhance real estate market analysis. It showcases the practical application of programming skills to gather, organize, and present data in a meaningful way.
