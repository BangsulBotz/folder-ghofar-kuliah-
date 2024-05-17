  #pada string
nama = input ("masukkan nama anda : ")
#contoh integer
umur = int (input("masukkan umur anda : "))
#contoh float 
ipk = float (input ("masukkan ipk anda : "))
print (f"nama anda adalah : {nama}\numur anda adalah :{umur}\nipk anda adalah  : {ipk}")





bil = input ("masukkan bilangan bulat yang di pisahkan oleh spasi: ")
#membagi variabel bil menjadi variabel bil1 dan bil2
bil1,bil2 = map(int,bil.split())
print ("bilangan pertama:",bil1)
print ("bilangan kedua :",bil2)





#pada string
nama = input ("masukkan nama anda : ")
#contoh integer
umur = int (input("masukkan umur anda : "))
#contoh float 
ipk = float (input ("masukkan ipk anda : "))
print ("hallo", nama, "umur anda :", umur ,"ipk anda :",ipk)
print ("hallo "+ nama+ " umur anda :", umur ,"ipk anda :",ipk)
print ("hallo %s umur anda : %i ipk anda : %1f" % (nama,umur,ipk))
print (f"hallo {nama} umur anda : {umur} ipk anda : {ipk}")

