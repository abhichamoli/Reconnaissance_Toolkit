import os
import subprocess

def IP_add(host):
	print("\nIp-Address:", end = '')
	os.system('dig ' + host + ' A +short') 

def name_server(host):
	print("\nname-server:", end = '')
	os.system('dig ' + host + ' -t ns +short') 

def mail_server(host):
	print("\nmail-server:", end = '')
	os.system('dig ' + host + ' -t mx +short') 

def c_name(host):
	print("\nCNAME:", end = '')
	query = 'dig ' + host + ' -t' + ' CNAME' + ' +short'
	#print(query)
	p = subprocess.run(query, shell=True, capture_output=True, text=True)
	if p.stdout == '':
		print("no cname record")
	else:
		print(p.stdout)
	
	

#c_name('google.com')

