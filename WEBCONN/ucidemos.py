import requests
import json
import datetime
import uba_uci
import scim_update_group
import scim_put_group

def main(s1,token,user,gc,rtime):
    success = 0
#    s1 = input("Introduzca el nombre del tenant:")
 #   user = input("Introduzca el upn:")
#    token = getpass("Introduzca token:")
#    gc = input("Introduzca grupo de cuarentena:")
#    rtime = input("Introduza fecha de inicio de búsqueda en formato d/m/y:" )
#    ttime = datetime.datetime.strptime(rtime + " 00:00:00", "%d/%m/%Y %H:%M:%S").timestamp()
#    print(ttime)
#    ttime = str(ttime).replace(".","") + "00"
#    ttime = datetime.datetime.today()-datetime.timedelta(days=1)
#    ttime2 = ttime.timestamp()
#    ttime2 = str(ttime2).replace(".","")[:-3]
    uci=uba_uci.getuci(s1,token,user,rtime)
    print("The user's UCI is: ", str(uci))
    if uci < 500:
        response = "The user's UCI is: " + str(uci) + " moving user to group " + gc
       # scim_put_group.creategroup(s1,token,gc,user)
        scim_update_group.updategroup(s1,token,user,gc)
        return(response,'red')
    else:
        response = "The user's UCI is: " + str(uci) + " ,not moving user to group " + gc
        return(response,'blue')
                                    
