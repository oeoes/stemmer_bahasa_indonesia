import requests
import re


class Kbbi():

    # Untuk memastikan kata yg dipotong tersedia di kbbi atau tidak
    def connect_to_kbbi(self, key):
        # create session object
        session_req = requests.session()

        # login url
        login_url = 'https://kbbi.kemdikbud.go.id/Account/Login'

        # get the page to find the access token
        result = session_req.get(login_url)
        token = re.findall(r'value="(.+)" />', result.text)

        # login information
        payload = {
            'Posel': 'oeoesroy@gmail.com',
            'KataSandi': '63635roy',
            '__RequestVerificationToken': token[0]
        }

        # login process
        result = session_req.post(
            login_url,
            data=payload,
            headers=dict(referer=login_url)
        )
        url = r'https://kbbi.kemdikbud.go.id/entri/'+key
        web = session_req.get(
            url,
            headers=dict(referer=url)
        )
        teks_web = web.text

        with open('result.txt', 'w+') as f:
            f.write(teks_web)
        find = open('result.txt').read()
        res = re.findall(r'(syllable|adjusted-par)', find)

        if len(res) > 0:
            return True
        else:
            return False

    def periksa_kata(self, kata):
        words = open(r'kata_dasar.txt', 'r')
        kata_dasar = words.read()
        if len(re.findall(r'\b'+kata+r'\b', kata_dasar)) > 0:
            return True
        else:
            return False

