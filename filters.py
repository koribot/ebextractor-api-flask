from urllib.parse import urlparse, urlunparse, parse_qs


# Mapping dictionary for readable filters
filter_mapping = {
    '_nkw': 'Keyword Used for Search',
    # '_odkw': 'Original Keyword',
    'LH_Complete': 'Completed Listings',
    'LH_Sold': 'Sold Listings',
    'LH_BIN': 'Listing Format',
    'LH_ItemCondition': 'Condition',
    'LH_Price': 'Price',
    'LH_Auction': 'Auction',
    # Add more filters here
}

# Mapping dictionary for specific filter values
filter_value_mapping = {
    'LH_Complete': {
        '1': 'Yes'
    },
    'LH_BIN': {
        '1': 'Buy it Now',
    },
    'LH_Sold': {
        '1': 'Yes',
    }
    # Add more filter values here
}


# Extracting filters used on the search result
def extract_filters(url):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)

    applied_filters = {}
    for param, values in query_params.items():
        if param in filter_mapping:
            filter_name = filter_mapping[param]
            filter_value = values[0]
            if filter_value in filter_value_mapping.get(param, {}):
                applied_filters[filter_name] = filter_value_mapping[param][filter_value]
            else:
                applied_filters[filter_name] = filter_value
    return applied_filters

# Extracting Categories


def extract_categories(soup):
    category_elements = soup.find_all(
        "li", class_="srp-refine__category__item")
    categories = []
    if category_elements:
        for category_element in category_elements:
            category_name = category_element.get_text(strip=True)
            if 'Selected' not in category_name and 'Show More' not in category_name and 'More' not in category_name:
                categories.append(category_name)
    return categories
