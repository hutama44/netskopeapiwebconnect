import requests
requests.packages.urllib3.disable_warnings()
import base64
import json
import csv
import url_validator

def main(s1,token):
    if url_validator.main(s1)=="Found":
        s2 = "https://" + s1 + ".goskope.com/api/v2/steering/apps/private"
        #true=true
        tag1=tag2="test"

        headers1 = {'Netskope-Api-Token':token, 'accept':'application/scim+json;charset=utf-8', 'Content-Type': 'application/scim+json;charset=utf-8'}

        def creation(row):
         name = row[0]
         host = row[1]
         real = row[2]
         proto = row[3]
         port = row[4]
         pubid = row[5]
         pubname = row[6]

         pay = {
            "app_name": name,
            "host": host,
            "real_host": real,
            "protocols": [
                {
                    "type": proto,
                    "port": port
                }
            ],
            "publishers": [
                {
                    "publisher_id": pubid,
                    "publisher_name": pubname
                }
            ],
            "tags": [
                {
                    "tag_name": tag2
                }
            ],
            "use_publisher_dns": False,
            "clientless_acces": False,
            "trust_self_signed_certs": True
            } 
         try:
             with requests.Session() as s:
                print("Creando applicación " + name + ":")
                i = s.post(s2,headers=headers1, data=json.dumps(pay), verify=False) 
                return("Finished")
         except requests.exceptions.ConnectionError:
             print("exception executed")
             return("Connection problem, please check the tenant name and network settings")

        with open('apps.csv', newline='') as csvfile:
            documento = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in documento:
                finished = creation(row)
        return(finished)
    else:
        return("Tenant not Found")

