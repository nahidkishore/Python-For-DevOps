import requests
import json
from flask import Flask, request

app = Flask(__name__)

# Define a route that handles POST requests from GitHub webhooks
@app.route('/createJira', methods=['POST'])
def createJira():
    # Extract the JSON payload from the GitHub webhook
    github_payload = request.json

    # Check if the payload contains the required keys and 'comment' body is 'jira'
    if 'action' in github_payload and github_payload['action'] == "created" \
            and 'comment' in github_payload and 'body' in github_payload['comment']:
        comment_body = github_payload['comment']['body']

        # Check if the body of the comment matches the specified text
        if comment_body.strip() == "jira":
            # Your existing Jira issue creation logic goes here

            url = "https://nahid0002.atlassian.net/rest/api/3/issue"
            API_TOKEN = ""  # Add your Jira API token here
            auth = requests.auth.HTTPBasicAuth("nahidkishore99@gmail.com", API_TOKEN)

            headers = {
                "Accept": "application/json",
                "Content-Type": "application/json"
            }

            payload = json.dumps({
                "fields": {
                    "description": {
                        "content": [{
                            "content": [{
                                "text": "Order entry fails when selecting supplier.",
                                "type": "text"
                            }],
                            "type": "paragraph"
                        }],
                        "type": "doc",
                        "version": 1
                    },
                    "project": {
                        "key": "NAH"
                    },
                    "issuetype": {
                        "id": "10006"
                    },
                    "summary": "Main order flow broken",
                },
                "update": {}
            })

            # Making a POST request to create a Jira issue
            response = requests.request(
                "POST",
                url,
                data=payload,
                headers=headers,
                auth=auth
            )

            # Returning the Jira API response as JSON if the condition is met
            return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
        else:
            return "Comment should be 'jira'"
    else:
        return "Invalid payload format or action is not 'created'"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000)
