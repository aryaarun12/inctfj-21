#to find key:
import codecs
a=[];
with open('xoxo.png', 'rb') as f:
	h = f.read().hex()
	k=['89','50','4E','47','0D','0A','1A','0A'];ss='';aa=[]
	for y in k:
		q=chr(int(y,16))	
		ss=ss+q	
	st=''
	for c in range(0,len(h),2):
		s=h[c]+h[c+1]
		st=st+chr(int(s,16))
	l=[chr(ord(a) ^ ord(b)) for a,b in zip(st, ss)]
	print(''.join(l))  

'''
#repeating xor
import codecs
a=[];key=b'eAsy-x0r'
with open('xoxo.png', 'rb') as f:
	h =f.read()
	for i in range(0,len(h)):
		a.append(h[i]^key[i % len(key)])
with open('f.png', 'wb') as m:
	m.write(bytes(a))
	
'''
