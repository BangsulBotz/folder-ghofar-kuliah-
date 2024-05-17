'''
nama  :muhammad ghofar
kelas : perminyakan E
npm   :233210710
'''

#soal 1
angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
angka.insert(5, 5)
print(angka,"\n")

#soal 2
angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
angka.remove(4)
print(angka,"\n")

#soal 3
angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
angka_yang_keluar = 5
baris_pertama = angka[:angka_yang_keluar]
baris_kedua = angka[angka_yang_keluar:]
print(baris_pertama)
print(baris_kedua,"\n")

#soal 4
angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
third_index = len(angka) // 3
second_index = third_index * 2
baris_pertama = angka[:third_index]
baris_kedua = angka[third_index : second_index]
baris_ketiga = angka[second_index:]
print(baris_pertama)
print(baris_kedua)
print(baris_ketiga,"\n")

#soal 5
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7,8,9,10]
gabungan = list1 + list2 +list3
print(gabungan,"\n")

#soal nomor 6
angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
panggil = angka [0:6:3]
print (panggil)
