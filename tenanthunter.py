import requests
import argparse
import sys
from termcolor import colored
import re
from pyfiglet import Figlet

banner = Figlet(font='standard')
banner_text = banner.renderText('TENANTHUNTER')
print(colored(banner_text.rstrip(), 'white'))
print()
banner = "        === Enumerate domains to Azure AD tenant IDs instantly! ==="
banner += "\n                  === By Lodzie Kotekya (axylisdead) ===\n"
print(banner)

parser = argparse.ArgumentParser(prog='tenanthunter.py')

if '-h' in sys.argv or '--help' in sys.argv:
    print('TenantHunter (by Lodzie Kotekya)')
    print('A small script to enumerate/resolve domains to Azure AD tenant IDs.\n')
    print('Arguments:')
    print('-h = (H)elp menu (you are here dumbass)')
    print('-t <DOMAIN> or --domain <DOMAIN> = The domain you wish to find the tenant ID of')
    print('-m = (M)inimal. It only prints the tenant ID and OAuth login page. The full response is left out.\n')
    print('Coming later (not yet implemented):')
    print('-e = Subdomain (e)numeration. Planned to use crt.sh to find subdomains for the TLD and enumerate all of those to tenant IDs too.')
    print('-s <FILENAME> = (S)ave to file. Saves the results to a file. It isn\'t fucking rocket science. In the meantime you can just write what gets displayed to stdout to a file by doing something like: python tenanthunter.py -t example.com > outfile.txt')
    print('\nYeah enjoy or whatever idfc')
    sys.exit()

parser.add_argument("-t", "--domain", help="Specify the domain")
parser.add_argument("-m", "--minimal", action="store_true", help="Minimal output")

args = parser.parse_args()

if not args.domain:
    print(colored("\nERROR: Please provide a domain using the -t or --domain argument.", "red"))
    sys.exit()

url = f"https://enterpriseregistration.windows.net/{args.domain}/EnrollmentServer/Contract?api-version=1.4"

response = requests.get(url)

if not args.minimal:
    print(colored("Full Response:", "green"))

    print(response.text)

if "invalid_tenant" in response.text or "AADSTS90002" in response.text:
    print("\n" + colored("ERROR: Tenant not found (are you sure that the domain runs on Azure AD?)", "red") + "\n")
else:
    match = re.search(r"\b\w{8}-\w{4}-\w{4}-\w{4}-\w{12}\b", response.text)
    if match:
        tenant_id = match.group()
        print("\n" + colored(f"Tenant ID found:", "green") + " " + tenant_id)
        oauth_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/authorize?client_id=0"
        print(colored("OAuth login:", "green") + " " + oauth_url + "\n")
    else:
        print("\n" + colored("ERROR: Tenant ID not found in the response.", "red") + "\n")
