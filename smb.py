import os

def smb_share(host, user):
	command = "smbclient -L " + host + " -U " + user
	print()
	os.system(command)


