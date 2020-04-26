import bs4
import requests

url = "https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRE55YXpBU0FtVnVLQUFQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen"
data = requests.get(url)
soup = bs4.BeautifulSoup(data.text, 'html.parser')
n = 0
for para in soup.find_all('h3'):
    n=n+1
    print("News",n,": " + para.text + "\n")


