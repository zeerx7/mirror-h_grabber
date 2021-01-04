import requests, re, time, urlparse
class pausi:
    def banner(self):
        print '''
        _                                 
  /\/\ (_)_ __ _ __ ___  _ __       /\  /\\
 /    \| | '__| '__/ _ \| '__|____ / /_/ /
/ /\/\ \ | |  | | | (_) | | |_____/ __  / 
\/    \/_|_|  |_|  \___/|_|       \/ /_/                               
   ___           _     _                  
  / _ \_ __ __ _| |__ | |__   ___ _ __    
 / /_\/ '__/ _` | '_ \| '_ \ / _ \ '__|   
/ /_\\| | | (_| | |_) | |_) |  __/ |      
\____/|_|  \__,_|_.__/|_.__/ \___|_| 
     Coded by Zeerx7 # XploitSec-ID
     Date: 04 - 01 - 2021
'''
    def __init__(self):
        self.user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:30.0) Gecko/20100101 Firefox/30.0'
	self.End = False
	self.end = '''<th>Attacker</th>
<th>Country</th>
<th>Web URL</th>
<th>IP's</th>
<th>Date</th>
<th>Preview</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
</div>
</div>
</div>
</div>'''
    def get_urls(self, url):
        headers = {
            'User-Agent' : self.user_agent
        }
        req = requests.get(url, headers=headers)
        if req.status_code == 200:
            if re.search('title>Attention Required! | Cloudflare</title>', req.text):
                print "Cloudflare :: Attention Required!"
	    elif re.search(self.end, req.text):
		self.End = True
            else:
                r = re.findall('break-word;white-space: normal;min-width: 300px;"><a href="(.+?)">(.+?)</a></td>', req.text)
                if r:
                    for dom in r:
                        try:
                            dom = dom[1]
                            dom = dom.replace('http//', 'http://')
                            dom = dom.replace('https//', 'https://')
                            if not re.search('http(s)?://', dom):dom = 'http://'+dom
                            domain = urlparse.urlparse(dom)
                            print domain.netloc
                            try:open(self.savefile, 'a').write(domain.netloc+'\n')
                            except:pass
                        except:
                            pass
    def start(self, id):
        try:
            url = 'https://mirror-h.org/search/hacker/'
            for i in range(1, 9999999):
		if self.End == True:
			print 'Done.'
			break
		else:
	                u = url+str(id)+'/pages/'+str(i)
        	        print '\n'+u
                	self.get_urls(u)
	                time.sleep(1)
        except:
            print "Error!"
    def main(self):
        self.banner()
        try:
            id_hacker = input('id hacker[ex: 5010] :: ')
            self.savefile = raw_input('Save filename[ex: domain.txt] :: ')
            self.start(id_hacker)
        except:
            print "Error!!"
pausi().main()
