import os


def zone_transfer(host):
    command = "dnsrecon -d " + host
    os.system(command)

