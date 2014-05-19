from http.client import HTTPConnection

conn = HTTPConnection("192.168.1.105")
conn.request("GET", "/videostream.cgi?user=pi&pwd=pi")
r1 = conn.getresponse()
print (r1.status, r1.reason)
print (r1.getheaders)
data1 = r1.read(18987)
#print(data1)
conn.request("GET", "/parrot.spam")
r2 = conn.getresponse()

print (r2.status, r2.reason)
data2 = r2.read()
conn.close()
