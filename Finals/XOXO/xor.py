#find key
import codecs
with open('xoxo.png', 'rb') as f:
	h = f.read().hex()
	k=['89','50','4E','47','0D','0A','1A','0A'];ss='';st=''
	for y in k:
		q=chr(int(y,16))
		ss=ss+q
	for c in range(0,len(h),2):
		s=h[c]+h[c+1]
		st=st+chr(int(s,16))
	key=''.join([chr(ord(a) ^ ord(b)) for a,b in zip(st, ss)])
	print(key)

#to retrieve image

a=[];
key=bytes(key,'utf-8')
h =codecs.decode(h,"hex")
for i in range(0,len(h)):
	a.append(h[i]^key[i % len(key)])
with open('f.png', 'wb') as m:
	m.write(bytes(a))
	

