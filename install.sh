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

INSTALL_DIR="/usr/share/doc/fsociety"

echo "[✔] Checking directories...";
if [ -d "$INSTALL_DIR" ];
then
    echo "[◉] A directory SnapTube was found! Do you want to replace it? [Y/n]:" ;
    read mama
    if [ $mama == "y" ] ;
    then
        rm -R "$INSTALL_DIR"
    else
        exit
    fi
fi

echo "[✔] Installing ...";
echo "";
sudo apt-get install -y python-pip
sudo pip install --upgrade youtube_dl
sudo apt-get install -y libav-tools
git clone https://github.com/Manisso/SnapTube.git $INSTALL_DIR;
echo "#!/bin/bash
python $INSTALL_DIR/snaptube.py" '${1+"$@"}' > snaptube;
chmod +x snaptube;
sudo cp snaptube /usr/bin/;
rm snaptube;


if [ -d "$INSTALL_DIR/SnapTube" ];
then
    echo "";
    echo "[✔]Tool istalled with success![✔]";
    echo "";
    echo "[✔]====================================================================[✔]";
    echo "[✔] ✔✔✔ All is done!! You can execute tool by typing snaptube  !   ✔✔✔ [✔]";
    echo "[✔]====================================================================[✔]";
    echo "";
else
    echo "[✘] Installation faid![✘] ";
    exit
fi
