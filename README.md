# ebextractor# ebextractor

Expected type of Request is POST
->>you can paste the copied html of ebay search result together with the url, the body should be should be JSON:


{
 htmlContent: "outerhtml",
 url: "ebay search result url"
}

You can use this tool to Sringify your HTML: https://jsonformatter.org/json-stringify-online




# Endpoints

### `/api/extract`

Endpoint to receive the outerHTML sent via Post request in the body.

Usage:
```
/api/extract
```
`Request Body should be like this`
```json
{
  htmlContent: "Your html in string form",
  url: "ebay search result url"
}
```


### `->  /api/extract/using_keyword`

/api/extract/using_keyword
Endpoint to receive a query sent via the URL.

Usage:
```
/api/extract/using_keyword?q=shoes

```



- 💰 Highest Price: Obtain the maximum price observed in the search results.
- 💵 Lowest Price: Identify the minimum price found among the listings.
- 📊 Average Price: Calculate the mean price across the search results.
- 🎯 Middle Price: Determine the median price, offering a representative value.
- 🔑 Keyword Occurrence: Track and quantify the frequency of each keyword throughout the listings.
- 💲 Price Occurrence: Gain an understanding of how often different price points appear in the search results.
-1 click search, if you go to listing page you will see on the top right of the listing section an option to search your item via google, wallmart, amazon or search it all


