import urllib2




























req=urllib2.Request("http://www.spongeliu.com/")
fd=urllib2.urlopen(req)
print fd.read(10000)
