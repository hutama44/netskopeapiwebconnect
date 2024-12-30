import requests
import base64
import json
import scim_get_uid
import url_validator

def creategroup(s1,token,group,user_upn):
    if url_validator.main(s1)=="Found":
        s2 = "https://" + s1 + ".goskope.com/api/v2/scim/Groups"

        headers1 = {'Netskope-Api-Token':token, 'accept':'application/scim+json;charset=utf-8', 'Content-Type': 'application/scim+json;charset=utf-8'}
        user_id = scim_get_uid.getuid(s1,token,user_upn)

        payload = {
                        'schemas': ['urn:ietf:params:scim:schemas:core:2.0:Group'],
                        'displayName': group,
                        'members': [
                                {
                                        'value': user_id,
                                }
                                ],
                        'externalId': 'User-Ext_id',
                        'meta': {
                                'resourceType': 'Group'
                                }
                }

        with requests.Session() as s:
            i = s.post(s2,headers=headers1, data=json.dumps(payload))
            return(i.text)
    else:
        return("Tenant not found")
