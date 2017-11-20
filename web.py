import requests,datetime
from bs4 import BeautifulSoup

import warnings
warnings.filterwarnings('ignore')

open('/home/prateksha/Desktop/IIITB/Web_Scraping/out.txt', 'w').close()
list = []
file = open('/home/prateksha/Desktop/IIITB/Web_Scraping/out.txt','a')


with requests.Session() as session:
	login_url = 'https://lms.iiitb.ac.in/moodle/login/index.php'
	request_url = 'https://lms.iiitb.ac.in/moodle/my/'
	usr = {'username': '''Enter your username''',
	       'password': '''Enter your password'''}
	
	log = session.get(login_url,verify = False)
	login = session.post(login_url,data = usr,verify = False)
	page = session.get(request_url,verify = False)
	final_page = BeautifulSoup(page.content, 'html5lib')
	for div in final_page.find_all('div',{"class":"box coursebox"}):
		if div.find_all('div',{"class":"activity_info"}):		
			list.append('\n' + div.div.h2.a['title'] + '\n')
			for posts in div.find_all('div',{'class':'collapsibleregioncaption'}):
				list.append(posts.text+'\n')
			for forum in div.find_all('span',{'class':'postsincelogin'}):
				list.append("  " + forum.text + '\n')
				
	now = str(datetime.datetime.now())
	list.append('\nDate and Time: '+now+'\n')
	if len(list) == 1:
		list.append("No New Updates")

	else:
		for i in range(len(list)):
			file.write(list[i])		
	
# The cronjob line for running the script every hour.
# 0 * * * * /usr/bin/python /home/prateksha/Desktop/IIITB/Web_Scraping/web.py


