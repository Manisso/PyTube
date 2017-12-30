#!/usr/bin/env python
#
from __future__ import unicode_literals
import youtube_dl
import os
import sys

os.system("clear && clear && clear")
license = """
MIT License

Copyright (c) 2017-2018 Manisso

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
logo = '''
                          ....              ...     ..      ..     
   .xnnx.  .xx.       .xH888888Hx.        x*8888x.:*8888: -"888:   
 .f``"888X< `888.   .H8888888888888:     X   48888X `8888H  8888   
 8L   8888X  8888   888*"""?""*88888X   X8x.  8888X  8888X  !888>  
X88h. `8888  X888k 'f     d8x.   ^%88k  X8888 X8888  88888   "*8%- 
'8888 '8888  X8888 '>    <88888X   '?8  '*888!X8888> X8888  xH8>   
 `*88>'8888  X8888  `:..:`888888>    8>   `?8 `8888  X888X X888>   
   `! X888~  X8888         `"*88     X    -^  '888"  X888  8888>   
  -`  X*"    X8888    .xHHhx.."      !     dx '88~x. !88~  8888>   
   xH88hx  . X8888   X88888888hx. ..!    .8888Xf.888x:!    X888X.: 
 .*"*88888~  X888X  !   "*888888888"    :""888":~"888"     `888*"  
 `    "8%    X888>         ^"***"`          "~'    "~        ""    
    .x..     888f \033[0m  \033[91m   \033[1m }--{+} Coded By Manisso {+}--{
\033[0m   88888    :88f  \033[0m  \033[91m  \033[1m}----{+}  fb.me/dzmanisso {+}----{
\033[0m   "88*"  .x8*~    \033[0m  \033[91m   \033[1m}--{+} Greetz To IcoDz  {+}--{
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
    choice = input("YDM~# ")
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
