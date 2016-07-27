import urllib.request

req = urllib.request.Request('http://www.cnn.com')
with urllib.request.urlopen(req) as response:
   the_page = response.read()

   print (the_page)
