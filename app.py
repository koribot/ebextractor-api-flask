
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


# Parsing UR
@app.route('/api/extract', methods=['POST'])
def extract_data():
    try:
        htmlContent = request.json.get('htmlContent')
        url = request.json.get('url')
        print(htmlContent, url)
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
