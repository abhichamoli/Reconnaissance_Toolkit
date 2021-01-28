#! /usr/bin/python3


from colorama import Fore
import Banner
import Dns
import whois
import subdomain
import zonetransfer
import nmapmodule
import smb

print(Fore.BLUE + Banner.banner)

text = ('''Enter the options to perform specified operation

1) PortScanning
2) BannerGrabbing
3) who's-Enumeration
4) Dns-Enumeration
5) Sub-domain-Enumeration
6) Zone-Transfer
7) SMB Enumeration
8) My-Sql Enumeration
9) Http Enumeration
10)Vulnerability Scanner
11)SMTP Enumeration
12)FTP Enumeration
''')

print(Fore.GREEN + text)


option = input("enter your choice: ")


if option == '1':
    host = input("\nenter host name: ")
    nmapmodule.port(host)


if option == '2':
    host = input("\nenter host name: ")
    nmapmodule.banner(host)



if option == '3':
    host = input("\nenter host name: ")

    whois.who_is(host)

if option == '4':
    choice = (''' \nEnter the options to get specified information

1)Ip-Address
2)Name-server
3)Mail-server 
4)CName
''')


    print(choice)



    option = input("enter your choice: ")

    host = input("\nenter host name: ")

    if option == '1':
        Dns.IP_add(host)

    if option == '2':
        Dns.name_server(host)

    if option == '3':
        Dns.mail_server(host)

    if option == '4':
        Dns.c_name(host)

if option == '5':
    host = input("\nenter host name: ")
    subdomain.sub_domain(host)

if option == '6':
    host = input("\nenter host name: ")
    zonetransfer.zone_transfer(host)


if option == '7':
    host = input("\nenter host name: ")
    user = input("\nenter user name: ")
    smb.smb_share(host, user)


if option == '8':
    host = input("\nenter host name: ")
    nmapmodule.sql(host)


if option == '9':

    print('''\n1)HTTP-methods
2)Finding hidden files
3)WAF detection
''')




    option = input("Enter your choice: ")
    host = input("\nenter host name: ")

    if option == '1':
        nmapmodule.http_methods(host)

    if option == '2':
        nmapmodule.hidden_files(host)

    if option == '3':
        nmapmodule.waf(host)



if option == '10':
    host = input("\nenter host name: ")
    nmapmodule.vul(host)



if option == '11':
    host = input("\nenter host name: ")
    nmapmodule.smtp(host)



if option == '12':
    host = input("\nenter host name: ")
    nmapmodule.ftp(host)

