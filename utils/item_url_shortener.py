

def item_url_shortener(url):
    shortened_url = ''
    for char in url:
        if char == '?':
            break
        shortened_url += char
    return shortened_url
