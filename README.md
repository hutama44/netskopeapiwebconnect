# About/Acerca de
WEB interface to interact with Netskope's API in container format / Interface WEB para interactuar con el API de Netskope en formato de contenedor

# Required API Privileges/Permisos Requeridos en el API
/api/v2/steering/apps/private \
/api/v2/policy/npa/rules \
/api/v2/steering/apps/private/tags \
/api/v2/incidents/user/uciimpact \
/api/v2/scim/Groups	\
/api/v2/steering/apps/private/tags/getpolicyinuse \
/api/v2/incidents/users/uci/reset \
/api/v2/scim/Users	\
/api/v2/ubadatasvc/user/uci \
/api/v2/policy/npa/policygroups
 
# Usage/Uso
Clone the repository locally: / Clonar el repositorio localmente:
```
git clone https://github.com/hutama44/netskopeapiwebconnect
```
Access the created folder: / Acceder a la carpeta creada:
```
cd netskopeapiwebconnect
```
Build the docker image: / Construir la imagen de docker:
```
sudo docker image build -t netskope/webapicont .
```
Run the docker image: / Ejecutar la imagen: 
```
sudo docker container run --rm -p 5000:5000 -ti netskope/webapicont
```
Access the web portal in port 5000: / Acceder al portal en el puerto 5000: 
```
http://127.0.0.1:5000/login
```
