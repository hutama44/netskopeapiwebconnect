import requests
requests.packages.urllib3.disable_warnings()
import base64
import json

def main(s1):
    success = 0
    s2 = "https://" + s1 + ".goskope.com"
    try:
        with requests.Session() as s:
            i = s.get(s2, verify=False)
            return("Found")
    except requests.exceptions.ConnectionError:
        print("Tenant not found")
        return("Connection problem, please check the tenant name and network settings")
