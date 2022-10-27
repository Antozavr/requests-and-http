import requests
from pprint import pprint
import json
import os


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Authorization': f'OAuth {self.token}'}

    def upload(self, path_to_file):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        res = requests.get(f'{url}/upload?path={path_to_file}&overwrite={False}',
                           headers=headers).json()
        with open(path_to_file, 'rb') as f:
            try:
                requests.put(res['href'], files={'file': f})
            except KeyError:
                print(res)


if __name__ == '__main__':
    path_to_file = 'TEXT.txt'
    token = ...
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
