import requests
requests.packages.urllib3.disable_warnings()
import base64
import json
import csv
import scim_update_group

def main(s1,token):
    s2 = "https://" + s1 + ".goskope.com/api/v2/scim/Users"
    headers1 = {'Netskope-Api-Token':token, 'accept':'application/scim+json;charset=utf-8', 'Content-Type': 'application/scim+json;charset=utf-8'}

    def creation(row):
        first_name = row[0]
        last_name = row[1]
        upn = row[2]
        gp = row[3]

        payload = {
                    'schemas': ['urn:ietf:params:scim:schemas:core:2.0:User'],
                    'userName': upn,
                    'name': {
                            'familyName': last_name,
                            'givenName': first_name
                            },
                    'active': 'true',
                    'emails': [
                            {
                                    'value': upn,
                                    'primary': 'true'
                            }
                            ],
                    'externalId': 'User-Ext_id',
                    'meta': {
                            'resourceType': 'User'
                            }
            }



        with requests.Session() as s:
            i = s.post(s2,headers=headers1, data=json.dumps(payload))
            print("Creando usuario :" + upn)
        print("Moviendo usuario a group: " + gp)
        print(scim_update_group.updategroup(s1,token,upn,gp))

    with open('users.csv', newline='') as csvfile:
        documento = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in documento:
            creation(row)
    return('Finished')
        
