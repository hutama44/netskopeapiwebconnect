import requests
import json
import url_validator

success = 0
def main(s1,token,polname,state):
    script = []
    if url_validator.main(s1)=="Found":
        s2 = "https://" + s1 + ".goskope.com/api/v2/policy/npa/rules"
        headers1 = {'Netskope-Api-Token':token, 'accept':'application/json'}
        with requests.Session() as s:
            i = s.get(s2,headers=headers1)
            for x in i.json().get('data'):
                if x['rule_name'] == polname:
                    result = json.dumps(x,indent=4)
                    result = x
                    success=1
            if success != 1:
                print('Policy not found')
            else:
                print(result) 
        polid = result["rule_id"]
        script.append("with requests.Session() as s:<br>")
        script.append(" i = s.get("+s2+",headers=headers1)<br>")
        print(polid)
        print(result)
        s3 = "https://htamayo.goskope.com/api/v2/policy/npa/rules/" + polid
        if state == "disable":
            result = { "enabled":"0" }
        if state == "enable":
            result = {"enabled":"1"}

        headers2 = {'Netskope-Api-Token':token, 'accept':'application/json', 'Content-Type': 'application/json'}

        with requests.Session() as s:
            i = s.patch(s3,headers=headers2, data=json.dumps(result))
            print(i.text)
            return(i.text,script)
    else:
        return('Tenant not found')
