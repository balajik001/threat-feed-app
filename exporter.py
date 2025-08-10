# In threat-feed-app/exporter.py
import pandas as pd
from io import BytesIO


def create_excel(articles):
    """Creates an Excel file in memory from a list of articles."""
    df = pd.DataFrame(articles)
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Threat Report')
    output.seek(0)
    return output


def create_text_file(articles, scan_info):
    """Creates a formatted text file in memory from a list of articles."""
    output = BytesIO()

    # Write header
    header = f"Cyber Threat Intelligence Report\n"
    header += f"Scan Type: {scan_info['type']}\n"
    header += f"Scan Time: {scan_info['time']}\n"
    header += "=" * 50 + "\n\n"
    output.write(header.encode('utf-8'))

    # Write articles
    if not articles:
        output.write("No relevant threats found in this scan.".encode('utf-8'))
    else:
        for article in articles:
            entry = f"Source: {article['source']}\n"
            entry += f"Title: {article['title']}\n"
            entry += f"Published: {article['published']}\n"
            entry += f"Link: {article['link']}\n"
            entry += "-" * 50 + "\n"
            output.write(entry.encode('utf-8'))

    output.seek(0)
    return output
