# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://nahid0002.atlassian.net//rest/api/3/project"


API_TOKEN= ""
auth = HTTPBasicAuth("nahidkishore99@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

# print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

# outputs=json.loads(response.text)
# name=outputs[0]["name"]
# print(name)

outputs=json.loads(response.text)

# Loop through the data and display names
for item in outputs:
    print(item['name'])