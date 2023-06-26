# TenantHunter

![image](https://github.com/axylisdead/TenantHunter/assets/135433130/70323c27-1dac-4ace-bb8b-6cf3d2b61e4a)

# Description
TenantHunter is a small script to resolve domains to Azure AD tenants (and OAuth login portals)
It is incredibly useful for pentesting companies or governments powered by the Azure ecosystem

Features:
- <b>Resolves domain to tenant ID</b>
- <b>Resolves tenant ID to OAuth login portal</b>
- <b>More upcoming features but for now that's it</b>

# Requirements
Python 3
<br>
requests
<br>
argparse
<br>
sys
<br>
termcolor
<br>
re
<br>
pyfiglet

<b>You can install all of the dependencies by cloning the repository and running: ```pip install -r requirements.txt```

# Usage
Run normally: ```python3 tenanthunter.py -t example.com```
<br>
Run in minimised mode (excludes full response): ```python3 tenanthunter.py -mt example.com```

# Arguments
- ```-t``` or ```--domain``` | Specifies the domain to find the tenant ID of
- ```-m``` or ```--minimal``` | Tells the script to run in minimal mode (excludes full response)

# To Do
- Subdomain enumeration (Use crt.sh to find subdomains for the TLD and enumerate all of those to tenant IDs too)
- Save to file (Saves the results to a file)

# Disclaimer
This is to be used for educational purposes only blah blah (insert boilerplate shite here)

# License
This code was proudly written and published under the <a href=https://plusnigger.org>+NIGGER license</a>, a modified version of Daddy Stallmans <a href="https://www.gnu.org/licenses/gpl-3.0.txt">GPL v3 license</a>

# Credits
All work was done by me, Lodzie Kotekya. You can find me on <a href="https://t.me/lodzie">Telegram</a>
