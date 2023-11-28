import requests
import random


class PocketRepository():
    def __init__(self, consumer_key, access_token):
        self.consumer_key = consumer_key
        self.access_token = access_token

    def fetch_items_randomly(self, state, tag, count):
        params = {
            'consumer_key': self.consumer_key,
            'access_token': self.access_token,
            'state': state,
            'tag': tag,
        }
        response = requests.post('https://getpocket.com/v3/get', params=params)
        if response.status_code != 200:
            print("Error: " + response.text)
            exit()

        response = response.json()

        if len(response["list"]) == 0:
            print("No items found.")
            exit()

        result = []
        for v in response["list"].values():
            tmp = {}
            tmp["url"] = v["given_url"]
            tmp["title"] = v["given_title"]
            tmp["excerpt"] = v["excerpt"] if "excerpt" in v else ""
            result.append(tmp)

        return random.sample(result, count)
