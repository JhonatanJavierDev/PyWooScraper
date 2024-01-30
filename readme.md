# PyWooScrap

**PyWooScraper** is a **simple,** **very easy**-to-use **library** created to provide a simple **scraping system** for **WordPress** websites with **Woocomerce**. This simple **scraper** allows you to **obtain** the **number of products** that a **WordPress store** has, per page in addition to a general total. This library will continue to add features and new additions, feel free to modify and interact with it, I love that **fork**.


# Install

    > pip install pywooscraper
   

## Example

```py
    from pywooscraper.scraper import ProductScraper

    base_url = 'https://yourlink.com/shop/page/'
    scraper = ProductScraper(base_url)
    scraper.run()
```

