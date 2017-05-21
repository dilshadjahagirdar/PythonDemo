import re
import urllib.request
city = input("enter your city : ")
url = "http://www.weather-forecast.com/locations/"+city+"/forecasts/latest"
data = urllib.request.urlopen(url).read()
data1=data.decode("utf-8")
m =re.search('span class="phrase">',data1)
start = m.start()+19
end = start+ 350
newstring = data1[start:end]
m = re.search("</span>",newstring)
end = m.start()-2
final = newstring[0:end]
print("================================================================")
print(final)
