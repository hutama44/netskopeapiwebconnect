import requests
import base64
import json
import url_validator

def main(s1,token,us):
    if url_validator.main(s1)=="Found":
        success = 0
        s2 = "https://" + s1 + ".goskope.com/api/v2/scim/Users"


        headers1 = {'Netskope-Api-Token':token, 'accept':'application/scim+json;charset=utf-8'}
        try:
            with requests.Session() as s:
                i = s.get(s2,headers=headers1)

                for x in i.json().get('Resources'):
                    if x['userName'] == us:
                        result = json.dumps(x,indent=4)
                        success=1
                if success != 1:
                    return('User not found')
                else:
                    return(result)
        except requests.exceptions.ConnectionError:
            print("exception executed")
            return("Connection problem, please check the tenant name and network settings")
    else:
        return("Tenant not found")
