import random

def acakkata(): # list kata
	katakata = ['mutlak',
			'benar',
			'terserap',
			'menonjolkan',
			'aktivis',
			'sebenarnya',
			'aktualitas',
			'remaja',
			'mempengaruhi',
			'terpengaruh',
			'udara',
			'waspada',
			'sepanjangwaktu',
			'mengalegorisasikan',
			'persekutuan',
			'aliansi',
			'kiasan',
			'sindiran',
			'baik',
			'samasekali',
			'memperkuat',
			'analisis',
			'semu',
			'tampaknya',
			'penampilan',
			'menangkap',
			'menilai',
			'penilaian',
			'anggapan',
			'astronomis',
			'sikap',
			'rata-rata',
			'sadar',
			'kesadaran',
			'bayi',
			'padadasarnya',
			'tongkat',
			'kepercayaan',
			'keyakinan',
			'besar',
			'darah',
			'berbasisluas',
			'tanpahenti',
			'pusat',
			'bersertifikat',
			'nyanyian',
			'klaim',
			'rahasia',
			'memikirkan',
			'tanggungjawab',
			'komentar',
			'komentator',
			'lengkap',
			'samasekali',
			'memahami',
			'terpadu',
			'curhat',
			'dugaan',
			'hatinurani',
			'kesadaran',
			'besar',
			'sangat']	
	kataterpilih = random.choice(katakata)
	return kataterpilih

def cektebakan(parsekata,huruftebakan=None): # cek apakan huruf ada di kata
	if huruftebakan in parsekata:
		return True
	else:
		return False

def hitunginput(huruftebakan): # menghitung jumlah input tebakan
	count = 0
	for i in huruftebakan:
	  	count += 1
	return count

def progresskata(parsekata,progress,huruftebakan=None): # fungsi tebak per 1 kata
	if progress == None: # jika game baru di mulai progress masih * semua
		progress = []
		for i in parsekata:
			progress.append('*')

	for i in (i for i,x in enumerate(parsekata) if x == huruftebakan):
		progress[i] = str(huruftebakan) # ubah * jd huruf

	return progress

def tebaklangsung(parsekata,huruftebakan): # fungsi tebakan langsung
	kata = ''.join(parsekata)
	tebak = ''.join(huruftebakan)

	if kata == tebak:
		return True
	else:
		return False

def cekselesai(progress): # cek progress kata yang di tebak
	ada = -1
	for i in (i for i,x in enumerate(progress) if x == '*'):
		ada = i

	if ada != -1:
		return True
	else:
		return False

def join(kata): # menggabungkan isi list
	kata = ' '.join(kata)
	return kata

def sudahdipilih(baghuruf,pilihan): # fungsi cek huruf pernah dipilih
	ada = -1
	for i in (i for i,x in enumerate(baghuruf) if x == pilihan):
		ada = i

	if ada != -1:
		return True
	else:
		return False

def main():
	kata = acakkata()
	parsekata = list(kata)
	panjangkata = len(parsekata)
	progress = None
	tertebak = False
	telahdipilih = []
	
	# print(parsekata)
	print('Selamat datang pada GAME TEBAK KATA.')

	langkah = 0
	while not tertebak:
		print('Kata berisi %d huruf, ' % panjangkata, end='')
		huruftebakan = input('silahkan tebak 1 huruf: ')

		jmltebakan = hitunginput(huruftebakan)
		if jmltebakan == 1: # jika input hanya 1 huruf
			# S: cek huruf sudah pernah di pilih
			cektlhdipilih = sudahdipilih(telahdipilih,huruftebakan)
			if cektlhdipilih:
				print('Anda sudah menebak hurur %s sebelumnya.' % huruftebakan)
				print(join(progress))
				continue # lansung langkah berikutnya
			else:
				telahdipilih.append(huruftebakan)
			# E: cek huruf sudah pernah di pilih

			# S: cek jika huruf tebakan ada dalam kata
			cekada = cektebakan(parsekata,huruftebakan)
			if cekada:
				progress = progresskata(parsekata,progress,huruftebakan)
				print(join(progress))
			else:
				print('Tidak mengandung huruf ', huruftebakan)
				print(join(progress))
			# E: cek jika huruf tebakan ada dalam kata

			# S: cek jika huruf sudah berhasil tertebak
			selesai = cekselesai(progress)
			if not selesai:
				print('Selamat Anda berhasil!!!')
				print('Kata ''%s'' tertebak dalam %d langkah.' % (join(parsekata),langkah))
				tertebak = True
			# E: cek jika huruf sudah berhasil tertebak
		else: # jika input lebih dari 1 huruf
			if jmltebakan == 0: # tidak ada input
				print('Tidak ada input, masukkna satu huruf.')
				print(join(progress))
			else: # input lebih dari satu, tebakan langsung
				langsung = tebaklangsung(parsekata,huruftebakan)
				if langsung == True: # jika tebakan langsung benar
					print('Selamat tebakan langsung anda berhasil!!!')
					print('Kata ''%s'' tertebak dalam %d langkah.' % (join(parsekata),langkah))
					tertebak = True
				else: # tebakan langsung salah
					print('Tebakan langsung anda belum tepat.')
					print(join(progress))
		langkah += 1

main()