import requests
import json
import datetime
import uba_uci
import scim_update_group
import scim_put_group
import url_validator

def main(s1,token,user,gc,rtime):
    if url_validator.main(s1)=="Found":
        success = 0
        uci=uba_uci.getuci(s1,token,user,rtime)
        print("The user's UCI is: ", str(uci))
        if uci < 500:
            response = "The user's UCI is: " + str(uci) + " moving user to group " + gc
           # scim_put_group.creategroup(s1,token,gc,user)
            scim_update_group.updategroup(s1,token,user,gc)
            return(response,'red')
        else:
            response = "The user's UCI is: " + str(uci) + ", not moving user to group " + gc
            return(response,'blue')
    else:
        return("Tenant not found",'black')
                                        
