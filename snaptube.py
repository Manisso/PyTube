#!/usr/bin/env python
#
from __future__ import unicode_literals
import youtube_dl
import os
import sys

os.system("clear && clear && clear")
logo = '''
 .d8888b.                         88888888888       888               
d88P  Y88b                            888           888               
Y88b.                                 888           888               
 "Y888b.   88888b.   8888b.  88888b.  888  888  888 88888b.   .d88b.  
    "Y88b. 888 "88b     "88b 888 "88b 888  888  888 888 "88b d8P  Y8b 
      "888 888  888 .d888888 888  888 888  888  888 888  888 88888888 
Y88b  d88P 888  888 888  888 888 d88P 888  Y88b 888 888 d88P Y8b.     
 "Y8888P"  888  888 "Y888888 88888P"  888   "Y88888 88888P"   "Y8888  
                             888                                      
                             888                                      
                             888                                              
   \033[0m  \033[91m   \033[1m           }--{+} Coded By Manisso {+}--{
   \033[0m  \033[91m  \033[1m          }----{+}  fb.me/dzmanisso {+}----{
   \033[0m  \033[91m    \033[1m          }--{+} Greetz To IcoDz  {+}--{
'''
menu = '''\033[0m
    {1}--Video Download
    {2}--Audio Download
    {3}--Audio PlayList Download
    
    {99}-Exit                                                                                                                        
 '''
print logo
print menu

def quit():
            con = raw_input('Continue [Y/n] -> ')
            if con[0].upper() == 'N':
                exit()
            else:
                os.system("clear")
                print logo
                print menu
                select()
           
def  select():
  try:
    choice = input("SnapTub~# ")
    if choice == 1:
      os.system("clear")
      print """
 __     __  __        __                     
/  |   /  |/  |      /  |                    
$$ |   $$ |$$/   ____$$ |  ______    ______  
$$ |   $$ |/  | /    $$ | /      \  /      \ 
$$  \ /$$/ $$ |/$$$$$$$ |/$$$$$$  |/$$$$$$  |
 $$  /$$/  $$ |$$ |  $$ |$$    $$ |$$ |  $$ |
  $$ $$/   $$ |$$ \__$$ |$$$$$$$$/ $$ \__$$ |
   $$$/    $$ |$$    $$ |$$       |$$    $$/ 
    $/     $$/  $$$$$$$/  $$$$$$$/  $$$$$$/  

PUT URL EX: https://www.youtube.com/watch?v=PYJHFVBsmeQ	  
"""
      ydl_opts = {}
      with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		  ydl.download([raw_input('URL: ')])
      print("")
      quit()
    elif choice == 2:
      os.system("clear")
      print """
  /$$$$$$                  /$$ /$$          
 /$$__  $$                | $$|__/          
| $$  \ $$ /$$   /$$  /$$$$$$$ /$$  /$$$$$$ 
| $$$$$$$$| $$  | $$ /$$__  $$| $$ /$$__  $$
| $$__  $$| $$  | $$| $$  | $$| $$| $$  \ $$
| $$  | $$| $$  | $$| $$  | $$| $$| $$  | $$
| $$  | $$|  $$$$$$/|  $$$$$$$| $$|  $$$$$$/
|__/  |__/ \______/  \_______/|__/ \______/ 

PUT URL EX: https://www.youtube.com/watch?v=PYJHFVBsmeQ                                                 
"""
      ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
      with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		  ydl.download([raw_input('URL: ')])
      quit()    
    elif choice == 3:
      os.system("clear")
      print("""
 /$$$$$$$  /$$                     /$$ /$$             /$$    
| $$__  $$| $$                    | $$|__/            | $$    
| $$  \ $$| $$  /$$$$$$  /$$   /$$| $$ /$$  /$$$$$$$ /$$$$$$  
| $$$$$$$/| $$ |____  $$| $$  | $$| $$| $$ /$$_____/|_  $$_/  
| $$____/ | $$  /$$$$$$$| $$  | $$| $$| $$|  $$$$$$   | $$    
| $$      | $$ /$$__  $$| $$  | $$| $$| $$ \____  $$  | $$ /$$
| $$      | $$|  $$$$$$$|  $$$$$$$| $$| $$ /$$$$$$$/  |  $$$$/
|__/      |__/ \_______/ \____  $$|__/|__/|_______/    \___/  
                         /$$  | $$                            
                        |  $$$$$$/                            
                         \______/                             
                         
EX: https://www.youtube.com/watch?v=lp-EO5I60KA&list=PLMC9KNkIncKtPzgY-5rmhvj7fax8fdxoj                        
""")
      d3 = raw_input('playlist URL: ')
      os.system("clear")
      os.system("youtube-dl -cit --extract-audio --audio-format mp3 " + d3 )
      print("")
      quit()
  except(KeyboardInterrupt):
    print ""
select()
