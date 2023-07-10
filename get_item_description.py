import requests
from bs4 import BeautifulSoup


def get_item_description(url):

    item_id = url.split('?')[0].split('/')[-1]  # this should be `392861887827`
    item_descr_url = 'https://vi.vipr.ebaydesc.com/ws/eBayISAPI.dll?ViewItemDescV4&item={item_id}'

    print(item_id)
    soup = BeautifulSoup(requests.get(item_descr_url.format(
        item_id=item_id)).content, 'html.parser')
    item_description = soup.get_text(strip=True, separator='\n')
    return item_description
