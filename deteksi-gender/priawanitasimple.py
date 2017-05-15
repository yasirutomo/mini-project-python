from sklearn import tree # decision tree

# sample data format [tinggi, berat, ukuran-sepatu]
# data ukuran dari 11 orang
data = [[181,80,44], [177,70,43], [160,60,38], [154,54,37], 
		[166,65,40], [190,90,47], [175,64,39], [165,49,40],
		[171,75,42], [157,55,39], [181,85,43],]

# data gender,berurut sesuai dengan datanya (merujuk variabel data)
gender = ['pria', 'pria', 'wanita', 'wanita', 
			'wanita', 'pria', 'pria', 'wanita', 
			'pria', 'wanita', 'pria',]

# memanggil metode DecisionTreeClassifier() dari onjek tree
klasifikasi = tree.DecisionTreeClassifier()
# training data, memanggil metode fit(param), param = data dan gender
klasifikasi = klasifikasi.fit(data,gender)

# memasukkan data baru untuk di prediksi
# memanggil metode predict([data])
databaru = [170,59,41]
prediksi = klasifikasi.predict([databaru])

# print hasil prediksi
print(data) 
# print(type(data))
print(prediksi)