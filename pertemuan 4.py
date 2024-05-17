#konruksi 1 kondisi
angka = int(input("masukkan angka = "))

if angka % 2 == 0 :
    print (f"angka {angka} merupakan bilangan genap")
else :
    print (f"angka {angka} merupakan bilangan ganjil")


#kontruksi 2 kondisi
tahun = int(input("masukkan tahun : "))
if (tahun % 4 == 0 and tahun % 100 == 0) or (tahun % 400 == 0):
    print (f"{tahun} adalah tahun kabisat")
else :
    print (f"{tahun} bukan tahun kabisat")



#kontruksi 3 kondisi atau lebih
angka1 = int(input("masukkan angka pertama = "))
angka2 = int(input("masukkan angka kedua = "))
operasi = input("masukkan operasi : (+ , - , * , / ) = ")
if operasi == "+" :
    hasil = angka1 + angka2
    print (f"{angka1} + {angka2} = {hasil}")
elif operasi == "-" :
    hasil = angka1 - angka2
    print (f"{angka1} - {angka2} =  {hasil}")
elif operasi == "*" :
    hasil = angka1 * angka2
    print (f"{angka1} * {angka2} =  {hasil}")
elif operasi == "/" :
    hasil = angka1 / angka2
    print (f"{angka1} / {angka2} = {hasil:.1f}")
else :
    print ("anda memasukkan operasi yang salah")