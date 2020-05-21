import lxml.html
import requests
import string

### Create a list of alphabet to loop though sites
alphabets = list(string.ascii_uppercase)
urls = ["http://eoddata.com/stocklist/NYSE/%s.htm"%letter for letter in alphabets]
print("*****Created *****\n %s"%urls)

### Looping through the site
for url in urls:
    ### requesting data from url
    siteinfo = requests.get(url)
    print('ON SITE:%s' % url)

    ### convert data fo usable data and use
    doc = lxml.html.fromstring(siteinfo.content)
    doc_tickers = doc.xpath("//a[contains(@title, 'Display Q')]/text()")

    ### save the list of tickers to a file
    with open('tickers.txt', 'a+') as ticker_file:
        ### turns ['A','B','CD'] to "A B CD"
        ticker_file.write(" ".join(doc_tickers))