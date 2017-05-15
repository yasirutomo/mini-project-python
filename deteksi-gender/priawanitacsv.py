import csv # import paket csv
from sklearn import tree # import sklearn untuk decision tree

gender = [] # variabel global gender
data = [] # variabel global data

# S: parse data csv
with open('dataset\\data.csv','r',newline='',encoding='utf-8') as csvfile:
	r = csv.reader(csvfile, delimiter=',')
	for row in r:
		gendertemp=[]
		datatemp=[]
		for i in range(len(row)):
			# genderin=[]
			if i == 0: # row[0] = gender
				gendertemp = row[0]
				# print(gender)
			elif i == 1: # row[1] = tinggi
				tinggi = int(row[1])
				datatemp.append(tinggi)
			elif i == 2: # row[2] = berat
				berat = int(row[2])
				datatemp.append(berat)
			else: # row[3] = ukuran sepatu
				ukrsepatu = int(row[3])
				datatemp.append(ukrsepatu)
		gender.append(gendertemp) # gabung gender
		data.append(datatemp) # gabung karakter
	csvfile.close()
# E: parse data csv

# S: print data awal
print('\n Dataset Training:')
print('Data Gender: ', end='')
print(gender)
print('Data Karakter: ', end='')
print(data)
# E: print data awal

# S: klasifikasi dan training dataset untuk decision tree
# memanggil metode DecisionTreeClassifier() dari onjek tree
klasifikasi = tree.DecisionTreeClassifier()
# training data, memanggil metode fit(param), param = data dan gender
klasifikasi = klasifikasi.fit(data,gender)
# E: klasifikasi dan training dataset untuk decision tree

# S: data baru untuk di prediksi
# memasukkan data baru untuk di prediksi
# memanggil metode predict([data])
databaru = [170,59,41]
prediksi = klasifikasi.predict([databaru])
# E: data baru untuk di prediksi

# S: print hasil prediksi
print('\n Data Tes Baru: ', end='')
print(databaru, end='')
print(', ', end='')
print('Hasil: ', end='')
print(prediksi)
# E: print hasil prediksi