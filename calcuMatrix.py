import numpy as np

A= int(input("Masukkan Jumlah Baris Matriks 1 :"))
B= int(input("Masukkan Jumlah Baris Matriks 1 :"))
print("Masukkan Nilai-Nilai Matriks 1: ")
entries= list(map(int, input().split()))
matriks1 = np.array(entries).reshape(A,B)
print("Matriks 1 : ")
print(matriks1)

C= int(input("Masukkan Jumlah Baris Matriks 2 :"))
D= int(input("Masukkan Jumlah Baris Matriks 2 :"))
print("Masukkan Nilai-Nilai Matriks 2: ")
entries= list(map(int, input().split()))
matriks2 = np.array(entries).reshape(C,D)
print("Matriks 2: ")
print(matriks2)

print("\nSilahkan Pilih Perhitungan Matriks Sesuai Angka:\n 1.Penjumlahan\n 2.Pengurangan Matriks\n 3.Perkalian Skalar\n 4.Perkalian 2 Matriks\n")
Pilihan = int(input("Maasukkan Pilihan Anda: "))

if Pilihan == 1:
    print("\nHasil Penjumlahan Matriks: ")
    print(matriks1 + matriks2)

elif Pilihan == 2:
    print("\nHasil Pengurangan Matriks: ")
    print(matriks1 - matriks2)

elif Pilihan == 3:
    skalar = int(input("Jumlah Skalar: "))
    perkalian_skalar1 = skalar*(matriks1)
    print("Perkalian Skalar1 : ")
    print(perkalian_skalar1)
    perkalian_skalar2 = skalar*(matriks2)
    print("Perkalian Skalar2 : ")
    print(perkalian_skalar2)

elif Pilihan == 4:
    perkalian_matriks = np.dot(matriks1,matriks2)
    print("Hasil Perkalian 2 Matriks: ")
    print(perkalian_matriks)    





