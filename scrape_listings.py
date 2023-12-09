from get_item_description import get_item_description
from utils.item_url_shortener import item_url_shortener
from utils.generate_ebay_img_webp_fromhref import generate_webp


def scrape_listings(soup):
    try:
        results_div = soup.find(
            "ul", class_=["srp-results srp-list clearfix", "srp-results srp-grid clearfix"]
        )

        # listing_elements = results_div.find_all(
        #     "li",
        #     class_=[
        #         "s-item s-item__dsa-on-bottom",
        #         "s-item s-item__pl-on-bottom",
        #         "s-item s-item__before-answer s-item__pl-on-bottom",
        #     ],
        #     recursive=False,
        # )
        listing_elements = results_div.select(
            "li.s-item.s-item__dsa-on-bottom, li.s-item.s-item__pl-on-bottom, li.s-item.s-item__before-answer.s-item__pl-on-bottom")

        listings = []
        if listing_elements:
            for index, listing in enumerate(listing_elements):
                try:
                    if not listing.find(
                        "li", class_="srp-river-answer srp-river-answer--SPECTRUM_OF_VALUE_CAROUSEL"
                    ):
                        link_element = listing.find("a", class_="s-item__link")
                        price_element = listing.find(
                            "span", class_="s-item__price")
                        image_div = listing.find("div", class_="s-item__image")
                        image_element = image_div.find(
                            "img") if image_div else None
                        if link_element and price_element and image_element:
                            title = link_element.get_text(strip=True)
                            if "Opens in a new window or tab" in title or "New Listing" in title:
                                title = title.replace(
                                    "Opens in a new window or tab", "").replace("New Listing", "")
                            price = price_element.get_text(strip=True)
                            image_url = generate_webp(link_element.get('href'))
                            item_url = item_url_shortener(
                                link_element.get("href"))

                            # Visit the item's URL and extract the description
                            # description = get_item_description(item_url)

                            listings.append(
                                {
                                    "title": title,
                                    "price": price,
                                    # "description": description,
                                    "image_url": image_url,
                                    "link": item_url,
                                    "index": index,  # Add the index of the listing
                                }
                            )
                except Exception as e:
                    print(f"Error occurred while parsing listing: {e}")
    except Exception as e:
        print(f"Error occurred while scraping listings: {e}")

    # Sort the listings based on their index to maintain the original order
    listings.sort(key=lambda x: x["index"])
    return listings
