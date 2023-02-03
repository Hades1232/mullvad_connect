import subprocess
import random
import requests

all_list = ["al", "au", "at", "be", "br", "bg", "ca", "hr", "cz", "dk", "ee", "fi", "fr", "de", "hk", "hu", "ie", "il", "it", "jp", "lv", "lu", "md", "nl", "nz", "mk", "no", "pl", "pt", "ro"\
   "rs", "sg", "sk", "za", "es", "se", "ch", "gb", "ae", "us"]

fast_vpn_list = ["us", "jp", "hk"]

al = ["tia"]
au = ["adl", "bne", "cbr", "mel", "per", "syd"]
at = ["vie"]
be = ["bru"]
br = ["sao"]
bg = ["sof"]
ca = ["mtr", "tor", "van"]
hr = ["zag"]
cz = ["prg"]
dk = ["cph"]
ee = ["tll"]
fi = ["hel"]
fr = ["mrs", "par"]
de = ["dus", "fra"]
hk = ["hkg"]
hu = ["bud"]
ie = ["dub"]
il = ["tlv"]
it = ["mil", "rom"]
jp = ["osa", "tyo"]
lv = ["rix"]
lu = ["lux"]
md = ["kiv"]
nl = ["ams"]
nz = ["akl"]
mk = ["skp"]
no = ["osl", "svg"]
pl = ["waw"]
pt = ["lis"]
ro = ["buh"]
rs = ["beg"]
sg = ["sin"]
sk = ["bts"]
za = ["jnb"]
es = ["mad"]
se = ["got", "mma", "sto"]
ch = ["zrh"]
gb = ["lon", "mnc"]
ae = ["dxb"]
us = ["qas", "atl", "chi", "dal", "den", "hou", "lax", "mia", "nyc", "phx", "rag", "slc", "sjc", "sea", "uyk"]

fast_vpn = True

check_is_this_bin = False
is_logging = False


def create_account():
    global is_logging
   
    create_info = subprocess.check_output(["mullvad", "account", "create"])
    if 'New account created!' in str(create_info):
        print("new account created")
        is_logging = True
    
def get_account():
    global is_logging
    create_info = subprocess.check_output(["mullvad", "account", "get"])
    if str(create_info) == "Not logged in on any account":
        is_logging = False
    else:
        is_logging = True
    

def login(login_key):
    
    global is_logging
    login_info = subprocess.check_output(["mullvad", "account", "login" if check_is_this_bin == False else "set", str(login_key)])
    
   
    if str(login_info) == f'b\'Mullvad account \"{str(login_key)}" set\\n\'' and is_logging != True:
        print("Login!")
        is_logging = True
    
    elif is_logging != False:
        print("Login Error...")
   
    
    else:
        print("Already Logined!")

def status():
    status_info = subprocess.check_output(["mullvad", "status"])
    if "Disconnected" == str(status_info):
        print("Disconnected")
    elif "Connected" == str(status_info):
        print("Disconnected")

def logout():
   global is_logging
   
   if is_logging == True:
    
    logout_info = subprocess.check_output(["mullvad", "account", "logout" if check_is_this_bin == False else "unset"])
    
    if str(logout_info) == "b'Mullvad account removed\\n'":
        print("Logout!")
        is_logging = False
    else:
        print("Logout Error..")  

   else:
       print("You're not current login!")

     
async def select_location(location1 = "random", location2 = "random", fast_vpn = False):
    
    location1 = all_list if location1 == "random" else location1
    if fast_vpn == True: location1 = fast_vpn_list[random.randint(0, len(fast_vpn_list)) -1 if location1 == "random" else location1] 
    

    location2 = globals()[location1][random.randint(0, len(globals()[location1]) - 1) if location2 == "random" else location2]
             

    print(location1)
    print(location2)
    
  
    location_info = subprocess.check_output(["mullvad", "relay", "set", "location", str(location1), str(location2)])
        

    if str(location_info) == 'b\'Relay constraints updated\\n\'':
        print("Country Setting Done!")
    else:
        print("Country Setting Error..")

def connect():
    connect = subprocess.check_output(["mullvad", "connect"])
    

async def disconnect():
    disconnect = subprocess.check_output(["mullvad", "disconnect"])
    



def get_current_ip():
  checkError = True
  while checkError:
    try:
        new_ip = requests.get('https://api.myip.com/').json()['ip']
        return new_ip
    except Exception as e:
        pass