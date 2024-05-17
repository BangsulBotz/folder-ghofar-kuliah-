#tampilan menu
print ("\nmenu menghitung luas & keliling")
print ("=" * 35 )
print ("1.persegi")
print ("2.persegi panjang")
print ("3.segitiga")
print ("4.lingkaran")
print ("=" * 35, "\n")
#keterangan:
#print yang ada di atas hanya untuk menampilkan menu

#input pilihan operasi
menghitung = (input("masukkan pilihan 1/2/3/4 = "))
#keterangan:
#meminta user untuk memilih operasi apa yang ingin di jalankan


#pilihan operasi 1 pada bangun datar persegi
if menghitung == '1':
    print ("menghitung luas & keliling persegi")
    print ("=" * 35, "\n")
    panjang  = eval(input("masukkan panjang= ")) #input panjang persegi
    luas     = panjang * panjang   #rumus mencari luas persegi
    keliling = panjang * 4         #rumus mencari keliling persegi
    print ("luas persegi     = ", luas)     #menampilkan jumlah luas persegi
    print ("keliling persegi = ", keliling) #menampilkan jumlah keliling persegi
    

#pilihan 2 pada bangun datar persegi panjang
elif menghitung == '2':
    print ("menghitung luas & keliling persegi panjang")
    print ("=" * 35, "\n")
    panjang  = eval(input("masukkan panjang= "))  #input panjang persegi panjang
    lebar    = eval(input("masukkan lebar= "))    #input lebar persegi panjang
    luas     = panjang * lebar        #rumus mencari luas persegi panjang
    keliling = 2 * (panjang + lebar)  #rumus mencari keliling persegi panjang
    print ("luas persegi panjang     = ", luas)     #menampilkan jumlah luas persegi panjang
    print ("keliling persegi panjang = ", keliling) #menampilkan jumlah keliling persegi panjang

#pilihan 3 pada bangun datar segitiga 
elif menghitung == '3':
    print ("menghitung luas & keliling segitiga")  
    print ("=" * 35, "\n")
    alas     = float(input("masukkan alas= "))   #input alas segitiga
    tinggi   = float(input("masukkan tinggi= ")) #input tinggi segitiga
    luas     = 0.5  * alas * tinggi  #rumus mencari luas segitiga
    keliling = alas + alas + alas    #rumus mencari keliling segitiga
    print ("luas segitiga     = ", luas)      #menampilkan luas segitiga
    print ("keliling segitiga = ", keliling)  #menampilkan keliling seggitiga

#pilihan 4 pada bangun datar lingkaran
elif menghitung =='4' :
    import math
    print ("menghitung luas & keliling lingkaran")
    print ("=" * 35, "\n")
    jari_jari = float(input("Masukkan jari jari lingkaran: ")) #input jari jari lingkaran
    luas      = math.pi * jari_jari**2   #rumus mencari luas lingkaran
    keliling  = 2 * math.pi * jari_jari  #rumus mencaru keliling lingkaran
    print(f"Luas lingkaran     = {luas:.2f}")      #menampilkan jumlah luas lingkaran 
    print(f"Keliling lingkaran = {keliling:.2f}")  #menampilkan jumlah keliling lingkaran

else:
    print ("anda memasukkan pilihan yang salah! silahkan pilih angka 1/2/3/4")
        
        