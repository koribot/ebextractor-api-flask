# ebextractor# ebextractor

Expected type of Request is POST
->>you can paste the copied html of ebay search result together with the url, the body should be should be JSON:


{
 htmlContent: "outerhtml",
 url: "ebay search result url"
}

You can use this tool to Sringify your HTML: https://jsonformatter.org/json-stringify-online




## Endpoints

### `/api/extract`

Endpoint to receive the outerHTML sent via Post request in the body.

Example:
```plaintext
/api/extract/
```
{
  "htmlContent": "<!DOCTYPE html>\r\n<html lang=\"en\">\r\n<head>\r\n    <meta charset=\"UTF-8\">\r\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\r\n    <title>Sample HTML Document</title>\r\n</head>\r\n<body>\r\n\r\n    <header>\r\n        <h1>Welcome to My Website</h1>\r\n    </header>\r\n\r\n    <nav>\r\n        <ul>\r\n            <li><a href=\"#home\">Home</a></li>\r\n            <li><a href=\"#about\">About</a></li>\r\n            <li><a href=\"#contact\">Contact</a></li>\r\n        </ul>\r\n    </nav>\r\n\r\n    <main>\r\n        <section id=\"home\">\r\n            <h2>Home Section</h2>\r\n            <p>This is the main content of the home section.</p>\r\n        </section>\r\n\r\n        <section id=\"about\">\r\n            <h2>About Section</h2>\r\n            <p>This is the main content of the about section.</p>\r\n        </section>\r\n\r\n        <section id=\"contact\">\r\n            <h2>Contact Section</h2>\r\n            <p>This is the main content of the contact section.</p>\r\n        </section>\r\n    </main>\r\n\r\n    <footer>\r\n        <p>&copy; 2023 My Website. All rights reserved.</p>\r\n    </footer>\r\n\r\n</body>\r\n</html>\r\n",
  "url": "ebay search result url"
}
```



### `/api/extract/using_keyword`

Endpoint to receive a query sent via the URL.

Example:
```plaintext
/api/extract/using_keyword?q=shoes





- 💰 Highest Price: Obtain the maximum price observed in the search results.
- 💵 Lowest Price: Identify the minimum price found among the listings.
- 📊 Average Price: Calculate the mean price across the search results.
- 🎯 Middle Price: Determine the median price, offering a representative value.
- 🔑 Keyword Occurrence: Track and quantify the frequency of each keyword throughout the listings.
- 💲 Price Occurrence: Gain an understanding of how often different price points appear in the search results.
-1 click search, if you go to listing page you will see on the top right of the listing section an option to search your item via google, wallmart, amazon or search it all


