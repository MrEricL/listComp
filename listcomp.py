def goodPass (password):
	up = [x for x in password if x.isupper()]
	low = [x for x in password if x.islower()]
	num = [x for x in password if x.isdigit()]

	if (len(up) > 0 and len(low) > 0 and len(num) > 0):
		print password + " is a good password"
	else:
		print password + " is a bad password"


goodPass("abc")
goodPass("aBc")
goodPass("aBc123")

def passStr(password):
	up = [x for x in password if x.isupper()]
	low = [x for x in password if x.islower()]
	num = [x for x in password if x.isdigit()]
	alphn = [x for x in password if not x.isalnum()]
	vary = 0
	if (len(up) > 0):
		vary+=26
	if (len(low) > 0):
		vary+=26
	if (len(num) > 0):
		vary+=10
	if (len(alphn) > 0):
		vary+=18

	#assuming 0.0017 milliseconds to hash
	time = (1.7*(10**-6)) * (vary**len(password)) * 0.5 
	#sec -> days to crack
	time = time/86400 
	#normalizes time w/ max 100 years
	score = (10) * (time/(36500)) 

	if score > 10:
		score = 10

	print score

passStr("7aB$c1xG")
passStr("6:7D8<}TZS>#I6e")
passStr("9)kzR6;FI.07v0N")
passStr("as*iA'6]%7n)XN0")