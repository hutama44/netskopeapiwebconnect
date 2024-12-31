import requests
import base64
import json
import url_validator

def resetuci(s1,token,user_upn):
    if url_validator.main(s1)=="Found":
        s2 = "https://" + s1 + ".goskope.com/api/v2/incidents/users/uci/reset"
        headers1 = {'Netskope-Api-Token':token, 'accept': 'application/json','Content-Type': 'application/json'}
        payload = {
                        'users': [
                            user_upn
                            ]
                }

        with requests.Session() as s:
            i = s.post(s2,headers=headers1, data=json.dumps(payload))
            print(i)
            return(i.text)
    else:
        return("Tenant not found")

