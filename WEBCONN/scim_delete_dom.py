import requests
import base64
import json
from scim_del_domain import getuiddom
import url_validator

resp = "No users found with this domain in the tenant or tenant connection issues"

def main(s1,token,dom):
    if url_validator.main(s1)=="Found":
        (ide,res) = getuiddom(s1,token,dom)
        print(ide)
        print(res)
        for g in ide:
                s2 = "https://" + s1 + ".goskope.com/api/v2/scim/Users/" + g
                headers1 = {'Netskope-Api-Token':token, 'accept':'application/scim+json;charset=utf-8'}
                with requests.Session() as s:
                  try:
                    global resp  
                    i = s.delete(s2,headers=headers1)
                    resp=i
                    print(resp)
                  except:
                    resp="Connection problem, please check the tenant name and network settings"
                    print(resp)
        return(resp)
    else:
        return("Tenant not found")
