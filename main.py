import os
import requests
import datetime
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("TOKEN")
USER_NAME = os.getenv("USER_NAME")
GRAPH_ID = "graph1"

# MAKING ACCOUNT -------------------------------------------------------

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",


}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# MAKING GRAPH ---------------------------------------------------------

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Training",
    "unit": "commit",
    "type": "int",
    "color": "momiji",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# ADDING COMMIT -------------------------------------------------------

now = datetime.datetime.now()
date = now.strftime("%Y%m%d")
print(date)

commit_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"

commit_params = {
    "date": date,
    "quantity": "1",
}

response = requests.post(url=commit_endpoint, json=commit_params, headers=headers)
print(response.text)

# UPDATING COMMIT (Changing value. No effect to this graph) ----------------------------------------------------------

DATE_TO_CHANGE = date

update_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{DATE_TO_CHANGE}"

update_params = {
    "quantity": "2"
}

# response = requests.put(url=update_endpoint, json=update_params, headers=headers)
# print(response.text)


# DELETING COMMIT-----------------------------------------------------------

delete_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{DATE_TO_CHANGE}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)