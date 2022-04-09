from requests import get, exceptions
import sys
import os
def check_domain(site):
    try:
        get("http://" + site, timeout = 3)
        http = True
    except exceptions.ConnectionError:
        http = False
 
    try:
        get("https://" + site, timeout = 3)
        https = True
    except exceptions.ConnectionError:
        https = False
 
    if http or https:
        os.system(f"echo {site} >> src/notavailable.txt")
    else:
        os.system(f"echo {site} >> src/available.txt")
os.system("echo  > src/notavailable.txt")
os.system("echo  > src/available.txt")
for url in range(len(sys.argv) - 1):
    check_domain(sys.argv[url + 1])