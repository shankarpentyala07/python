import requests

"""
curl --request GET  --header "PRIVATE-TOKEN: <Access-Token>" 
https://gitlab.com/api/v4/users/shankarcodes/projects
"""

user_name = "shankarcodes"
token = "<access-token>"

#Construct URL to get projects for a specific user
url = f"https://gitlab.com/api/v4/users/{user_name}/projects"

#Make a request to gitlab 
res = requests.get(url)

print(res.status_code,res.reason)

#Get the response in json format
json_response = res.json()

#Iterate over the json response
for key in json_response:
    print(f"Project: {key['name']}")
    print(f"Project URL: {key['http_url_to_repo']}\n")
