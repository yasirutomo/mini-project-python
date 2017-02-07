import random

def randnumber():
	number = random.randint(1,100)
	return number

def userinput():
	putar = True
	while putar:
		guest = input('Masukkan angka tebakan: ')
		try:
	   		number = int(guest)
		except ValueError:
		    print('Input harus berupa angka')
		else:
		    return int(guest)
		    putar = False

def main():
	tebak = True
	number = randnumber()
	angkauser = userinput()
	num_tebak = 0
	while tebak:
		num_tebak += 1
		if (angkauser==number):
			print('Tebakan benar, angkanya adalah', number)
			print('Tertebak dalam %d tebakan' % num_tebak)
			tebak = False
		elif (angkauser<number):
			print('Angka terlalu kecil')
			angkauser = userinput()
		else:
			print('Angka terlalu besar')
			angkauser = userinput()
	print('Terimakasih sudah bermain')

main()