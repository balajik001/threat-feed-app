# Cyber Threat Intelligence Feed

A simple but powerful web application built with Python and Flask that scans public RSS feeds from top cybersecurity news sources for specific threat-related keywords. The results are displayed in a clean, easy-to-read web interface.

This project is an excellent demonstration of web scraping, web development with Flask, and data parsing skills for any aspiring cybersecurity professional.

---

## Features

-   **Real-time Scanning:** Fetches the latest articles from multiple trusted sources.
-   **Keyword-based Filtering:** Scans titles and summaries for keywords like "ransomware", "vulnerability", "CVE-", etc., to filter out noise.
-   **Time-Sensitive:** Only shows articles published within the last 24 hours to ensure relevance.
-   **Simple Web Interface:** Presents the findings in a clean, organized table.
-   **Stateless Design:** Runs on-demand without needing a database, making it lightweight and easy to deploy.

---

## How It Works

This application uses a combination of powerful Python libraries to achieve its goal:

-   **Flask:** A lightweight web framework used to create the web server and render the HTML pages.
-   **Feedparser:** A robust library for downloading and parsing RSS/Atom feeds.
-   **Dateutil:** A library for easily parsing and handling date/time information from various formats.

When a user clicks the "Run New Scan" button, the Flask application calls the scanner module, which iterates through the list of RSS feeds, checks each article against the time and keyword filters, and returns a list of relevant articles to be displayed on the page.

---

## Getting Started

Follow these instructions to get the application running on your local machine.

### Prerequisites

-   Python 3 installed on your system.
-   `pip` (Python's package installer), which typically comes with Python.

### Installation & Execution

1.  **Clone or Download the Repository**
    If you have Git, clone the repository. Otherwise, download the source code and place it in a folder named `threat-feed-app`.

2.  **Navigate to the Project Directory**
    Open your terminal or command prompt and change into the project folder:
    ```bash
    cd path/to/threat-feed-app
    ```

3.  **Install Required Libraries**
    Install all the necessary Python packages using the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Flask Application**
    Start the local development server with the following command:
    ```bash
    flask run
    ```
    You will see output in your terminal indicating that the server is running, including a line like:
    `* Running on http://127.0.0.1:5000`

5.  **View in Your Browser**
    Open your web browser and navigate to the address shown in the terminal:
    [http://127.0.0.1:5000](http://127.0.0.1:5000)

You should now see the web interface. Click the "Run New Scan" button to fetch the latest threat intelligence!

---
