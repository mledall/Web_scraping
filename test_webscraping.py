# We will follow the tutorial at https://blog.miguelgrinberg.com/post/easy-web-scraping-with-python

# use the 'requests package' http://docs.python-requests.org/en/master/user/quickstart/
import requests
import bs4
#use beautiful soup: https://www.crummy.com/software/BeautifulSoup/
from bs4 import BeautifulSoup

import pandas as pd
import time

URL= 'https://arxiv.org/'

def web_page(link):
	page = requests.get(link)
	print(page.url)				# gets the page URL
	print(page.status_code)		# I don't remember what the status code is
	print (page.text)			# gets the html text

#web_page(URL)

# In order to parse through the text, we want to clean the text which is done using the beautiful soup library.

def parser(link):
	page = requests.get(link)
	page_text = page.text
	page_htmlcode = BeautifulSoup(page_text, 'html.parser')	# Allows to treat the text as html code, rather than just a long string.
	page_htmlcode_clean = page_htmlcode.prettify()			# formats the html code in a more structured way for easier reading.
	return page_htmlcode

def writing_html(URL, name = 'test_html.txt'):
	html_code = parser(URL)
	with open(name, 'w') as f:
		f.write(html_code)
	print("Wrote submission to file {}.".format(name))

# parser(URL).children Gives the hierarchical structure of tags in the html, https://www.dataquest.io/blog/web-scraping-tutorial-python//


def navigate_through_page():	# This function will navigate through the page using the children method, which allows to go down or up levels in the tag hierarchy.
	tags = [type(item) for item in list(parser(URL).children)]	# Gives all the types of items found in the html code. The tag 'tag' is the most important, as it allows us to navigate through the html content.
	html_tag = list(parser(URL).children)[4]	# Select the html tag in the html code, which will allow us to deal with the page content
	[type(item) for item in list(html_tag.children)]	# This gives the two types of content in the children of the html. There is the 'head' and there is the 'body'. The body gives the interesting content of the page. This is what we want.
	html_body = list(html_tag.children)[3]	# Selects the body of the html page
	div = list(html_body.children)[7]
	print list(div.children)[7:][0::4]


# The above function is fine to navigate up and down the ladder of tags in the html page. There is a simpler method to obtain all content under a specific tag at once.


# This is a command I am adding for the sake of demonstrating I can edit a cloned repository



def arxiv_fields():	# This function will enumerate all fields covered by arxiv
	page = requests.get(URL)
	soup = BeautifulSoup(page.content, 'html.parser')	# You can prettify this soup.prettify()
	fields = [soup.find_all('h2')[i].get_text() for i in range(len(soup.find_all('h2')))]
	first_field = soup.find('h2')	# the .find() method returns the first instance of a specific field.
	print fields, first_field


arxiv_fields()



# The command soup.select(URL) allows to select specific text from the URL. Here, we are going to try to get a list of all subjects covered by arxiv.




























