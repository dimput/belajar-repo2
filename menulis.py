# Ambil input dari user
nama = input("Nama: ")
umur = int(input("Umur: "))
alamat = input("Alamat: ")
# nama = ["apel\n", "mangga\n", "anggur"]

# format teks
teks = '{{"Nama": "{}",\n"Umur": {},\n"Alamat": "{}"}}'.format(nama, umur, alamat)

# buka file untuk ditulis
file_bio = open("./assets/biodata.json", "w")

# tulis teks ke file
file_bio.writelines(teks)

# tutup file
file_bio.close()