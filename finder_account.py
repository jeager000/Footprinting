import requests
from termcolor import colored
import os
import time


baner="""


                  <•==================•>
                   | [Code by Jeager] |
<•=================|    [ ©2020 ]     |=================•>
    |   ___ __ _  ___ __ _  ___ _ __ __ _  ___| | __  |  
    |  / __/ _` |/ __/ _` |/ __| '__/ _` |/ __| |/ /  |  
    | | (_| (_| | (_| (_| | (__| | | (_| | (__|   <   |
    |  \___\__,_|\___\__,_|\___|_|  \__,_|\___|_|\_\  | 
<•==============                          ==============•>
               |  [ Youtube: CACACRACK ]  |   
               | [ Instagram: Jeager000 ] |          
              <•==========================•>"""  
  
  
print(colored(baner,'green'))
print(colored('Announcement:','cyan'))
print(colored('conditions for joining cacacrack,','cyan'))
print(colored('send any program (python3) that','cyan'))
print(colored('you make to e-mail: cacacrack000@gmail.com','cyan'))
print(os.linesep)
print(colored("[!]( get a username on any social media )[!]",'yellow'))
tag=str(input(colored('Enter tag: ','yellow')))
print(os.linesep)
print(colored('Waiting...','yellow'))
time.sleep(3)

facebook='https://www.facebook.com/'
x=requests.get(facebook+tag)
if x.status_code == 200:
  print(colored('Facebook found: '+facebook+tag,'green'))
else:
  print(colored('Facebook not found!!!','red'))
  
  
instagram='https://www.instagram.com/'
x=requests.get(instagram+tag)
if x.status_code == 200:
  print(colored('Instagram found: '+instagram+tag,'green'))
else:
  print(colored('Instagram not found!!!','red'))


google_plus='https://plus.google.com/'
x=requests.get(google_plus+tag+'/posts')
if x.status_code == 200:
  print(colored('Google plus found: '+google_plus+tag+'/posts','green'))
else:
  print(colored('Google plus not found!!!','red'))


twitter='https://www.twitter.com/'
x=requests.get(twitter+tag)
if x.status_code == 200:
  print(colored('Twitter found: '+twitter+tag,'green'))
else:
  print(colored('Twitter not found!!!','red'))


youtube='https://www.youtube.com/'
x=requests.get(youtube+tag)
if x.status_code == 200:
  print(colored('Youtube found: '+ youtube+tag,'green'))
else:
  print(colored('Youtube not fund!!!','red'))


wordpress='.wordpress.com'
p='https://'
x=requests.get(p+tag+wordpress)
if x.status_code == 200:
  print(colored('Wordpress found: https://'+tag+wordpress,'green'))
else:
  print(colored('Wordpress not found!!!','red'))


x=requests.get('https://'+tag+'.blogspot.com')
if x.status_code == 200:
  print(colored('Blogspot found: https://'+tag+'.blogspot.com','green'))
else:
  print(colored('Blogspot not found!!!','red'))


github='https://www.github.com/'
x=requests.get(github+tag)
if x.status_code == 200:
  print(colored('Github found: '+github+tag,'green'))
else:
  print(colored('Github not found!!!','red'))


wiki='https://www.wikipedia.org/wiki/User:'
x=requests.get(wiki+tag)
if x.status_code == 200:
  print(colored('Wikipedia found: '+wiki+tag,'green'))
else:
  print(colored('Wikipedia not found!!!','red'))
 

steam='https://steamcommunity.com/id/'
x=requests.get(steam+tag)
if x.status_code == 200:
  print(colored('Steam found: '+steam+tag,'green'))
else:
  print(colored('Steam not found!!!','red'))
  
  

flickr='https://www.flickr.com/people/'
x=requests.get(flickr+tag)
if x.status_code == 200:
  print(colored('Flickr found: '+flickr+tag,'green'))
else:
  print(colored('Flickr not found!!!','red'))
  
  
pinterest='https://www.pinterest.com/'
x=requests.get(pinterest+tag)
if x.status_code == 200:
  print(colored('Pinterest found: '+pinterest+tag,'green'))
else:
  print(colored('Pinterest not found!!!','red'))
  
  
soundcloud='https://soundcloud.com/'
x=requests.get(soundcloud+tag)
if x.status_code == 200:
  print(colored('SoundCloud found: '+soundcloud+tag,'green'))
else:
  print(colored('SoundCloud not found!!!','red'))
  
  
disqus='https://disqus.com/'
x=requests.get(disqus+tag)
if x.status_code == 200:
  print(colored('Disqus found: '+disqus+tag,'green'))
else:
  print(colored('Disqus not found!!!','red'))


medium='https://medium.com/'
x=requests.get(medium+tag)
if x.status_code == 200:
  print(colored('Medium found: '+medium+tag,'green'))
else:
  print(colored('Medium not found!!!','red'))
  
  
deviantart='.deviantart.com'
x=requests.get('https://'+tag+deviantart)
if x.status_code == 200:
  print(colored('Deviantart found: https://'+tag+deviantart,'green'))
else:
  print(colores('Deviantart not found!!!','red'))


vk='https://vk.com/'
x=requests.get(vk+tag)
if x.status_code == 200:
  print(colored('Vk found: '+vk+tag,'green'))
else:
  print(colored('Vk not found','red'))
  
  
about='https://about.me/'
x=requests.get(about+tag)
if x.status_code == 200:
  print(colored('About found: '+about+tag,'green'))
else:
  print(colored('About not found','red'))


imgur='https://imgur.com/user/'
x=requests.get(imgur+tag)
if x.status_code == 200:
  print(colored('Imgur found: '+imgur+tag,'green'))
else:
  print(colored('Imgur not found!!!','red'))


flip='https://flipboard.com/@'
x=requests.get(flip+tag)
if x.status_code == 200:
  print(colored('FlupBoard found: '+flip+tag,'green'))
else:
  print(colored('FlipBoard not found','red'))


slid='https://slideshare.net/'
x=requests.get(slid+tag)
if x.status_code == 200:
  print(colored('SlidShare found: '+slid+tag,'green'))
else:
  print(colored('SlidShare not found!!!','red'))
  
  
foto='https://fotolog.com/'
x=requests.get(foto+tag)
if x.status_code == 200:
  print(colored('Fotolog found: '+foto+tag,'green'))
else:
  print(colored('Fotolog not found!!!','red'))
  
  
spotify='https://open.spotify.com/user/'
x=requests.get(spotify+tag)
if x.status_code == 200:
  print(colored('Spotify found: '+spotify+tag,'green'))
else:
  print(colored('Spotify not found!!!','red'))
  
  
mix='https://www.mixcloud.com/'
x=requests.get(mix+tag)
if x.status_code == 200:
  print(colored('Mixcloud found: '+mix+tag,'green'))
else:
  print(colored('Mixcloud not found','red'))
  
  
scribd='https://www.scribd.com/'
x=requests.get(scribd+tag)
if x.status_code == 200:
  print(colored('Scribd found: '+scribd+tag,'green'))
else:
  print(colored('Scribd not found!!!','red'))
  
  
bado='https://www.badoo.com/en/'
x=requests.get(bado+tag)
if x.status_code == 200:
  print(colored('Badoo found: '+bado+tag,'green'))
else:
  print(colored('Badoo not found!!!','red'))


patreon='https://www.patreon.com/'
if x.status_code == 200:
  print(colored('Patreon found: '+patreon+tag,'green'))
else:
  print(colored('Patreon not found!!!','red'))
  
  
bit='https://bitbucket.org/'
x=requests.get(bit+tag)
if x.status_code == 200:
  print(colored('Bitbucket found: '+bit+tag,'green'))
else:
  print(colored('Bitbucket not found!!!','red'))
  
  
daily='https://www.dailymotion.com/'
x=requests.get(daily+tag)
if x.status_code == 200:
  print(colored('Dailymotion found: '+daily+tag,'green'))
else:
  print(colored('Dailymotion not found!!!','red'))
  
  
etsy='https://www.etsy.com/shop/'
x=requests.get(etsy+tag)
if x.status_code == 200:
  print(colored('Etsy found: '+etsy+tag,'green'))
else:
  print(colored('Etsy not found!!!','red'))


cash='https://cash.me/'
x=requests.get(cash+tag)
if x.status_code == 200:
  print(colored('Cash found: '+cash+tag,'green'))
else:
  print(colored('Cash not found!!!','red'))


beh='https://www.behance.net/'
x=requests.get(beh+tag)
if x.status_code == 200:
  print(colored('Behance found: '+beh+tag,'green'))
else:
  print(colored('Behance not found!!!','red'))


good='https://www.goodreads.com/'
x= requests.get(good+tag)
if x.status_code == 200:
  print(colored('GoodReads found: '+good+tag,'green'))
else:
  print(colored('GoodReads not found!!!','red'))


ins='https://www.instructables.com/member/'
x=requests.get(ins+tag)
if x.status_code == 200:
  print(colored('Instructables found: '+ins+tag,'green'))
else:
  print(colored('Instructables not found!!!','red'))


keybase='https://keybase.io/'
x=requests.get(keybase+tag)
if x.status_code == 200:
  print(colored('Keybase found: '+keybase+tag,'green'))
else:
  print(colored('Keybase not found!!!','red'))
  
  
kong='https://kongregate.com/accounts/'
x=requests.get(kong+tag)
if x.status_code == 200:
  print(colored('Kongregate found: '+kong+tag,'green'))
else:
  print(colored('Kongtegate not found','red'))
  
 
jurnal='.livejournal.com'
x=requests.get('https://'+tag+jurnal)
if x.status_code == 200:
  print(colored('Livejurnal found: https://'+tag+jurnal,'green'))
else:
  print(colored('Livejurnal not found!!!','red'))
  

angel='https://angel.co/'
x=requests.get(angel+tag)
if x.status_code == 200:
  print(colored('Angel found: '+angel+tag,'green'))
else:
  print(colored('Angel not found','red'))
  
  
last='https://last.fm/user/'
x=requests.get(last+tag)
if x.status_code == 200:
  print(colored('LastFm found: '+last+tag,'green'))
else:
  print(colored('LastFm not found','red'))
  
  
drib='https://dribbble.com/'
x=requests.get(drib+tag)
if x.status_code == 200:
  print(colored('Dribble found: '+drib+tag,'green'))
else:
  print(colored('Dribble not found!!!','red'))


codec='https://www.codecademy.com/'
if x.status_code == 200:
  print(colored('Codecademy found: '+codec+tag,'green'))
else:
  print(colored('Codecademy not found!!!','red'))


grav='https://en.gravatar.com/'
x=requests.get(grav+tag)
if x.status_code == 200:
  print(colored('Gravatar found: '+grav+tag,'green'))
else:
  print(colored('Gravatar not found!!!','red'))


pastebin='https://pastebin.com/u/'
x=requests.get(pastebin+tag)
if x.status_code == 200:
  print(colored('Pastebin found: '+pastebin+tag,'green'))
else:
  print(colored('Pastebin not found!!!','red'))


four='https://foursquare.com/'
x=requests.get(four+tag)
if x.status_code == 200:
  print(colored('FourSquare found: '+four+tag,'green'))
else:
  print(colored('FourSquare not found!!!','red'))
  

rob='https://www.roblox.com/user.aspx?username='
x=requests.get(rob+tag)
if x.status_code == 200:
  print(colored('Roblox found: '+rob+tag,'green'))
else:
  print(colored('Roblox not found!!!','red'))


gum='https://www.gumroad.com/'
x=requests.get(gum+tag)
if x.status_code == 200:
  print(colored('Gumroad found: '+gum+tag,'green'))
else:
  print(colored('Gumroad not found','red'))

wat='https://www.wattpad.com/user/'
x=requests.get(wat+tag)
if x.status_code == 200:
  print(colored('Wattpad found: '+wat+tag,'green'))
else:
  print(colored('Wattpad not found!!!','red'))


canva='https://www.canva.com/'
x=requests.get(canva+tag)
if x.status_code == 200:
  print(colored('Canva found: '+canva+tag,'green'))
else:
  print(colored('Canva not found!!!','red'))


cre='https://creativemarket.com/'
x=requests.get(cre+tag)
if x.status_code == 200:
  print(colored('Creativemarket found: '+cre+tag,'green'))
else:
  print(colored('Creativemarket not found!!!','red'))


track='https://www.trakt.tv/users/'
x=requests.get(track+tag)
if x.status_code == 200:
  print(colored('TrackTv found: '+track+tag,'green'))
else:
  print(colored('TrackTv not found!!!','red'))