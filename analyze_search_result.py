from flask import Flask

from collections import Counter
import string
import re
import locale
# Analyze search result function


def analyze_search_result(listings, applied_filters, exact_url):
    # Get the keyword used for search from the query parameters
    if applied_filters:
        keyword = applied_filters['Keyword Used for Search']
    else:
        keyword = ""

    # keyword = keyword.lower() if keyword else ''
    # print(keyword)
    # # Count the occurrences of the keyword in each listing title
    # keyword_counts = Counter()
    # for listing in listings:
    #     title = listing['title'].lower()
    #     keyword_counts[keyword] += title.count(keyword)

    # Count the occurrences of other words in the whole listings
    word_counts = Counter()

    for listing in listings:
        title = listing['title'].lower()
        words = title.split()  # Split the title into individual words
        word_counts.update(words)

    # Filter the word_counts to include words that occur two or more times
    other_words = [word for word, count in word_counts.items() if count >= 0]

    other_word_counts_formatted = [
        {"Word": word, "Counter": word_counts[word]} for word in other_words
    ]

    other_word_counts_formatted.sort(key=lambda x: x['Counter'], reverse=True)

    # OLD CODE NOT USING ARRAY OF OBJECTS
    # Format the keyword_counts as "Keyword - Count"
    # keyword_counts_formatted = [
    #     f"{keyword}: {count}x" for keyword, count in keyword_counts.items()
    # ]

    # Format the other_word_counts as "Word - Count" and sort by count in descending order

    # other_word_counts_formatted = [
    #     f"{word}: {word_counts[word]}x" for word in other_words
    # ]

    # other_word_counts_formatted = sorted(other_word_counts_formatted, key=lambda x: float(x.split(':')[1].split(
    #     '/')[0]) / float(x.split(':')[1].split('/')[1]) if '/' in x.split(':')[1] else 0, reverse=True)

    # other_word_counts_formatted.sort(
    #     key=lambda x: int(x.split(': ')[1][:-1]), reverse=True)

    # other_word_counts_formatted.sort(key=lambda x: int( // issue when title is Vitanica Opti-Recovery, Pre & Post Surgery Support 60 VEGAN CAPS EXP:8/24
    #     x.split(':')[1][:-1] or 0), reverse=True)

    # Get the prices of the listings
    # Define the currency symbols to remove in price range necessary for all ebay sites
    ebay_site_mapping = {
        'www.ebay.com': 'en_US',  # eBay US with USD
        'www.ebay.co.uk': 'en_GB',   # eBay UK with GBP
        'www.ebay.au': 'en_AU',   # eBay Australia with AUD
        'www.ebay.ca': 'en_CA',   # eBay Canada with CAD
        'www.ebay.de': 'de_DE',   # eBay Germany with EUR
        'www.ebay.fr': 'fr_FR',   # eBay France with EUR
        'www.ebay.it': 'it_IT'    # eBay Italy with EUR
    }

    for site_url, site_code in ebay_site_mapping.items():
        if site_url in exact_url:
            currentSite = site_url
            locale.setlocale(locale.LC_ALL, site_code)
            break
    else:
        print('No matching URL for the locale')

    currency_symbols = "$£AUCEUR"
    translation_table = str.maketrans('', '', currency_symbols)
    # print(currentSite)
    prices = []
    for listing in listings:
        checker = listing['price'].translate(translation_table).replace(
            '.', '').replace(',', '').replace(' ', '').isdigit()
        if (checker):
            price = listing['price']

        if (currentSite == 'www.ebay.it' or currentSite == 'www.ebay.de'):
            price = price.replace('.', '').replace(',', '.')
        else:
            price = price.replace(',', '')
        if any(sep in price for sep in ['to', 'a', 'bis']):
            price_range = re.split(r'to|a|bis', price)
            min_price = float(price_range[0].translate(translation_table))
            max_price = float(price_range[1].translate(translation_table))
            prices.append(min_price)  # Add min_price to the prices list
            prices.append(max_price)  # Add max_price to the prices list
        else:
            price_value = float(price.translate(translation_table))
            # print(locale.atof(price_value))
            # Check currentSite to determine the eBay locale and apply the appropriate conversion
            prices.append(price_value)

    # Count the occurrence of each price
    prices_counter = Counter(prices)

    sorted_prices_counter = dict(
        sorted(prices_counter.items(), key=lambda x: x[1], reverse=True))

    sorted_prices_formatted = [
        {"Price": locale.currency(price), "Counter": count} for price, count in sorted_prices_counter.items()]

    # OLD CODE NOT USING ARRAY OF OBJECTS
    # # Sort the prices_counter by count in descending order
    # sorted_prices_counter = dict(
    #     sorted(prices_counter.items(), key=lambda x: x[1], reverse=True))

    # # Format the sorted_prices_counter as "Price - Count"
    # sorted_prices_formatted = [
    #     f"{locale.currency(price)}: {count}x" for price, count in sorted_prices_counter.items()
    # ]

    # Find the highest, average, middle, and lowest prices
    if prices:
        highest_price = max(prices)
        average_price = sum(prices) / len(prices)
        sorted_prices = sorted(prices)
        middle_price = sorted_prices[len(sorted_prices) // 2]
        lowest_price = min(prices)
    else:
        highest_price = None
        average_price = None
        middle_price = None
        lowest_price = None
    # Count the number of listings with free shipping
    # free_shipping_count = sum(listing['free_shipping'] for listing in listings)

    # Count the number of items listed by each store
    # store_counts = Counter(listing['store_name'] for listing in listings)

    return {
        'keyword': keyword,
        'other_word_counts': other_word_counts_formatted,
        'highest_price': locale.currency(highest_price) if highest_price is not None else 0,
        'average_price': locale.currency(average_price) if average_price is not None else 0,
        'middle_price': locale.currency(middle_price) if middle_price is not None else 0,
        'lowest_price': locale.currency(lowest_price) if lowest_price is not None else 0,
        'prices_counter': sorted_prices_formatted,
        # 'free_shipping_count': free_shipping_count,
        # 'store_counts': dict(store_counts)
    }
