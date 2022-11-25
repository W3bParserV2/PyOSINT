#Made by W3bParser
from pystyle import *
import time

banner = """
 __          ______  _     _____                           _____        ____   _____ _____ _   _ _______ 
 \ \        / /___ \| |   |  __ \                         |  __ \      / __ \ / ____|_   _| \ | |__   __|
  \ \  /\  / /  __) | |__ | |__) |_ _ _ __ ___  ___ _ __  | |__) |   _| |  | | (___   | | |  \| |  | |   
   \ \/  \/ /  |__ <| '_ \|  ___/ _` | '__/ __|/ _ \ '__| |  ___/ | | | |  | |\___ \  | | | . ` |  | |   
    \  /\  /   ___) | |_) | |  | (_| | |  \__ \  __/ |    | |   | |_| | |__| |____) |_| |_| |\  |  | |   
     \/  \/   |____/|_.__/|_|   \__,_|_|  |___/\___|_|    |_|    \__, |\____/|_____/|_____|_| \_|  |_|   
                                                                  __/ |                                  
                                                                 |___/                                   """

# --- Define the init function ---
def init():
    System.Clear()
    print(Col.purple + banner)
    print(Col.white + '[' + Col.yellow + '!' + Col.white + '] Welcome to PyOSINT by W3bParser.')

# --- Define the main function ---
def main():
    print(Col.white + '[' + Col.yellow + '!' + Col.white + '] Please chose an option : ')
    print(Col.white + """
[1] - Google Dorks Template
[2] - Google Dorks Generator
[3] - Github""")
    # --- Define the user choice ---
    select = input(Col.white + '\nuser@w3bparser:~$ ')
    # --- Define the select action ---
    if select == '1':
        print(Col.white + '[' + Col.yellow + '!' + Col.white + '] Please chose an option : ')
        print(Col.white + """
[1] - Website vulnerability's
[2] - CMS/Admin login pages
[3] - Database Breachs/Index of""")
        # --- Define the Website vuln dorks ---
        select2 = input(Col.white + '\nuser@w3bparser:~$ ')
        if select2 == '1':
            print('''
inurl:"index.php?page=news.php"
intitle:"index of"|"access_token.json"
intitle:"index of" intext:"Apache/2.2.3"
intitle:"index of smtp"
intext:"index of" "ipaddress"
inurl:_admin "login"
intitle:"web server login" "please enter your login"
inurl:"/index.php?qa=login"
inurl:/admin ext:config
intitle:"index of" "configure.sh"
intitle:"index of" "deploy.sh"''')
        if select2 == '2':
            print('''
inurl:"admin/default.aspx"
intitle:"Pi-hole-ip" inurl:admin
intitle:"Synnefo Admin"
inurl:_admin "login.aspx"
intitle:"index of smtp"
intitle:"User Authentication : IR*"
intitle:"Login page for" inurl:user.cgi
intitle:"Login - Residential Gateway"
intitle:"Login to Redash"
inurl:_admin "login"
inurl:"/index.php?qa=login"''')
        if select2 == '3':
            print('''
index of /wp-admin.zip
intitle:"index of" include/
intitle:"index of" "db.py"
intitle:"index of" "db.txt"
intitle:"index of" "db.xlsx"
intitle:"index of" "db.sql"
intitle:"index of" "db.php"
ntext:"index of" "phonepe" "wp-content"
intext:"index of" "ipaddress"
inurl: /wp-includes/uploads
intitle:"index of" "release.sh"
intitle:"index of" "*db.sh"
intext:"index of" ".sql"''')
    if select == '2':
        # --- Define the custom OSINT dorks generation ---
        print(Col.white + '[' + Col.red + '!' + Col.white + '] The tool is still under developement. This feature is under developement too.')
        print(Col.white + '[' + Col.green + '!' + Col.white + '] This will generate a personnal information dorks')
        name = input(Col.white + '[' + Col.yellow + '!' + Col.white + '] Enter name : ')
        lastname = input(Col.white + '[' + Col.yellow + '!' + Col.white + '] Enter lastname : ')
        country = input(Col.white + '[' + Col.yellow + '!' + Col.white + '] Enter the target country (format : France : fr / United Kingdom : uk etc...) : ')
        print(Col.purple + '"' + name + ' ' + lastname + '" filetype:pdf | xlsx | docx | txt site:' + country)
    if select == '3':
        print(Col.white + 'Github : ' + Col.purple + 'https://github.com/W3bParser')

if __name__ == "__main__":
    init()
    while True:
        main()
