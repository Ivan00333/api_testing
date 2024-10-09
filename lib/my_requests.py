import requests

class MyRequests():
    @staticmethod
    def _send(url: str, data: dict, headers: dict, cookies: dict, method: str):
        if headers is None:
            headers = {}
        if cookies is None:
            cookies = {}


        if method == 'POST':
            response = requests.post(url, json=data, headers=headers, cookies=cookies)
        elif method == 'GET':
            response = requests.get(url, params=data, headers=headers, cookies=cookies)
        elif method == 'PUT':
            response = requests.put(url, data=data, headers=headers, cookies=cookies)
        elif method == 'DELETE':
            response = requests.put(url, data=data, headers=headers, cookies=cookies)
        else:
            raise Exception(f"Bad HTTP method '{method}' was received")

        return response

    @staticmethod
    def post(url: str, json: dict=None, headers: dict=None, cookies: dict=None):
        return MyRequests._send(url, json, headers, cookies, 'POST')

    @staticmethod
    def get(url: str, data: dict=None, headers: dict=None, cookies: dict=None):
        return MyRequests._send(url, data, headers, cookies, 'GET')

    @staticmethod
    def put(url: str, data: dict=None, headers: dict=None, cookies: dict=None):
        return MyRequests._send(url, data, headers, cookies, 'PUT')

    @staticmethod
    def delete(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        return MyRequests._send(url, data, headers, cookies, 'DELETE')