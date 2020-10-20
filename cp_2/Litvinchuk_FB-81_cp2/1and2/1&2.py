#форматування тексту
import re
text = open('text.txt','r',encoding='utf8')
ftext = open('ftext.txt','w',encoding='utf8')

temp = ''

for line in text:
	line = re.sub(r"[^a-zA-Z]+"," ",line)
	newline = line.replace(' ','')
	temp += newline

temp = temp.upper()
#temp - відредагований ВТ
ftext.write(temp)
text.close()
ftext.close()


#cтворюю словник для всіх символів
def form_dict():
	d={}
	iter=0
	for i in range(65,91):
		d[iter]=chr(i)
		iter=iter+1
	return d

key = 'EABCQDPFHGMDBGFCFWXN'  #визначаю ключ, яким буде відбуватись шифрування

#форматування тексту, де кожній літері співставляється деяке число
def encode_val(t):
	res=[]
	lent=len(t)
	d=form_dict()
	for w in range(lent):
		for value in d:
			if t[w]==d[value]:
				res.append(value)
	return res

#з'єдную ВТ і ключ в одному словнику
def comparator(value,key):
	lk=len(key)
	dic={}
	iter=0
	f=0
	for i in value:
		dic[f]=[i,key[iter]]
		f+=1
		iter+=1
		if(iter>=lk):
			iter=0
	return dic

#перетворює ВТ у ШТ але у числовому форматі
def full_encode(value,key):
	dic=comparator(value,key)
	lis=[]
	d=form_dict()
	for v in dic:
		go=((dic[v][0]+dic[v][1]) % len(d))
		lis.append(go)
	return lis

#числа переходять у символи
def decode_val(t):
	res=[]
	lent=len(t)
	d=form_dict()
	for w in range(lent):
		for value in d:
			if t[w]==value:
				res.append(d[value])
	return res

ST = ''.join(decode_val(full_encode(encode_val(temp),encode_val(key)))) #ШТ

count=0
def count_each_letter(t):
	qa_letters = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0,
              'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0,
              'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 
              'Y':0, 'Z':0} 
	for symbol in t:
		global count
		count += 1
		qa_letters[symbol] += 1
	return qa_letters

def index_v(text):
	qa=count_each_letter(text)
	index = 0
	for item, value in qa.items():
		value = int(value)
		index+= value*(value-1)
	index = index*(1/(count*(count-1)))
	return index

ID = index_v(ST)


r = open('results.txt','a',encoding='utf8')
r.write("KEY LENGTH: "+str(len(key))+'\n')
r.write("CHIPHER TEXT INDEX: "+str(ID)+'\n')
r.write('CHIPHER TEXT: '+ST+'\n\n\n')
