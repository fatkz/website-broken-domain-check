from cmath import pi
from encodings import utf_8
import os
import time
import argparse
import re
from pyparsing import line
import requests
from urllib.parse import urlparse
import requests
import json
from color import *

parser = argparse.ArgumentParser()
parser.add_argument('--site=', nargs='+')
list = []
for _, value in parser.parse_args()._get_kwargs():
    if value is not None:
        try:
            list.append(value)
            args_site = list[0]
        except:
            continue

args_site = str(args_site)
args_site = args_site.replace("[", "")
args_site = args_site.replace("]", "")
args_site = args_site.replace("'", "")




def main(site):
    with open('src/data.txt','w',encoding='utf8') as payload:
        r = requests.get(f'http://{site}')
        payload.write(str(r.text))
    os.system(f"echo {site}  > src/beforafterdomains.txt")
        
    


def extractURLs(fileContent,site_data):
    os.system(f"echo ''  > src/data.txt")
    os.system(f"echo ''  > src/link.txt")
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', fileContent.lower())
    for i in urls:  ##olmadığı zaman -1 döndürür
        os.system(f"echo {i} >> src/link.txt")



def analisys(args_site):
    os.system(f"echo ''  > src/out_of_links.txt")
    os.system(f"echo ''  > src/sitelinks.txt")
    args_site = '.'.join(args_site.split('.')[-2:])
    with open('src/link.txt',"r",encoding='utf8') as file:

        for line in file:
            domain = urlparse(f'{line}').netloc
            base_domain = '.'.join(domain.split('.')[-2:])
            domain_recapt = base_domain.find(args_site)
            if str(domain_recapt) == "-1":
                os.system(f"echo {domain} >> src/out_of_links.txt")
            else:
                os.system(f"echo {domain} >> src/sitelinks.txt")
                
                
                
def file_edit():
    
    with open("src/sitelinks.txt", "r") as fp:
        lines = fp.readlines()

    with open("src/sitelinks.txt", "w") as fp:
        for line in lines:
            if line.strip("\n") != "text to delete":
                fp.write(line)
    
    
    with open("src/out_of_links.txt", "r") as fp:
        lines = fp.readlines()

    with open("src/out_of_links.txt", "w") as fp:
        for line in lines:
            if line.strip("\n") != "text to delete":
                fp.write(line)
        
    # with open("src/sitelinks.txt") as file_in:
    #     lines_links = []
    #     lines_links1 = []
    #     try:
    #         for line in file_in:
    #             lines_links.append(line)
    #     except:
    #         pass
    #     lines_outoflinks = []
    #     lines_outoflinks1 = []
    #     try:
    #         for line in file_in:
    #             lines_outoflinks.append(line)
    #     except:
    #         pass
        
    #     for i in lines_links:
    #         if i not in lines_links1:
    #             lines_links1.append(i)
                
    #     for i in lines_outoflinks:
    #         if i not in lines_outoflinks1:
    #             lines_outoflinks1.append(i)
        
    #     # lines_links1 = list(set(lines_links))
    #     # lines_outoflinks1 = list(set(lines_outoflinks)) //error amk 9d76c6c47cmsh41ed99796162db3p1250acjsn02d0747f5d11
        
    #     for i in lines_links1:
    #         os.system("echo '' >> src/sitelinks.txt")
    #         os.system(f"echo {i} >> src/sitelinks.txt")
    #     for i in lines_outoflinks1:
    #         os.system("echo '' >> src/out_of_links.txt")
    #         os.system(f"echo {i} >> src/out_of_links.txt")
            
        
def size():
    file = open("src/link.txt", "r", encoding='utf8')
    file_out_of = open("src/out_of_links.txt", "r", encoding='utf8')
    file_site_links = open("src/sitelinks.txt", "r", encoding='utf8')
    out_of_links_number = len(file_out_of.readlines())
    site_links_number = len(file_site_links.readlines())
    link_number = len(file.readlines())
    print(Base.FAIL,+"All link size number: " +link_number+2 +Base.END)
    print(Base.FAIL,f"Out off link size number: {out_of_links_number}",Base.END)
    print(Base.FAIL,f"Site link size number: {site_links_number}",Base.END)





def whois(args_site):
    f = open("src/out_of_links.txt", "r")
    for x in f:    
        os.system(f"python3 checker.py {x}")
        # url = "https://domain-checker7.p.rapidapi.com/whois"

        # querystring = {"domain":f"{x}"}

        # headers = {
        #     "X-RapidAPI-Host": "domain-checker7.p.rapidapi.com",
        #     "X-RapidAPI-Key": f"{args_api_key}"
        # }

        # response = requests.request("GET", url, headers=headers, params=querystring)
        # r = response.text
        # j = json.loads(r)
        # print(j)
        # try:
        #     valid_check = j['valid']
        #     print(valid_check)
        # except:
        #     pass
    
def result():
    file = open("src/available.txt","r")
    for i in file:
        print(ANSI_Compatible.Color(120),f"Available Domain: {i}",ANSI_Compatible.END)






os.system("echo  > src/available.txt")
main(args_site)
myFile = open("src/data.txt",encoding='utf8')
fileContent = myFile.read()
URLs =  extractURLs(fileContent,args_site)
analisys(args_site)
file_edit()
whois(args_site)
result()
# size()





