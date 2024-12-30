import requests
import base64
import json
from getpass import getpass
from scim_get_uid import getuid
import url_validator

def main(s1,token,upn):
    if url_validator.main(s1)=="Found":
        ide = getuid(s1,token,upn)
        if ide == "0":
            return("User not found or connection to tenant failed, please check your input")
        s2 = "https://" + s1 + ".goskope.com/api/v2/scim/Users/" + ide

        headers1 = {'Netskope-Api-Token':token, 'accept':'application/scim+json;charset=utf-8'}

        with requests.Session() as s:
            i = s.delete(s2,headers=headers1)
            return(i)
    else:
        return("Tenant not found")
