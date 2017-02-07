cerita = '''
saya merasa {} hari ini,
jika tidak hujan, hari ini saya akan {},
dan pergi ke {} untuk membuat {},
menghabiskan waktu sebelum memesan {}
untuk makan, dan pulang pada {} hari,
untuk melanjutkan dengan {} di rumah
'''

def main():
	keadaan = input('Bagaimana perasaan Anda hari ini? (eg. sehat): ')
	lokasi = input('Masukkan nama tempat? (eg. lapangan/mall): ')
	objek = input('Masukkan kata objek? (eg. PR/Mading/layangan): ')
	makanan = input('Nama makanan yang Anda suka? (eg. coto): ')
	hari = input('Masukkan ungkapan waktu? (eg. pagi/siang/sore/malam): ')

	pekerjaan = []
	pekerjaan.append(input('Masukkan ungkapan kata kerja? (eg. bersepeda): '))
	pekerjaan.append(input('Masukkan ungkapan kata kerja yang biasa dilakukan dirumah? (eg. tidur): '))

	mad_lib = cerita.format(keadaan,
							pekerjaan[0],
							lokasi,
							objek,
							makanan,
							hari,
							pekerjaan[1])
	print(mad_lib)

main()
