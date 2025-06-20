import requests
requests.packages.urllib3.disable_warnings()
import url_validator

def main(s1,token,filename):
    if url_validator.main(s1)=="Found":
        token = "Bearer " + token
        s2 = "https://" + s1 + ".goskope.com/api/v2/atp/scans/filescan?scantype=sandbox"
        headers1 = {'Authorization':token, 'accept':'application/json'}
        files= {'file':open(filename,'rb')}
        print("Filename:",filename)
        try:
            with requests.Session() as s:
                i = s.post(s2,headers=headers1, files=files)
                print("Analizando Archivo")
                print(i.text)
                print(i)
                return(i.text)
        except requests.exceptions.ConnectionError:
            print("exception executed")
            return("Connection problem, please check the tenant name and network settings")

    else:
        return("Tenant not found")

