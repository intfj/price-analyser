import requests

SCRAPER_API_KEY = "32f9326539f91b64524c0dbf72b48153"

def scrape_all_marketplaces(product, url, condition, margin, marketplaces):
    results = []
    if "amazon" in marketplaces:
        results.append({"marketplace": "Amazon", "price": 99.99})
    if "ebay" in marketplaces:
        results.append({"marketplace": "eBay", "price": 89.99})
    if "walmart" in marketplaces:
        results.append({"marketplace": "Walmart", "price": 92.99})
    if "etsy" in marketplaces:
        results.append({"marketplace": "Etsy", "price": 95.49})

    lowest = min([x["price"] for x in results])
    recommended = round(lowest + (lowest * float(margin) / 100), 2)

    return {
        "product": product,
        "results": results,
        "recommended_price": f"${recommended}"
    }
