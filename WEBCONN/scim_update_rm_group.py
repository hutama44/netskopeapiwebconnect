import requests
import json
from scim_get_uid import getuid
from scim_get_guid import getguid
import url_validator

def updategroup(s1,token,upn,gp):

    if url_validator.main(s1)=="Found":
        user_id = getuid(s1,token,upn)
        group = getguid(s1,token,gp)
        if group == None:
            return("Group not found")
        print(group)
        s2 = "https://" + s1 + ".goskope.com/api/v2/scim/Groups/" + group

        headers1 = {'Netskope-Api-Token':token, 'accept':'application/scim+json;charset=utf-8', 'Content-Type': 'application/scim+json;charset=utf-8'}

        payload = {
                        'schemas': ['urn:ietf:params:scim:api:messages:2.0:PatchOp'],
                        'Operations': [
                                {
                                        'path': 'members',
                                        'op': 'Remove',
                                        'value': {
                                                'value': {
                                                        'value': user_id,
                                                        }
                                                }
                                }
                                ],
                }

        with requests.Session() as s:
            i = s.patch(s2,headers=headers1, data=json.dumps(payload))
            return(i)
    else:
        return("Tenant not found")
