import os


def sub_domain(host):
    command = "sublist3r -d " + host
    os.system(command)

