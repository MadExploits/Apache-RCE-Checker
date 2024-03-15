#!/usr/bin/python3

import urllib3
import requests as req
from os.path import exists
from os import system, name
from multiprocessing.dummy import Pool
from colorama import Fore,Style

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class ApacheVuln:
    def __init__(self):
        self.list_version_apache = [
            '2.4.49',
            '2.4.50',
            '2.4.51',
            '2.4.52',
            '2.4.53',
            '2.4.54',
        ]
        self.user_agents = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0"
        }

    def clear_command_line(self):
        if name == "nt":
            system("cls")
        else:
            system("clear")

    def ApacheCheck(self,website):
        # Checked
        try:
            with req.session() as s:
                r = s.get(f'{website}', headers=self.user_agents, verify=False, timeout=30)
                for x in range(len(self.list_version_apache)):
                    if 'Server' in r.headers and f"Apache/{self.list_version_apache[x]}" in r.headers['Server']:
                        print(Fore.GREEN + f"{website} => Apache/{self.list_version_apache[x]}" + Style.RESET_ALL)
                        with open('apachexp.txt', 'a+') as wr:
                            wr.write(f"{website}" + "\n")
                    else:
                        break
                if "/usr/share/doc/apache2/README.Debian.gz" in r.text:
                    print(Fore.GREEN + f"{website} => Apache Default Page Found!" + Style.RESET_ALL)
                else:
                    pass

                print(f"{website} => Cannot Find Apache Vuln")
        except:
            pass

                    

    def main(self):
        
        print("CVE-2021-41773 / CVE-2021-42013 Finder By ./Mr.Mad")

        list_target = input("List of urls : ")
        if exists(list_target):
            with open(list_target, 'r') as r:
                read = r.read()
                target = read.split("\n")
                with Pool(int(10)) as Th:
                    Th.map(self.ApacheCheck, target)
                    Th.join()
                    Th.close()
        else:
            print(f"File Not Found [{list_target}]")




if __name__ == "__main__":
    run = ApacheVuln()
    run.clear_command_line()
    run.main()
