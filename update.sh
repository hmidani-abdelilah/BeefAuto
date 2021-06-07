green=`tput setaf 2`
RED=`tput setaf 1`
reset=`tput sgr0`
if [ "$(id -u)" != "0" ]; then
   echo "${RED}This script must be run as root" 1>&2
   exit 1
fi
if [ -d "/root/BeefAuto" ] 
then
    rm -r /root/BeefAuto
    echo "${RED}Removing Beef Auto And installing it Again${reset}"
    
    cd /root/ && git clone https://github.com/youhacker55/BeefAuto
else
    echo "${green}[+]${reset}Installing BeefAuto in root Directory"
    cd /root/ && git clone https://github.com/youhacker55/BeefAuto
fi

echo "${green}[+]${reset}Updated"

