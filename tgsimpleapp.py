from os import system
from time import sleep

def print_menu():
	system("cls")
	print("""
		Aplikasi Kasir Restoran
		[1]. Lihat Menu
		[2]. Tambah Menu
		[3]. Buat Struk
		[4]. Hapus Menu
		[5]. Update Menu
		[Q]. Keluar
			""")

def print_header(msg):
	system("cls")
	print(msg)

def searching(food):
	if food in daftar_menu:
		return True
	else:
		return False

def not_empty(container):
	if len(container) != 0:
		return True
	else:
		return False

def print_header(msg):
	system("cls")
	print(msg)

def verify_ans(char):
	if char.upper() == "Y":
		return True
	else:
		return False

def print_data(food=None, harga=True, all_data=False):
	if food != None and all_data == False:
		print(f"NAMA : {food}")
		print(f"TELP : {daftar_menu[food]['harga']}")
	elif harga == False and all_data == False:
		print(f"NAMA : {daftar_menu}")
		print(f"TELP : {daftar_menu[food]['harga']}")
	elif all_data == True:
		for every_food in daftar_menu: # lists, string, dict
			nama = every_food # nama = key dari dict-nya
			harga = daftar_menu[every_food]["harga"]
			print(f"NAMA MAKANAN : {nama} - HARGA : {harga}")


def lihat_menu():
	print_header("DAFTAR KONTAK TERSIMPAN")
	if not_empty(daftar_menu):
		print_data(all_data=True)
	else:
		print("Belum di isi Menu")
	input("Tekan ENTER untuk kembali ke MENU")


def add_menu():
	system("cls")
	print("menambahkan menu baru")
	makanan = input("Nama Makanan : ")
	harga = input("Harga Makanan : ")
	data = {
		'harga' : harga
	}
	daftar_menu[makanan] = data
	print_data(all_data=True)
	input("Tekan ENTER untuk kembali ke MENU")

def kalkulator():
	system("cls")
	print("Daftar Harga dan nama makanan")
	print_data(all_data=True)
	namamenu1 = input("Nama Pesanan: ")
	pesanan1 = int(input("Pesanan 1 Rp"))
	namamenu2 = input("Nama Pesanan: ")
	pesanan2 = int(input("Pesanan 2 Rp"))
	namamenu3 = input("Nama Pesanan: ")
	pesanan3 = int(input("Pesanan 3 Rp"))
	aming = (pesanan1 + pesanan2 + pesanan3 * 10 / 100) + (pesanan1 + pesanan2 + pesanan3)
	print(namamenu1, "Rp", pesanan1)
	print(namamenu2, "Rp", pesanan2)
	print(namamenu3, "Rp", pesanan3)
	print("total anda adalah (Sudah Termasuk PPn) Rp", aming)
	input("Tekan MENU Untuk kembali")

def del_menu():
	print(daftar_menu)
	print("NOTE : Tuliskan Menu yang ingin dihapus dengan persis")
	print_data(all_data=True)
	x = input("Menu yang ingin dihapus ")
	exist = searching(x)
	if exist:
		respon = input(f"Apakah anda yakin untuk menghapus {x} ? Y/N: ")
		if verify_ans(respon):
			del daftar_menu[x]
			input("Tekan Menu untuk Keluar")
		else:
			print("Menu batal dihapus")
			input("Tekan Menu untuk Keluar")
	else:		
		input("Tekan Menu untuk kembali")

def update_price():
	print_header("Mengupdate Harga")
	print_data(all_data=True)
	makanan = input("Menu yang harganya akan di-update : ")
	exists = searching(makanan)
	if exists:
		print(f"{makanan}")
		print(f"Harga Lama = {daftar_menu[makanan]['harga']}")
		harga_baru = input("Harga Baru = ")
		respon = input("Yakin ingin mengupdate harga makanan (Y/N): ")
		if verify_ans(respon):
			daftar_menu[makanan]['harga'] = harga_baru
			print("Harga telah di-update")
			print_data(food = makanan)
			input("Tekan ENTER untuk kembali")
		else:
			print("Harga batal diubah")
			input("Tekan ENTER untuk kembali")
	
	
daftar_menu ={
	"Rendang" : { 
		"harga" : 15000
	},
	"Nasi_Padang" : {
		"harga" : 25000
	}
}

while True:
	print_menu()
	user_input = input("Pilihan : ").upper()
	if  user_input ==  "Q":
		print("Goodbye")
		break
	elif user_input == "1":
		lihat_menu()
	elif user_input == "2":
		add_menu()
	elif user_input == "3":
		kalkulator()
	elif user_input == "4":
		del_menu()
	elif user_input == "5":
		update_price()
