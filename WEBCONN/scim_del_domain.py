import requests
import json
import url_validator

l = []
def getuiddom(s1,token,dom):
 if url_validator.main(s1)=="Found": 
     s2 = "https://" + s1 + ".goskope.com/api/v2/scim/Users"
     headers1 = {'Netskope-Api-Token':token, 'accept':'application/scim+json;charset=utf-8'}
     try:
         with requests.Session() as s:
            i = s.get(s2,headers=headers1)
            for x in i.json().get('Resources'):
             if dom in x['userName']:
                l.append(x['id'])
            return(l,"ok")
     except requests.exceptions.ConnectionError:
            print("exception executed")
            return(l,"Connection problem, please check the tenant name and network settings")
 else:
     return(l,"Tenant not found")
