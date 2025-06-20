import requests
import url_validator

def mainjobid(s1,token,jobid):
    if url_validator.main(s1)=="Found":
        token = "Bearer " + token
        s2 = "https://" + s1 + ".goskope.com/api/v2/atp/scans/reports/" + jobid
        headers1 = {'Authorization':token, 'accept':'application/json'}
        try:
            with requests.Session() as s:
                i = s.get(s2,headers=headers1)
                print("Validando solicitud")
                print(i.text)
                print(i)
                return(i.text)
        except requests.exceptions.ConnectionError:
            print("exception executed")
            return("Connection problem, please check the tenant name and network settings")
    
    else:
        return("Tenant not found")
