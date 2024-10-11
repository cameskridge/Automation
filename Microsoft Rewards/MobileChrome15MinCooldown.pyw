# Mobile search emulator for bing mobile points
# Scroll to lines 35 and 43  to replace email and password before running

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium_stealth import stealth
import time
import random

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument('user-agent=Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36')

# Start the WebDriver
service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Android",
        webgl_vendor="Qualcomm",
        renderer="Adreno (TM) 640",
        fix_hairline=True)

driver.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=162&id=264960&wreply=https%3a%2f%2fwww.bing.com%2fsecure%2fPassport.aspx%3fedge_suppress_profile_switch%3d1%26requrl%3dhttps%253a%252f%252fwww.bing.com%252f%253ftoWww%253d1%2526redig%253dE31DBBB3B5FF4734A3E5F6E126803F44%2526wlexpsignin%253d1%26sig%3d261A677568956B431C1F726769F96AD8%26nopa%3d2&wp=MBI_SSL&lc=1033&CSRFToken=f9e34852-581f-4007-b4be-98c440bc25ec&cobrandid=c333cba8-c15c-4458-b082-7c8ce81bee85&aadredir=1&nopa=2')
time.sleep(3)

# Find the email input field, enter email, click next, and wait for the next page to load
email_input = driver.find_element("name", "loginfmt")
email_input.send_keys("ENTER EMAIL")
time.sleep(1)
next_button = driver.find_element("id", "idSIButton9")
next_button.click()

# Wait for page to load, then enter password, press next
time.sleep(2)
passwd_input = driver.find_element("name", "passwd")
passwd_input.send_keys("ENTER PASSWORD")
sign_in_button = driver.find_element("id", "idSIButton9")
sign_in_button.click()


# Wait for page to load, then click the "Sign in" button
time.sleep(1)
yesButton = driver.find_element("id", "acceptButton")
yesButton.click()

# Wait for login to complete, then open URLs
time.sleep(5)

urls = ['https://www.bing.com/search?q=Call+of+Duty+release+date&form=QBLH&sp=-1&ghc=1&lq=0&pq=call+of+duty+release+date&sc=10-25&qs=n&sk=&cvid=B644D7BB2E0642908F054F57DEF441B2&ghsh=0&ghacc=0&ghpl=','https://www.bing.com/search?q=directions+to+niagara+falls&qs=FT&pq=directions&sk=AS1FT1&sc=10-10&cvid=AC9B9A96783E4D079DB699EB3EEC5429&FORM=QBLH&sp=3&ghc=1&lq=0', 'https://www.bing.com/search?q=top+selling+rap+album&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=top+selling+rap+album&sc=11-21&sk=&cvid=205DB1F6C0554123A02223D83805AABF&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=current+presidential+polls&qs=LS&pq=current+preside&sc=10-15&cvid=1676B455580E4252831FD55772553C0B&FORM=QBRE&sp=1&ghc=1&lq=0',
'https://www.bing.com/search?q=meatloaf+recipes&qs=SC&pq=meatloaf+reciepes&sc=10-17&cvid=B2AAABEECCFD4BA3A24FF8C156077A03&FORM=QBLH&sp=1&ghc=1&lq=0', 
'https://www.bing.com/search?q=latest+currency+conversion&form=QBLH&sp=-1&ghc=2&lq=0&pq=latest+currency+conversion&sc=11-26&qs=n&sk=&cvid=3883A8D8B92241D6ABC969A819862B44&ghsh=0&ghacc=0&ghpl=','https://www.bing.com/search?q=Wendys&form=QBLH&sp=-1&ghc=1&lq=0&pq=wendys&sc=11-6&qs=n&sk=&cvid=5E9EEEDCC06340EDAAE63DD3B2054685&ghsh=0&ghacc=0&ghpl=','https://www.bing.com/search?q=houses+for+sale+northwest+houston&form=QBLH&sp=-1&ghc=1&lq=0&pq=houses+for+sale+northwest+houston&sc=11-33&qs=n&sk=&cvid=ACE290EDE1F84D6389B150C286E7F464&ghsh=0&ghacc=0&ghpl=','https://www.bing.com/search?q=Xbox+account+not+connecting+to+modern+warfare+3+online+services&form=QBLH&sp=-1&ghc=1&lq=0&pq=xbox+account+not+connecting+to+modern+warfare+3+online+services&sc=7-63&qs=n&sk=&cvid=63FF8F9D22A947BDBAE1176127C55A25&ghsh=0&ghacc=0&ghpl=','https://www.bing.com/search?q=flush%20dns%20cmd&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=flush%20dns%20cmd&sc=10-13&sk=&cvid=46A44183F70E447AABE02513EF9C9261&ghsh=0&ghacc=0&ghpl=','https://www.bing.com/search?q=my+router%27s+home+page&form=ANSPH1&refig=953d74a076e246519b246fbd91a3f998&pc=U531','https://www.bing.com/search?q=shopping+list&filters=ufn%3a%22Shopping+list%22+sid%3a%2201a608d5-f6eb-6dcf-8ff8-261622e26a12%22&asbe=SC&qs=MB&pq=shoppimg+li&sc=10-11&cvid=8FEA1C1E165E482AB384F8724DB73441&FORM=QBRE&sp=1&ghc=1&lq=0','https://www.bing.com/search?q=delta+air+lines+tickets+&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=delta+air+lines+ticke&sc=11-21&sk=&cvid=EF1DEAF66DD24BCF97E0C063D507465D&ghsh=0&ghacc=0&ghpl=','https://www.bing.com/search?q=+restaurants+near+me&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=+restaurants+near+me&sc=11-20&sk=&cvid=4C94873A159D45B79B5038DE6CBB72ED&ghsh=0&ghacc=0&ghpl=','https://www.bing.com/search?q=247910f&qs=n&form=QBRE&sp=-1&lq=0&pq=247910f&sc=11-7&sk=&cvid=737872AA7FA24A6B8CB0746CDEE2E941&ghsh=0&ghacc=0&ghpl=','https://www.bing.com/search?q=wsvn&filters=ufn%3a%22WSVN%22+sid%3a%22a6768f39-b394-abe6-4dc5-c50900e0527e%22&asbe=SC&qs=MB&pq=wsnnj&sc=10-5&cvid=3B2DE1A9725E45898B58C1017561C666&FORM=QBRE&sp=1&ghc=1&lq=0',
'https://www.bing.com/search?q=eggs&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=egg&sc=11-3&sk=&cvid=4787320CEAA042E88649E95A4F39FB0E&ghsh=0&ghacc=0&ghpl=','https://www.bing.com/search?q=efrr&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=efrr&sc=11-4&sk=&cvid=488337FC395A487196358D52F8FBEEAB&ghsh=0&ghacc=0&ghpl=','https://www.bing.com/search?q=stock+market+today&qs=LS&pq=stock+m&sc=10-7&cvid=29F87A7E1BEC45D588202DD143618363&FORM=QBLH&sp=1&ghc=1&lq=0','https://www.bing.com/search?q=cost+of+living+austin+tx&form=ANSPH1&refig=B888142C39284CE78E7F07D57AA78D3B&pc=U531&sp=1&lq=0&qs=AS&pq=cost+of+living+austin&sc=10-21&cvid=b888142c39284ce78e7f07d57aa78d3b', 'https://www.bing.com/search?q=bulking+and+cutting&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=bulking+and+cutting&sc=11-19&sk=&cvid=7E8DDD1FADD84B8FA8127D40DE29DD74&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=efrreftssdr&qs=n&form=QBRE&sp=-1&lq=0&pq=efrreftssdr&sc=0-11&sk=&cvid=F894535A23A6402DAEFC95C4776556A4&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=y&form=ANSPH1&refig=3558ad494abb47069e8cae963e3d169a&pc=U531',
'https://www.bing.com/search?q=texans+next+game&form=QBLH&sp=-1&ghc=1&lq=0&pq=texans+next+game&sc=9-16&qs=n&sk=&cvid=2CFE78ECFF5144589E813D1131A62831&ghsh=0&ghacc=0&ghpl=', 
'https://www.bing.com/search?q=ev+charging+stations+near+me&qs=LS&pq=ev+charging+statio&sk=LS1&sc=10-18&cvid=0944B6D7DFC14C5C9D11152ABE294123&FORM=QBRE&sp=2&ghc=1&lq=0',
'https://www.bing.com/search?q=rockets+roster&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=rockets+roster&sc=11-14&sk=&cvid=111391EC1CDC498BB05A965764DE589F&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=software+engineering+no+experience&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=software+engineering+no+experience&sc=11-34&sk=&cvid=3EE6264CD947454EAA53A892C12BF7C8&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=tired+of+upper+lower+split&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=tired+of+upper+lower+split&sc=11-26&sk=&cvid=0DBB3E113902459AA26D15FCEC50695C&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=4+day+high+frequency+split&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=4+day+high+frequency+split&sc=11-26&sk=&cvid=C1DA6E7A4790437DA7559873C35733C1&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=steam+most+played&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=steam+most+played&sc=11-17&sk=&cvid=804BA229F2DA4078B86C546777AD6D62&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=xbox+most+played&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=xbox+most+played&sc=11-16&sk=&cvid=0C30D3A1C46C46CC8CEA58D674D24F9B&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=playstation+most+played&qs=n&form=QBRE&sp=-1&lq=0&pq=playstation+most+played&sc=8-23&sk=&cvid=46F669C460E44341B1C99E4BD02C5518&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=volta+fast+charging&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=volta+fast+charging&sc=10-19&sk=&cvid=475CFE65724D4E659D62E67BFE7BEDDE&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=my+user+agent&form=QBLH&sp=-1&ghc=1&lq=0&pq=my+user+agent&sc=10-13&qs=n&sk=&cvid=014E95A9C06848C084D307EED4B407FB&ghsh=0&ghacc=0&ghpl=',
'https://www.bing.com/search?q=hotels&form=QBLH&sp=-1&ghc=1&lq=0&pq=hotels&sc=10-6&qs=n&sk=&cvid=DC589F7F4A944850A8CBC64C86CE8ADA&ghsh=0&ghacc=0&ghpl='
]
#Randomly pick 20 URLs, taking a 15 min break every 4th URL, 6-10 sec otherwise
#Every URL is worth 5 points; only 100 points can be earned per day
#Added many URLs to make search actions less routine

i = 0
random.shuffle(urls)

while (i<21):
    driver.get(urls[i])    
    if ((i+1) % 4 == 0):
        time.sleep(903)
    else:
        time.sleep(random.uniform(6,10))
    i+=1

#Leave browser open for a little bit
time.sleep(10) 

#Close browser
driver.quit()

