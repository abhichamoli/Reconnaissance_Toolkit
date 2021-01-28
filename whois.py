import os

def who_is(host):
	str = "whois " + host
	os.system(str)

#who_is('google.com')
