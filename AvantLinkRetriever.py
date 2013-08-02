'''
  widget to retrieve merchant data from Avantlink
  potentially other Affiliate Marketers as well. 
  must use links from Avantlink API Builder 

'''
# import py libraries 
import urllib2 
import re

# BeautifulSoup used to parse XML
from BeautifulSoup import BeautifulStoneSoup

print 'Please input link here' 
link = raw_input('> ')

####################################################

print '\n'

####################################################

# opens initial link inputted
response1 = urllib2.urlopen(link)
# pulls down data from the API 
data = response1.read()
xml = data 

# parses the XML doc in search for downloadlink
soup = BeautifulStoneSoup(xml)
downloadlink = soup.response.subscription_url
url = downloadlink.string 

# regex used to replace "amp;" with empty string 
# this authorizes download of data
url = (re.sub('amp;', '', url))

print 'This is the new [authorized] URL that the data will download from: '
print '\n'
print url
print '\n'
print 'NOTE: There might be lag! Give it a second.'
print '\n'
print 'What would you like to call this textfile?'
filename = raw_input('> ')

####################################################

print '\n'

####################################################

# this now reads the newly edited link
response2 = urllib2.urlopen(url)
data2 = response2.read()

# creates a txt file called "AvantLinkData"
# writes data to "AvantLinkData"
# closes file
f = open(filename, 'w')
f.write(data2)
f.close()

# end




