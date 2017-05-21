import re
import urllib.request
url = "http://www.dictionary.com/browse/"+input("enter keyword to search : ")
data = urllib.request.urlopen(url).read()
data1=data.decode("utf-8")
m= re.search('meta name="description" content=',data1)
start = m.end()
end = start + 200
newstring = data1[start : end]
m = re.search("See more.",newstring)
if m :
	end = m.start()-1

definition = newstring[0:end]
print(definition)
