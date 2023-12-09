from urllib.parse import urlparse


url = "https://www.ebay.com/itm/155901771487?hash=item244c783edf:g:fRQAAOSwob9lZMlP&amdata=enc%3AAQAIAAAA0MKc%2BRyWjV%2FIgi%2BZkVVY6feRQ65qvgyo%2B8Bw2q5HMRz7WpDX8i0OdtkPUPcQxa63D46CIyj%2FVszggkdS0Y%2BzH4sIbXtqEArllOBj1KGtbqPaScwFTNLwFbk7FIXQEdznl%2FZvkLdk%2Fkx1Vkg%2FaxUVpxv%2BIvpzOf%2FNaaeHLZ0qiD%2B1Qse23wWV35ylEUmVPBruO7SonRK2Y7Gvjj%2BHHQ%2F8n4ZdbpBID%2BPRwf7U04QefTwAlIkhto9qGwC8ZWBA0wXWki1zCiirh%2BWS2XWB%2F822e3o%3D%7Ctkp%3ABFBM8rDxz4lj"
url2 = "https://www.ebay.com/itm/155595890020?hash=item243a3cdd64:g:YSwAAOSwKkRlM~Wi&amdata=enc%3AAQAIAAAA0Kh4WPQDlX59mdN76OE2qIheFLBUIsPZSysP4Tq%2FonTcQgJYWz8tgCwebD%2BkbD%2FxXWp%2BnPcY3nYHAXMOrlVvCcZPnuk01ocv4gQP33PNIvzXg3L%2BuNwGRsiQ2gK3ItJ2wx2m%2Fo6eZoduPByBi2F7WKky%2Fp4Wxv5ayubtXZvFY9j7OsAEg0SInY1tPUXsT3CVOD%2Bqoc5KtXpmI9ExShN9bGMLPg39VWZaRxAkjgUKsYUCEi6v43K1UzbLAMVKAWyZONGJc%2BBggiWcvy4P4dv0oJs%3D%7Ctkp%3ABFBM8rDxz4lj"


# def generate_webp(url):
#     extracted_image_id = ''
#     begin = False
#     token_conter = 0
#     for index in range(6, len(url)):
#         if url[index] == ':':
#             token_conter += 1
#             if (token_conter == 2):
#                 begin = True
#                 continue
#         if url[index] == '&':
#             begin = False
#             break
#         if begin == True:
#             extracted_image_id += url[index]
#     print(extracted_image_id)

def generate_webp(url):
    tokens = url.split(':')
    image_id = tokens[3].split('&')[0]
    return f"https://i.ebayimg.com/thumbs/images/g/{image_id}/s-l300.webp"
