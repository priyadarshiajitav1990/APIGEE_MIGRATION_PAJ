import requests, json
import sys, os
import ast
import base64

#pass values in command
org = raw_input("enter org name :  ")
sysadmin = raw_input("enter sysadmin id :  ")
syspass = raw_input("enter sysadmin password : ")
bs64 = base64.b64encode(sysadmin + ":" + syspass)
auth = "Basic " + bs64

##get environments
urlenv = "http://localhost:8080/v1/o/" + org + "/e/"
payload = ""
headers = { 'Authorization': auth }
responsenv = requests.request("GET", urlenv, data=payload, headers=headers)
respenv = ast.literal_eval(responsenv.text)
print("the envs are")
for env in respenv:
  print(env)

##get apis
urlapi = "http://localhost:8080/v1/o/" + org +"/apis"
response = requests.request("GET", urlapi, data=payload, headers=headers)
resparr = ast.literal_eval(response.text)


##get revision

for api in resparr:
  rev = []
  print("processing : " + api)
  for env in respenv:
    urlrev = "http://localhost:8080/v1/o/" + org + "/e/" + env + "/apis/" + api + "/deployments"
    response = requests.request("GET", urlrev, data=payload, headers=headers)
    resp_dict = json.loads(response.text)
    if "revision" in response.text :
     revis = int(resp_dict['revision'][0]['name'])
     print("revision deployed in " + env + " :   " )
     print(revis)
     rev.append(revis)

  #get the lowest revision
  if len(rev) != 0 :
    minimum = min(rev)
  #3 revision below the lowest revision deployed
  apirev = int(minimum) - 3
  #download the revisions and delete
  if apirev <= 0 :
     print("no revision to download and delete")
  while apirev > 0 :
      print("downloading revision : " )
      print(apirev)
      curlstring = "curl -H 'Authorization: " +  auth + "' http://localhost:8080/v1/o/" + org +"/apis/" + api + "/revisions/" + str(apirev) + "?format=bundle -o" +api+"_"+str(apirev)+".zip -s"
      os.system(curlstring)
      curlstringdel = "curl -X DELETE -H 'Authorization: " +  auth + "' http://localhost:8080/v1/o/" + org +"/apis/" + api + "/revisions/" + str(apirev)
      os.system(curlstringdel)
      apirev = apirev - 1




print("Process completed for all apis")
