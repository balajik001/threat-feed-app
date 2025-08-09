# In threat-feed-app/scanner.py
import feedparser
import datetime
import re
from dateutil import parser as date_parser

RSS_FEEDS = {
    'The Hacker News': 'https://feeds.feedburner.com/TheHackersNews',
    'Bleeping Computer': 'https://www.bleepingcomputer.com/feed/',
    'CISA Alerts': 'https://www.cisa.gov/news.xml',
    'Dark Reading': 'https://www.darkreading.com/rss.xml',
    'Krebs on Security': 'https://krebsonsecurity.com/feed/',
}

THREAT_KEYWORDS = [
    "zero-day", "ransomware", "vulnerability", "CVE-",
    "exploit", "data breach", "malware", "APT", "phishing",
    "remote code execution", "RCE", "critical flaw"
]


def published_within_last_24_hours(published_str):
    """Checks if an article was published within the last 24 hours."""
    try:
        published_time = date_parser.parse(published_str)
        if published_time.tzinfo is None:
            published_time = published_time.replace(tzinfo=datetime.timezone.utc)
        time_diff = datetime.datetime.now(datetime.timezone.utc) - published_time
        return time_diff.total_seconds() <= 86400
    except Exception:
        return False


def run_scan():
    """Scans RSS feeds and returns a list of found articles."""
    print("Starting threat scan...")
    found_articles = []
    unique_links = set()

    for source, url in RSS_FEEDS.items():
        feed = feedparser.parse(url)
        for entry in feed.entries:
            if entry.link in unique_links:
                continue

            published = entry.get('published', '') or entry.get('updated', '')
            if published and published_within_last_24_hours(published):
                content = f"{entry.get('title', '')} {entry.get('summary', '')}".lower()
                if any(re.search(rf"\b{kw}\b", content) for kw in THREAT_KEYWORDS):
                    found_articles.append({
                        'source': source,
                        'title': entry.title,
                        'link': entry.link,
                        'published': published.split(' +')[0]  # Clean up date string
                    })
                    unique_links.add(entry.link)

    print(f"Scan complete. Found {len(found_articles)} relevant articles.")
    return found_articles