import requests
from bs4 import BeautifulSoup
import traceback

class Request:
    headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36',
               'accept': '*/*'}
    error = False
    def __init__(self):
        super().__init__()


    def download_music(self, txt):
        try:
            self.mp3_downloader(self.mp3_search(pr.search(txt)))
            return self.chislo
        except Exception:
            self.error = True
            print(traceback.format_exc())
            return None


    def get_html(self, link):
        response = requests.get(url=link, headers=self.headers)
        return response

    def resp(self, url):
        html = self.get_html(link=url)
        if html.status_code != 200:
            self.error = True
        soup = BeautifulSoup(html.text, 'html.parser')
        item = soup.find('div', class_='music-popular__item')
        track = item.find('div', class_='popular-download')
        download_link = track.find('a', class_='popular-download-link').get('href')
        download_link = 'http://ru.drivemusic.me' + str(download_link)
        return download_link

    def mp3_search(self, url):
        html = self.get_html(link=self.resp(url=url))
        soup = BeautifulSoup(html.text, 'html.parser')
        item = soup.find('div', class_='song-author-btn-box')
        track = item.find_all('a')[1].get('href')
        link = 'http://ru.drivemusic.me' + str(track)
        return link


    def mp3_downloader(self, __downloadlink):
        chislo = pr.num_get
        req = requests.get(__downloadlink, stream=True, headers=self.headers)
        if req.status_code == 200:
            with open('attachments/audio/'+chislo+'.mp3', 'wb') as f:
                f.write(req.content)
                f.close()
        self.chislo = chislo



class Properties:
    @property
    def num_get(self) -> str:
        import random
        return str(random.randint(1000, 9999))

    def search(self, text):
        a = list(text)
        for i in range(a.count(' ')):
            indx = a.index(' ')
            a.remove(' ')
            if indx != 0 and a[indx-1] != ' ' and indx != -1:
                a.insert(indx, '+')
        a = ''.join(a)
        a = 'http://ru.drivemusic.me/?do=search&subaction=search&story=' + a
        return a




pr = Properties()
request = Request()