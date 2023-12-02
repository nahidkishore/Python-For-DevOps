This project aims to automate GitHub-Jira integration using Python Flask, enabling seamless communication between GitHub repositories and Jira issue tracking system. The automation involves creating Jira issues based on GitHub repository events through webhook triggers.

### Table of Contents

* Pre-requisites

* Installation Requirements

* Verification Process

* Code Explanation

* Utilizing Requests Library

* Flask Setup

* Jira Issue Creation Logic

* GitHub Webhooks Integration

* Webhooks Configuration

* Automated Issue Creation Process

* Conditional Conditions for Jira Issue Creation


### Pre-requisites:

To run the Flask application, ensure the following:

Pip3 (Python's package manager for Python 3) is installed using 'sudo apt update' and 'sudo apt install python3-pip' commands.

Verify pip3 installation and version using 'pip3 --version'.

Install Flask using 'pip3 install flask'.
```
sudo apt update
sudo apt install python3-pip
pip3 --version
pip3 install flask
```
### Code Explanation:
```
# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask

app = Flask(__name__)

# Define a route that handles GET requests
@app.route('/createJira', methods=['POST'])
def createJira():

    url = "https://nahid0002.atlassian.net/rest/api/3/issue"

    API_TOKEN=""

    auth = HTTPBasicAuth("nahidkishore99@gmail.com", API_TOKEN)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps( {
        "fields": {
        "description": {
            "content": [
                {
                    "content": [
                        {
                            "text": "Order entry fails when selecting supplier.",
                            "type": "text"
                        }
                    ],
                    "type": "paragraph"
                    }
                ],
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
    } )


    response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
    )

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```
The Python Flask script sets up a REST API endpoint ('/createJira') that handles POST requests and communicates with the Jira REST API to create issues. Here's a breakdown of the script's functionalities:

Libraries are imported: requests, HTTPBasicAuth, json, and Flask.

Flask application instance is created.

Function 'createJira()' is defined to construct and send a POST request to the Jira API to create an issue.

The payload includes specific details like description, project key, issue type, and summary formatted as per Jira API requirements.

A POST request is sent to the Jira API endpoint with authentication headers, and the response is returned in JSON format.

GitHub Webhooks Integration:

After clicking the "Add Webhooks" button, please verify if the webhooks were successfully added or not. In case of failure, kindly check what went wrong. Once the issue is resolved, click the "Redelivery" button. You will see a screenshot below with the successful addition of webhooks, indicated by a green checkmark.

After configuring GitHub webhooks, when we create an issue on GitHub repository and comment on it. The webhook triggers the Flask API endpoint, and GitHub webhooks automatically send the issue to the JIRA channel and create a new issue in the backlog section.

Below, in the screenshot image, we can view the new issue list in the backlog section.

Conditional Statements and Logic:

If I want to use a conditional statement, for example, when I comment on the GitHub issue section, I don't want an issue ticket to be generated in JIRA for every comment. I specifically want a JIRA ticket to be automatically created only when I comment 'jira' in the GitHub issue ticket. Otherwise, it should display a failed message.

Now, when I commented 'jira' in the GitHub issue, a new issue ticket got generated in the JIRA backlog automatically. Previously, there were three issues, and now there are four.

Checking the GitHub webhook section, we verified that an issue was created, and the body section shows 'jira'. This confirms our logic is working successfully.

Now, for our else conditions, if any message other than 'jira' is entered in the GitHub issue comment section, it will display the message 'Comment should be 'jira''.

Let's check all the else conditions. I commented 'test' in the GitHub issue ticket, then checked the GitHub webhooks, and found 'Comment should be 'jira''. However, no new issue ticket was generated in JIRA. So, our logic is operating correctly. Hence, if a comment other than 'jira' is made in the GitHub issue, JIRA won’t create a new issue ticket.

Conclusion:

The integration between GitHub and Jira streamlines the task management process by automating issue creation based on repository events. The conditional logic ensures precise control over issue creation, minimizing clutter in the issue tracking system and optimizing efficiency. This automation reduces manual efforts, enhances efficiency, and showcases the power of Python scripting for DevOps automation.

