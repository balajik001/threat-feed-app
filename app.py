# In threat-feed-app/app.py
from flask import Flask, render_template, request
import scanner
import datetime

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Handles both displaying the page and running a scan.
    - On GET: Shows the initial page.
    - On POST: Runs a scan and shows the results.
    """
    articles = []
    scan_time = None

    if request.method == 'POST':
        # If the "Run New Scan" button was clicked, run the scan
        articles = scanner.run_scan()

        # Get the current time to display on the report
        scan_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Render the page. If it's a GET request, 'articles' will be empty.
    return render_template('index.html', articles=articles, scan_time=scan_time)


if __name__ == '__main__':
    app.run(debug=True)