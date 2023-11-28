import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        response_body = self.get_response_body()
        data = json.loads(response_body)
        return data
    
# Create an instance of GetRequester with the URL
requester = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')

# Call the get_response_body method
response_body = requester.get_response_body()
print(response_body)

# Call the load_json method
data = requester.load_json()
print(data)    