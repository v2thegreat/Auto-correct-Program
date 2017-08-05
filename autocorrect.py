Correct_Word_List=['hi','this','is','a','sentence']		#Or open("Correct Words.txt").readlines()
def get_sent_token(sentence):
	return sentence.split('.')
def get_Incorrect_Words(sentence):
	word_lst=[]
	temp=[x.split() for x in get_sent_token(sentence)]
	for x in temp:
		word_lst+=x
	incorrect_Words_Lst=[]
	for x in word_lst:
		if x.lower() not in Correct_Word_List:
			incorrect_Words_Lst.append(x)
	return incorrect_Words_Lst
def get_Incorrect_Words_Position(sentence):
	Incorrect_Words_Position=[]
	for x in get_Incorrect_Words(sentence):
		Incorrect_Words_Position.append(sentence.index(x))
	return Incorrect_Words_Position
def get_Incorrect_Sent_Upper(sentence):
	i=0
	s=''
	for x in range(len(sentence)):
		if i>=len(sentence):
			break
		elif i in get_Incorrect_Words_Position(sentence):
			s+=sentence[i:i+len(get_Incorrect_Words(sentence)[get_Incorrect_Words_Position(sentence).index(i)])].upper()
			i+=len(get_Incorrect_Words(sentence)[get_Incorrect_Words_Position(sentence).index(i)])
		else:
			s+=sentence[i]
			i+=1
	return s
def is_Likely_To_Be_Correct(Incorrect_Word,Possible_Word):
	ch1 = float(len(Incorrect_Word))/float(len(Possible_Word))<1.5 and len(Incorrect_Word)/len(Possible_Word)>0.5
	ch2 = [True if Incorrect_Word[x].lower()==Possible_Word[x].lower() else False for x in range(min(len(Incorrect_Word),len(Possible_Word)))].count(True)>=(min(len(Incorrect_Word),len(Possible_Word)))/2
	return (ch1 and ch2)
def get_Suggestions(sentence):
	d={}
	for x in get_Incorrect_Words(sentence):
		d[x]=[]
		for i in Correct_Word_List:
			if is_Likely_To_Be_Correct(x,i):
				d[x].append(i)
	return d
def main():
	l="Hi. Ths is a sentence."
	print(get_Incorrect_Sent_Upper(l))
	for x in get_Suggestions(l):
		print (get_Suggestions(l)[x])

if __name__ == '__main__':
	main()