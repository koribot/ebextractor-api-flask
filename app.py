
from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urlunparse, parse_qs
from flask_cors import CORS
import time
from analyze_search_result import analyze_search_result
from scrape_listings import scrape_listings
from filters import extract_categories, extract_filters
from notification import notification
import requests


app = Flask(__name__)
# CORS(app, resources={
#     r"/api/*": {"origins": "chrome-extension://eicdpgbknpihdhckcknjkkjignmcefpd"}
# })
CORS(app)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Referer": "https://www.google.com/",
    "DNT": "1",
    "Cache-Control": "max-age=0",
}


@app.route('/api/extract/using_keyword', methods=['GET'])
def extract_data_using_keyword_params():
    try:
        search_query = request.args.get('q')
        if not search_query:
            return jsonify({'error': 'You need to provide keyword'}), 400
        url = f"https://www.ebay.com/sch/i.html?_from=R40&_nkw={search_query}&_sacat=0&_ipg=240&_pgn=2"

        response = requests.get(url, headers=headers)
        if (response.status_code == 200):
            htmlContent = response.text
        soup_parse_content = BeautifulSoup(htmlContent, "html.parser")
        applied_filters = extract_filters(url)
        categories = extract_categories(soup_parse_content)
        listings = scrape_listings(soup_parse_content)
        notifications = notification()
        # print(listings)
        analysis_result = analyze_search_result(
            listings, applied_filters, url)

        # with open('soup.txt', 'w', encoding='utf-8') as file:
        #     file.write(str(soup_parse_content.prettify()))

        result = {
            'exact_url': url,
            'applied_filters': applied_filters,
            'categories': categories,
            'listings': listings,
            'analysis_result': analysis_result,
            'notifications': notifications
        }

        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Parsing UR
@app.route('/api/extract', methods=['POST'])
def extract_data():
    try:
        htmlContent = request.json.get('htmlContent')
        url = request.json.get('url')
        # print(htmlContent, url)
        if not htmlContent and url:
            return jsonify({'error': 'Combined data is missing'}), 400

        # Parse the URL to extract its components
        parsed_url = urlparse(url)
        scheme = parsed_url.scheme
        netloc = parsed_url.netloc
        path = parsed_url.path

        # Reconstruct the exact URL
        exact_url = urlunparse((scheme, netloc, path, '', '', ''))

        # Rest of your code...
        # Simulate some processing time (replace with your actual processing logic)
        # time.sleep(5)

        soup_parse_content = BeautifulSoup(htmlContent, "html.parser")
        applied_filters = extract_filters(url)
        categories = extract_categories(soup_parse_content)
        listings = scrape_listings(soup_parse_content)
        notifications = notification()
        # print(listings)
        analysis_result = analyze_search_result(
            listings, applied_filters, exact_url)

        # with open('soup.txt', 'w', encoding='utf-8') as file:
        #     file.write(str(soup_parse_content.prettify()))

        result = {
            'exact_url': url,
            'applied_filters': applied_filters,
            'categories': categories,
            'listings': listings,
            'analysis_result': analysis_result,
            'notifications': notifications
        }

        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run()
