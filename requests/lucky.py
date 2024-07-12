import requests, webbrowser, bs4

print('Googling...')    # display text while downloading the Google page
res = requests.get('https://www.google.com/search?q=Mozart')

#retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')

link_elems = soup.select('a', {'jsname' :'UWckNb'})
print(link_elems[0])


