# In threat-feed-app/app.py
from flask import Flask, render_template, request, redirect, url_for, send_file, g, flash
import scanner
import exporter
import datetime
import sqlite3
import os
from io import BytesIO

app = Flask(__name__)
app.secret_key = 'your_very_secret_key_change_me'
DATABASE = 'threat_history.db'


def get_db():
    """Opens a new database connection if there is none yet for the current application context."""
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE, detect_types=sqlite3.PARSE_DECLTYPES)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(e=None):
    """Closes the database again at the end of the request."""
    db = g.pop('db', None)
    if db is not None:
        db.close()


@app.route('/')
def index():
    """Renders the main welcome page."""
    return render_template('index.html')


@app.route('/scan', methods=['POST'])
def handle_scan():
    """Runs a scan, saves it to the DB, and redirects to the results page for that scan."""
    scan_type_str = 'Vendor' if 'vendor_scan' in request.form else 'Vulnerability'
    scan_type_code = 'vendor' if 'vendor_scan' in request.form else 'vulnerability'

    articles = scanner.run_scan(scan_type_code)
    scan_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    article_count = len(articles)

    db = get_db()
    cursor = db.cursor()
    cursor.execute('INSERT INTO scans (scan_type, scan_time, article_count) VALUES (?, ?, ?)',
                   (scan_type_str, scan_time, article_count))
    scan_id = cursor.lastrowid

    for article in articles:
        cursor.execute('INSERT INTO articles (scan_id, source, title, link, published) VALUES (?, ?, ?, ?, ?)',
                       (scan_id, article['source'], article['title'], article['link'], article['published']))
    db.commit()

    return redirect(url_for('results', scan_id=scan_id))


@app.route('/history')
def history():
    """Displays a page with the history of all past scans."""
    db = get_db()
    scans = db.execute('SELECT * FROM scans ORDER BY id DESC').fetchall()
    return render_template('history.html', scans=scans)


@app.route('/results/<int:scan_id>')
def results(scan_id):
    """Displays the results for a specific scan from the history."""
    db = get_db()
    scan_info = db.execute('SELECT * FROM scans WHERE id = ?', (scan_id,)).fetchone()
    if not scan_info:
        return "Scan not found.", 404

    articles = db.execute('SELECT * FROM articles WHERE scan_id = ? ORDER BY published DESC', (scan_id,)).fetchall()
    return render_template('results.html', articles=articles, scan_info=scan_info)


@app.route('/delete_database', methods=['POST'])
def delete_database():
    """Deletes the database file and re-initializes an empty one."""
    close_db()  # Ensure the connection is closed before deleting
    if os.path.exists(DATABASE):
        os.remove(DATABASE)
    database.init_db()  # Create a fresh, empty database
    flash("Scan history has been successfully deleted.")
    return redirect(url_for('index'))


@app.route('/download/<int:scan_id>/<file_format>')
def download_report(scan_id, file_format):
    db = get_db()
    scan_info = db.execute('SELECT * FROM scans WHERE id = ?', (scan_id,)).fetchone()
    articles = db.execute('SELECT * FROM articles WHERE scan_id = ?', (scan_id,)).fetchall()

    if not scan_info:
        return "Scan not found.", 404

    # Convert articles from sqlite3.Row to dict for the exporter
    articles_dict = [dict(article) for article in articles]
    scan_info_dict = dict(scan_info)

    filename_time = scan_info_dict['scan_time'].replace(':', '-').replace(' ', '_')
    filename = f"Threat_Report_{filename_time}.{file_format}"

    if file_format == 'xlsx':
        file_data = exporter.create_excel(articles_dict)
        mimetype = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        return send_file(file_data, as_attachment=True, download_name=filename, mimetype=mimetype)

    elif file_format == 'txt':
        file_data = exporter.create_text_file(articles_dict, scan_info_dict)
        return send_file(file_data, as_attachment=True, download_name=filename, mimetype='text/plain')

    return redirect(url_for('results', scan_id=scan_id))


if __name__ == '__main__':
    app.run(debug=True)