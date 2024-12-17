import requests
requests.packages.urllib3.disable_warnings()
import base64
import json

def main(s1,token,app):
    success = 0
    s2 = "https://" + s1 + ".goskope.com/api/v2/infrastructure/publishers"
    headers1 = {'Netskope-Api-Token':token, 'accept':'application/json'}

    with requests.Session() as s:
        i = s.get(s2,headers=headers1, verify=False)
        for x in i.json().get('data').get('publishers'):
         if x['publisher_name'] == app:
          return("Publisher ID: " + str(x['publisher_id']))
          success = 1
        if success != 1:
            return("Publisher not found")

