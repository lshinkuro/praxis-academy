''' buatlah program untuk:
1.menampilkan total pembayaran 
2.untuk menampilkan kembalian

'''

n = int(input("masukan berapa jumlah item yang dibeli :"))
nilai =[]
jumlah_total=0
for i in range(0,int(n)):
      tmp=int(input("masukan harga barang ke %d:"%(i+1)))
      nilai.append(int(tmp)) #ngubah file yang di input jadi di simpan di array

      jumlah_total = sum(nilai)
      print ("jumlah yang harus di bayar adalah :",jumlah_total)


jumlah_uang = int(input("jumlah uang saya :"))

if jumlah_uang >jumlah_total:
    uang_Kembalian = jumlah_uang-jumlah_total
    print("uang kembalian saya adalah:",uang_Kembalian)
elif jumlah_uang<jumlah_total:
    uang_Kembalian 
