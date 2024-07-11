import requests
import re


class UserAgent:
    def __init__(self):
        self._apikey = "glbbLNMBxjNgMAV8IbL3Tvf163oARD4T"

    def get_apikey(self):
        return self._apikey

    def set_apikey(self, apikey):
        self._apikey = apikey

    def randomua(self):
        header = {"apikey": self.get_apikey()}
        payload = {}
        endpoint = "https://api.apilayer.com/user_agent/generate?mobile=true&android=true"
        return requests.get(endpoint, headers=header, data=payload).json()['ua']


class Login:

    def __init__(self):
        useragent = UserAgent()
        self.head = {
            'User-Agent': f'{useragent.randomua()}'}
        self.token = ""
        self.cookie = ""

    def login(self):
        cookie = input("Cookie: ")
        try:
            data = requests.get('https://business.facebook.com/business_locations', headers={
                'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 ('
                              'KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36',
                # don't change this user agent.
                'referer': 'https://www.facebook.com/',
                'host': 'business.facebook.com',
                'origin': 'https://business.facebook.com',
                'upgrade-insecure-requests': '1',
                'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                'cache-control': 'max-age=0',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'content-type': 'text/html; charset=utf-8'
            }, cookies={
                'cookie': cookie
            })
            find_token = re.search('(EAAG\w+)', data.text)
            self.token = find_token.group(1)
            self.cookie = cookie
            return "Token Sudah Didapat"
        except requests.exceptions.ConnectionError:
            return -1
        except:
            return -1

    def getuname(self):
        try:
            getteruname = requests.get(f'https://graph.facebook.com/me?fields=name&access_token={self.token}',
                                   cookies={
                                       'cookie': self.cookie
                                   })
            return getteruname.json()
        except requests.exceptions.ConnectionError:
            return -1
        except requests.exceptions.RequestException:
            return False
        except:
            return 303





main = Login()
main.login()
print(main.getuname())


