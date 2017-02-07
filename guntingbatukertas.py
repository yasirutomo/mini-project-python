import random
import sys

def initial(pilihan):
	if pilihan == 'Gunting':
		return 0
	if pilihan == 'Batu':
		return 1
	if pilihan == 'Kertas':
		return 2

def winlose(aturan,pilihanuser,pilihankomp):
	cekpemenang = initial(pilihankomp)
	cekaturan = aturan[cekpemenang]

	if cekaturan == 1:
		print('Selamat kamu Menang.')
	elif cekaturan == 0:
		print('Pilihan sama, Seri.')
	else:
		print('Maaf, kamu kalah.')

def main():
	aturan = (0,0,0) # gunting, batu, kertas

	gunting = {'nama':'Gunting','aturan':aturan,'pesan':''}
	batu = {'nama':'Batu','aturan':aturan,'pesan':''}
	kertas = {'nama':'Kertas','aturan':aturan,'pesan':''}

	gunting['aturan'] = (0,-1,1) # g=g:0,g<b:-1,g>k:1
	batu['aturan'] = (1,0,-1)
	kertas['aturan'] = (-1,1,0)
	
	datapilihan = [gunting,batu,kertas]

	keluar = False

	print('Game Gunting Batu Kertas')
	while not keluar:
		pilihankomp = random.choice(datapilihan)
		pilihanuser = gunting
		inputuser = input('Pilihan Kamu: ')
		print('Pilihan Komputer: ', pilihankomp['nama'])

		if inputuser.isdigit():
			if inputuser == 0:
				keluar = True
			else:
				print('Input tidak valid.')
		else:
			if inputuser == 'gunting':
				pilihanuser = gunting
			elif inputuser == 'batu':
				pilihanuser = batu
			elif inputuser == 'kertas':
				pilihanuser = kertas
			else:
				print('Input tidak valid')

			cekmenang = winlose(pilihanuser['aturan'],pilihanuser['nama'],pilihankomp['nama'])
			print()

main()