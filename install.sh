#!/bin/bash
clear
echo "
███╗   ███╗ █████╗ ███╗   ██╗██╗███████╗███████╗ ██████╗
████╗ ████║██╔══██╗████╗  ██║██║██╔════╝██╔════╝██╔═══██╗
██╔████╔██║███████║██╔██╗ ██║██║███████╗███████╗██║   ██║
██║╚██╔╝██║██╔══██║██║╚██╗██║██║╚════██║╚════██║██║   ██║
██║ ╚═╝ ██║██║  ██║██║ ╚████║██║███████║███████║╚██████╔╝
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚══════╝╚══════╝ ╚═════╝ 
▀▀█▀▀ █▀▀█ █▀▀█ █   █▀▀ ~ Tools Instaler By Ⓜ Ⓐ Ⓝ Ⓘ Ⓢ Ⓢ Ⓞ  ☪ ~
  █   █  █ █  █ █   ▀▀█ 
  ▀   ▀▀▀▀ ▀▀▀▀ ▀▀▀ ▀▀▀             

                                                ";

echo "[✔] Checking directories...";
if [ -d "/usr/share/doc/YDM" ] ;
then
echo "[◉] A directory YDM was found! Do you want to replace it? [Y/n]:" ; 
read mama
if [ $mama == "y" ] ; 
then
 rm -R "/usr/share/doc/YDM"
else
 exit
fi
fi

 echo "[✔] Installing ...";
 echo "";
 git clone https://github.com/Manisso/YDM.git /usr/share/doc/YDM;
 echo "#!/bin/bash 
 python /usr/share/doc/YDM/ydm.py" '${1+"$@"}' > ydm;
 chmod +x ydm;
 sudo cp ydm /usr/bin/;
 rm ydm;


if [ -d "/usr/share/doc/YDM" ] ;
then
echo "";
echo "[✔]Tool istalled with success![✔]";
echo "";
  echo "[✔]====================================================================[✔]";
  echo "[✔]  ✔✔✔   All is done!! You can execute tool by typing ydm  !     ✔✔✔ [✔]"; 
  echo "[✔]====================================================================[✔]";
  echo "";
else
  echo "[✘] Installation faid![✘] ";
  exit
fi
