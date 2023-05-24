import requests


class SirotinskyAPI:
    url = 'https://api.sirotinsky.com/'

    def __init__(self, username, password):
        data = {'username': username, 'password': password}
        response = requests.post('https://api.sirotinsky.com/token', data=data)
        response = response.text[17:]
        self.token = response[:-26]


    def say_hello(self, name):
        response = requests.get('https://api.sirotinsky.com/hello/' + name)
        return response.text

    def efrsb_trader(self, inn):
        response = requests.get('https://api.sirotinsky.com/' + self.token + '/efrsb/trader/' + inn)
        return response.text

    def efrsb_manager(self, inn):
        response = requests.get('https://api.sirotinsky.com/' + self.token + '/efrsb/manager/' + inn)
        return response.text

    def efrsb_person(self, inn):
        response = requests.get('https://api.sirotinsky.com/' + self.token + '/efrsb/person/' + inn)
        return response.text

    def efrsb_organisation(self, inn):
        response = requests.get('https://api.sirotinsky.com/' + self.token + '/efrsb/organisation/' + inn)
        return response.text

    def efrsb_party(self, inn):
        response = requests.get('https://api.sirotinsky.com/' + self.token + '/dadata/party/' + inn)
        return response.text

username = 'HSE_student'
password = '123123123'

x = SirotinskyAPI(username, password)

print(x.token)



