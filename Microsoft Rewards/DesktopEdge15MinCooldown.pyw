#Search bot adjusted for timer; 5 seconds per search, 15 minutes per 4 searches
#Make sure that you are already signed in to Edge

import webbrowser
import time
import os
import random

edge_path = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'
webbrowser.register('microsoft-edge', None, webbrowser.BackgroundBrowser(edge_path))
browser = 'microsoft-edge'


urls = ['https://www.bing.com/search?q=meatloaf+recipes&qs=SC&pq=meatloaf+reciepes&sc=10-17&cvid=B2AAABEECCFD4BA3A24FF8C156077A03&FORM=QBLH&sp=1&ghc=1&lq=0','https://www.bing.com/search?q=latest+currency+conversion&form=QBLH&sp=-1&ghc=2&lq=0&pq=latest+currency+conversion&sc=11-26&qs=n&sk=&cvid=3883A8D8B92241D6ABC969A819862B44&ghsh=0&ghacc=0&ghpl=','https://www.bing.com/search?q=Wendys&form=QBLH&sp=-1&ghc=1&lq=0&pq=wendys&sc=11-6&qs=n&sk=&cvid=5E9EEEDCC06340EDAAE63DD3B2054685&ghsh=0&ghacc=0&ghpl=','https://www.bing.com/search?q=houses+for+sale+northwest+houston&form=QBLH&sp=-1&ghc=1&lq=0&pq=houses+for+sale+northwest+houston&sc=11-33&qs=n&sk=&cvid=ACE290EDE1F84D6389B150C286E7F464&ghsh=0&ghacc=0&ghpl=','https://www.bing.com/search?q=Xbox+account+not+connecting+to+modern+warfare+3+online+services&form=QBLH&sp=-1&ghc=1&lq=0&pq=xbox+account+not+connecting+to+modern+warfare+3+online+services&sc=7-63&qs=n&sk=&cvid=63FF8F9D22A947BDBAE1176127C55A25&ghsh=0&ghacc=0&ghpl=','https://www.bing.com/search?q=flush%20dns%20cmd&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=flush%20dns%20cmd&sc=10-13&sk=&cvid=46A44183F70E447AABE02513EF9C9261&ghsh=0&ghacc=0&ghpl=','https://www.bing.com/search?q=my+router%27s+home+page&form=ANSPH1&refig=953d74a076e246519b246fbd91a3f998&pc=U531','https://www.bing.com/search?q=shopping+list&filters=ufn%3a%22Shopping+list%22+sid%3a%2201a608d5-f6eb-6dcf-8ff8-261622e26a12%22&asbe=SC&qs=MB&pq=shoppimg+li&sc=10-11&cvid=8FEA1C1E165E482AB384F8724DB73441&FORM=QBRE&sp=1&ghc=1&lq=0','https://www.bing.com/search?q=delta+air+lines+tickets+&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=delta+air+lines+ticke&sc=11-21&sk=&cvid=EF1DEAF66DD24BCF97E0C063D507465D&ghsh=0&ghacc=0&ghpl=','https://www.bing.com/search?q=+restaurants+near+me&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=+restaurants+near+me&sc=11-20&sk=&cvid=4C94873A159D45B79B5038DE6CBB72ED&ghsh=0&ghacc=0&ghpl=','https://www.bing.com/search?q=247910f&qs=n&form=QBRE&sp=-1&lq=0&pq=247910f&sc=11-7&sk=&cvid=737872AA7FA24A6B8CB0746CDEE2E941&ghsh=0&ghacc=0&ghpl=','https://www.bing.com/search?q=wsvn&filters=ufn%3a%22WSVN%22+sid%3a%22a6768f39-b394-abe6-4dc5-c50900e0527e%22&asbe=SC&qs=MB&pq=wsnnj&sc=10-5&cvid=3B2DE1A9725E45898B58C1017561C666&FORM=QBRE&sp=1&ghc=1&lq=0',
'https://www.bing.com/search?q=yandex&filters=ufn%3a%22Yandex%22+sid%3a%22d4091904-caea-4b11-459a-00c59487110f%22&asbe=SC&qs=MB&pq=ynfx&sk=LT1&sc=10-4&cvid=2BC6D9F59D9F40D9BC404BEC6B910CB8&FORM=QBRE&sp=2&ghc=1&lq=0',
'https://www.bing.com/search?q=eggs&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=egg&sc=11-3&sk=&cvid=4787320CEAA042E88649E95A4F39FB0E&ghsh=0&ghacc=0&ghpl=','https://www.bing.com/search?q=efrr&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=efrr&sc=11-4&sk=&cvid=488337FC395A487196358D52F8FBEEAB&ghsh=0&ghacc=0&ghpl=','https://www.bing.com/search?q=stock+market+today&qs=LS&pq=stock+m&sc=10-7&cvid=29F87A7E1BEC45D588202DD143618363&FORM=QBLH&sp=1&ghc=1&lq=0','https://www.bing.com/search?q=cost+of+living+austin+tx&form=ANSPH1&refig=B888142C39284CE78E7F07D57AA78D3B&pc=U531&sp=1&lq=0&qs=AS&pq=cost+of+living+austin&sc=10-21&cvid=b888142c39284ce78e7f07d57aa78d3b', 'https://www.bing.com/search?q=bulking+and+cutting&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=bulking+and+cutting&sc=11-19&sk=&cvid=7E8DDD1FADD84B8FA8127D40DE29DD74&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=efrreftssdr&qs=n&form=QBRE&sp=-1&lq=0&pq=efrreftssdr&sc=0-11&sk=&cvid=F894535A23A6402DAEFC95C4776556A4&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=y&form=ANSPH1&refig=3558ad494abb47069e8cae963e3d169a&pc=U531',
'https://www.bing.com/search?q=texans+next+game&form=QBLH&sp=-1&ghc=1&lq=0&pq=texans+next+game&sc=9-16&qs=n&sk=&cvid=2CFE78ECFF5144589E813D1131A62831&ghsh=0&ghacc=0&ghpl=', 
'https://www.bing.com/search?q=ev+charging+stations+near+me&qs=LS&pq=ev+charging+statio&sk=LS1&sc=10-18&cvid=0944B6D7DFC14C5C9D11152ABE294123&FORM=QBRE&sp=2&ghc=1&lq=0',
'https://www.bing.com/search?q=rockets+roster&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=rockets+roster&sc=11-14&sk=&cvid=111391EC1CDC498BB05A965764DE589F&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=y4%24%24&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=y4%24%24&sc=11-4&sk=&cvid=61046AC83844456F872F370FD0C29386&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=software+engineering+no+experience&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=software+engineering+no+experience&sc=11-34&sk=&cvid=3EE6264CD947454EAA53A892C12BF7C8&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=tired+of+upper+lower+split&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=tired+of+upper+lower+split&sc=11-26&sk=&cvid=0DBB3E113902459AA26D15FCEC50695C&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=4+day+high+frequency+split&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=4+day+high+frequency+split&sc=11-26&sk=&cvid=C1DA6E7A4790437DA7559873C35733C1&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=steam+most+played&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=steam+most+played&sc=11-17&sk=&cvid=804BA229F2DA4078B86C546777AD6D62&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=xbox+most+played&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=xbox+most+played&sc=11-16&sk=&cvid=0C30D3A1C46C46CC8CEA58D674D24F9B&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=playstation+most+played&qs=n&form=QBRE&sp=-1&lq=0&pq=playstation+most+played&sc=8-23&sk=&cvid=46F669C460E44341B1C99E4BD02C5518&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=y4%24%24%23rgf&qs=n&form=QBRE&sp=-1&lq=0&pq=y4%24%24%23rgf&sc=11-8&sk=&cvid=86418008C27C41D1801DF65F72EF27C9&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=volta+fast+charging&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=volta+fast+charging&sc=10-19&sk=&cvid=475CFE65724D4E659D62E67BFE7BEDDE&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=german+shepherd+average+life+span&qs=MT&pq=german+shepherd+averag&sk=AS1&sc=10-22&cvid=4F022D871BFA446FB84A81442902F507&FORM=QBRE&sp=2&ghc=1&lq=0',
'https://www.bing.com/search?q=Logitech+POP+Keys+Mechanical+Wireless+Keyboard+With+Customizable+Emoji+%2c+Durable+Compact+Design%2c+Bluetooth+Or+USB+Connectivity%2c+Multi-Device%2c+OS+Comp&FORM=HDRSC1',
'https://www.bing.com/search?q=logitech+pop+mechanical+keyboard+review&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=logitech+pop+mechanical+keyboard+review&sc=11-39&sk=&cvid=4361A1A2CD4D407FB4442D0C93FFA702&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=options+settle+time&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=options+settle+time&sc=11-19&sk=&cvid=ABEDA9E7CF4E486FA22473BDAA01DA2F&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=how+many+skill+magazines+are+in+starfield&qs=UT&pq=how+many+skill+ma&sc=10-17&cvid=87A8FA6FEFFA428E9E34794D4C837923&FORM=QBRE&sp=1&ghc=1&lq=0',
'https://www.bing.com/search?q=nfl+playoff+picture&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=nfl+playoff+picture&sc=11-19&sk=&cvid=87B46F59605B41608B7D4357282D3D74&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=wolf+dog&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=wolf+dog&sc=11-8&sk=&cvid=DE45291A316F4E4AA8DFA4017CB8579F&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=top+selling+albums+of+the+year&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=top+selling+albums+of+the+year&sc=11-30&sk=&cvid=F45E3A9B96E54BACACFED9C42809E620&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=top+selling+rap+album&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=top+selling+rap+album&sc=11-21&sk=&cvid=205DB1F6C0554123A02223D83805AABF&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=current+presidential+polls&qs=LS&pq=current+preside&sc=10-15&cvid=1676B455580E4252831FD55772553C0B&FORM=QBRE&sp=1&ghc=1&lq=0',
'https://www.bing.com/search?q=metacritic&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=metacritic&sc=11-10&sk=&cvid=10E4294AC52F40309EB05EBC867C8CF7&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=slickdeals&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=slickdeals&sc=11-10&sk=&cvid=2BEFD3BCF9B145C8B0A97A16CD785E2A&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=youtube&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=youtube&sc=11-7&sk=&cvid=0838B916048744B2A029B62FEB087F49&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=this+week%27s+weather&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=this+week%27s+weather&sc=11-19&sk=&cvid=EF4DEA65DA2D464B882DD23544C9EE8B&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=year+of+the+backup+quarterback&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=year+of+the+backup+quarterbac&sc=2-29&sk=&cvid=974ED0C87D9A4D9998D25E94544A48DA&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=foobar2000&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=foobar2000&sc=11-10&sk=&cvid=2073D5AA9D1F4FCFA213BFE3C8DF72EB&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=average+life+expectancy&qs=LS&pq=average+life&sc=10-12&cvid=3688528C6D98493AA29E306A55503310&FORM=QBRE&sp=1&ghc=1&lq=0',
'https://www.bing.com/search?q=best+bootcamps+for+coding&qs=AS&pq=best+bootcam&sk=LS1&sc=10-12&cvid=1A050826E68245E9BAB4C575FC2BD3A0&FORM=QBRE&sp=2&ghc=1&lq=0',
'https://www.bing.com/search?q=ai+stock+trading&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=ai+stock+trading&sc=11-16&sk=&cvid=C0C6F14E442D4714B2EB108CB615A0B8&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=+4+or+5+day+splits&form=QBLH&sp=-1&ghc=1&lq=0&pq=+4+or+5+day+splits&sc=11-18&qs=n&sk=&cvid=33CBB1B16B8747D2946938C6245913BE&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=23&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=23&sc=10-2&sk=&cvid=346ABD8D2C9549159C3DF8F2318FEF76&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=24&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=24&sc=10-2&sk=&cvid=18D97D0DFE584D72A4D67D86B3B5AF04&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=247&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=247&sc=10-3&sk=&cvid=F263D47A5B6A4F869C15FBFB7D2543C7&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=2479&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=2479&sc=10-4&sk=&cvid=DACBF7DF308D40B0ABF8D96FB5C9BC99&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=247910&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=247910&sc=10-6&sk=&cvid=DD56DE4BE76C45DD9E2D5206F1953447&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=hggdddd&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=hggdddd&sc=10-7&sk=&cvid=9CF7D838339047988588493BA5B8B260&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=hggddddf&qs=n&form=QBRE&sp=-1&lq=0&pq=hggddddf&sc=10-8&sk=&cvid=0A45974EE87F4303B3D2ACFFEDF6846F&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=ffdgd&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=ffdgd&sc=10-5&sk=&cvid=4A7685EBD1E545CCAEC51CF51BEBD694&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=fgrrrrr&qs=n&form=QBRE&sp=-1&ghc=2&lq=0&pq=fgrrrrr&sc=10-7&sk=&cvid=81B20C12E5064B038D78A7C0098A55E6&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=fgrrrrrsass&qs=n&form=QBRE&sp=-1&lq=0&pq=fgrrrrrsass&sc=0-11&sk=&cvid=ECBC0994222A4C37A63DDE4E7C50EBE6&ghsh=0&ghacc=0&ghpl=', 'https://www.bing.com/news/search?q=modern+warfare+iii+cannot+sign+in&qs=n&form=QBNT&sp=-1&ghc=1&lq=0&pq=modern+warfare+iii+cannot+sign+in&sc=10-33&sk=&cvid=5B9E0706EECC4A03B25A5763E6312951&ghsh=0&ghacc=0&ghpl='
]

# Shuffles URLs to make the searches less predictable
random.shuffle(urls)


# Opens URLs with a 6 second delay. After 4 searches, a 15 minute cooldown takes place.
for i in range(len(urls)):
    webbrowser.get(browser).open(urls[i], new=0)
    if (i+1)%4==0:
        time.sleep(901) # 15 minutes
    else:
        time.sleep(6)
#os.system("shutdown /s /t 1") 