import os


def http_methods(host):
    command = "nmap -Pn -sV -p 80 -T4 --script http-methods --script-args http-method.text=all " + host
    os.system(command)


def hidden_files(host):
    command = "nmap -sV -p 80 --script http-enum " + host
    os.system(command)


def waf(host):
    command = "nmap -p 443 --script http-waf-detect " + host
    os.system(command)


def sql(host):
    command = "nmap -p 3306 --script mysql-info " + host
    os.system(command)


def ftp(host):
    command = "nmap -p 21 -sS --script ftp-anon,tftp-enum,ftp-vsftpd-backdoor " + host
    os.system(command)


def vul(host):
    command = "nmap -sV -p21-8080 --script vulners " + host
    os.system(command)


def smtp(host):
    command = "nmap -p25 --script smtp-commands,smtp-enum-users --script-args smtp-enum-users.methods={VRFY} " + host
    os.system(command)


def port(host):
    command = "nmap --open " + host
    print()
    os.system(command)

def banner(host):
    command = "nmap --open -sV " + host
    print()
    os.system(command)



