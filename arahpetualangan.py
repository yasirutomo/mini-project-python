import random

def msg(posisi):
	if posisi['msg'] == '':
		return "kau memasuki ruangan " + posisi['nama'] + '.'
	else:
		return posisi['msg']

def pilihan(posisi,dir):
	if dir == 'u':
		pilih = 0
	elif dir == 't':
		pilih = 1
	elif dir == 's':
		pilih = 2
	elif dir == 'b':
		pilih = 3
	else:
		return -1
	# return kearah
	if posisi['arah'][pilih] == 0:
		return 4
	else:
		return pilih

def main():
	arah = (0,0,0,0) # u,t,s,b

	# bikin dictionary tiap ruang
	ruangtamu = {'nama':'Ruang Tamu','arah':arah,'msg':''}
	ruangkeluarga = {'nama':'Ruang Keluarga','arah':arah,'msg':''}
	ruangkerja = {'nama':'Ruang Kerja','arah':arah,'msg':''}
	kamar = {'nama':'kamar','arah':arah,'msg':''}
	ruangmakan = {'nama':'Ruang Makan','arah':arah,'msg':''}
	dapur = {'nama':'Dapur','arah':arah,'msg':''}

	# inisialisasi ruangan U,T,S,B
	ruangtamu['arah'] = (ruangkeluarga,0,0,0)
	ruangkeluarga['arah'] = (0,ruangmakan,ruangtamu,ruangkerja)
	ruangkerja['arah'] = (kamar,ruangkeluarga,0,0)
	kamar['arah'] = (0,0,ruangkerja,0)
	ruangmakan['arah'] = (0,dapur,0,ruangkeluarga)
	dapur['arah'] = (0,0,0,ruangmakan)

	# inisialisasi masuk dari ruang tamu
	ruangan = [ruangtamu,ruangkeluarga,ruangkerja,kamar,ruangmakan,dapur]
	ruang_telur = random.choice(ruangan)
	telur_diantarkan = False
	posisi = ruangtamu
	print('Anda membawa sebuah telur untuk diantarkan ke dalam keranjang.')
	print('Ada sebuah keranjang dalam rumah, bisa kah kau menemukannnya untuk mengantar telurnya?')

	while True:
		if telur_diantarkan and posisi['nama'] == 'Ruang Tamu':
			print('Kau berhasil mengantarkan telurnya, sekarang kau bisa pergi, selamat !!!')
			break;
		elif not telur_diantarkan and posisi['nama'] == ruang_telur['nama']:
			telur_diantarkan = True
			print(msg(posisi) + 'ada keranjang, telur berhasil di kirim, sekarang keluar!')
			posisi['msg'] = ('kau kembali ke ' + posisi['nama'] + ' ayo cepat keluar.!')
		else:
			print(msg(posisi))
			posisi['msg'] = 'kau kembali ke ' + posisi['nama']

		stuck = True
		while stuck:
			dir = input('Ke arah mana kau ingin pergi: u/t/s/b? ')
			pilih = pilihan(posisi,dir)
			if pilih == -1:
				print('tolong pilih u/t/s/b?')
			elif pilih == 4:
				print('kau tidak bisa ke arah sana')
			else:
				posisi = posisi['arah'][pilih]
				stuck = False

	# print(posisi['nama'])

main()