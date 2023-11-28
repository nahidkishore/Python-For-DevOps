import requests



response=requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
# print(response.json())

# complete_details=response.json()
# print(complete_details[0]["id"])
# print(complete_details[0]["user"]["login"])

complete_details=response.json()

for i in range(len(complete_details)):
    
    print(complete_details[i]["user"]["login"])