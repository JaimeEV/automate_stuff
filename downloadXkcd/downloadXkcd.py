import requests, os, bs4 

url = 'http://xkcd.com' 
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
    # TODO: Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.txt)

    # TODO: Find the URL of the comic image.
    # TODO: Download the image.
    # TODO: Save the image to ./xkcd.
    # TODO: Get the Prev button's url.
print('Done.') 


