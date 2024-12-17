import requests
import base64
import json
import scim_get_guid

def deletegroup(s1,token,group):
        s2 = "https://" + s1 + ".goskope.com/api/v2/scim/Groups/"

        headers1 = {'Netskope-Api-Token':token, 'accept':'*/*'}
#        print(s1,group)
        id=scim_get_guid.getguid(s1,token,group)
        with requests.Session() as s:
            i = s.delete(s2+id,headers=headers1)
            return(i.text)

