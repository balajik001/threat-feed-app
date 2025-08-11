# Cyber Threat Intelligence Feed

A multi-page web application built with Python and Flask that scans public RSS feeds for cybersecurity threats. This version includes persistent scan history, separate results pages, and report exporting.

This project is an excellent demonstration of web development, data parsing, and database management skills for any aspiring cybersecurity professional.

---

## Features

-   **Dual Scan Modes:** Run a broad "Vulnerability Scan" or a targeted "Vendor Scan".
-   **Persistent History:** All scans are saved to a lightweight SQLite database, allowing you to review past results.
-   **Multi-Page Interface:** A clean user experience with separate pages for the homepage, scan history, and detailed results.
-   **Customizable Vendor List:** Easily edit a text file to control which vendors are monitored.
-   **Report Exporting:** Download scan results as a clean `.txt` file or a structured `.xlsx` Excel file.
-   **Database Management:** Includes a simple "Delete History" button to reset the application state.

---

## Installation Guide

Follow these steps carefully to get the application running on your local machine.

### Prerequisites

-   Python 3 installed on your system.
-   `pip` (Python's package installer).

### Step-by-Step Installation

1.  **Clone or Download the Repository**
    Place the project files in a folder named `threat-feed-app`.

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

4.  **Initialize the Database (Crucial First-Time Step)**
    This version of the app uses a lightweight SQLite database to store your scan history. You must create this file before running the app for the first time.
    ```bash
    python database.py
    ```
    > **Note:** You only need to run this command once during the initial setup. It will create a `threat_history.db` file in your project folder.

5.  **Run the Flask Application**
    Start the local development server with the following command:
    ```bash
    flask run
    ```
    You will see output indicating the server is running on `http://127.0.0.1:5000`.

---

## How to Use the Application

The application now has a more robust, multi-page workflow.

-   **Homepage:** This is the main landing page where you can start a new scan.
-   **Scan Buttons:** Choose either "Vulnerability News Scan" for general threats or "Vendor News Scan" for news related to specific companies.
-   **History Page:** Click "View Scan History" on the homepage to see a table of all your past scans, including the type, time, and number of articles found.
-   **Results Page:** From the history page, click "View Report" on any entry to see the detailed list of articles found in that specific scan.
-   **Download Reports:** On the results page, you can download the report as a clean Text file or a structured Excel file.
-   **Delete History:** On the history page, the "Delete All History" button will completely wipe the database and give you a fresh start.

---

## Customizing the Vendor List

You can easily edit the list of vendors that the "Vendor News Scan" looks for.

1.  Open the `vendors.txt` file in your project folder.
2.  Add, edit, or remove company names.
3.  Make sure there is one vendor name per line.
4.  Save the file. The changes will be used the next time you run a Vendor News Scan.
