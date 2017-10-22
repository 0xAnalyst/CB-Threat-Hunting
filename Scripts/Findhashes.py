import requests
import json
import urlparse
import urllib2
URL = r"https://IP:PORT/api/v1/sensor?hostname=HOSTNAME" #Hostname to check if it is live or not
URL2= r"https://IP:PORT/api/v1/binary/"
headers = {'X-Auth-Token': 'Token Here' # add the API key here after generating it from Carbon Black
           }

r = requests.get(URL,headers=headers, verify=False)
data = json.loads(r.text)
if(data[0]['status']=="Online"): #Machine is live
   print "Agent is  Online"

hashes = open("hashes.txt", "r") #hashes file and it is path
for i in hashes:
	print "getting results for" + i
	summary =  requests.get(URL2 + i + "/summary",headers=headers, verify=False)
	data =  json.loads(summary.text)
	if data['host_count'] !=0 :
		print "found on " + str(data['host_count']) + "machines"
		print "The Following are the observed file names\t\t\n" 		
		for filename in data['observed_filename']:
			print filename + "\n"
		for j in range(len(data['endpoint'])):
			print "found in hostname\t" + data['endpoint'][j] 
	else:
		print "binary not found"
	
		
		

