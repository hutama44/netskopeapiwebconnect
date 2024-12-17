import requests
import base64
import json

def main(s1,token,us):
	success = 0
	s2 = "https://" + s1 + ".goskope.com/api/v2/scim/Users"


	headers1 = {'Netskope-Api-Token':token, 'accept':'application/scim+json;charset=utf-8'}

	with requests.Session() as s:
		i = s.get(s2,headers=headers1)

		for x in i.json().get('Resources'):
				if x['userName'] == us:
					result = json.dumps(x,indent=4)
					success=1
		if success != 1:
			return('User not found')
		else:
			return(result)

