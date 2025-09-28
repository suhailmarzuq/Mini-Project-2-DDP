import maskpass as mp
from prettytable import PrettyTable

c_dialog = 0

stat_m = ("Nama", "Pekerjaan", "Misi")

mode = {
    "freemode": {"role": "Visitor", "password": ""},
    "paidmode": {"role": "Adventurer", "password": "Adv12451."}
}

def login():
    try:
        while True:
            print("""
    Selamat datang! Tulis jenis role anda!
    1. freemode
    2. paidmode
    """)
            role = input("Pilihan Role: ")

            if role == "freemode":
                print("Login ke mode gratis. Role:", mode[role]["role"])
                return 1

            elif role == "paidmode":
                password = mp.askpass(prompt="Masukkan Password : ", mask="●")
                if password == mode["paidmode"]["password"]:
                    print("Login ke mode berbayar. Role:", mode[role]["role"])
                    return 2
                else:
                    print("Password salah, coba lagi!\n")

            else:
                print("Role salah, coba lagi!\n")
    except (KeyboardInterrupt, EOFError):
        print("Tolong memasukkan input dengan benar.")

def visitor():
    print(f"Atda : Selamat datang di guild petualang, wahai pengunjung!")
    input()
    print(f"Atda : Namaku adalah Atda, resepsionis dari guild ini.")
    input()
    print(f"Atda : Tugasku adalah mengurus para petualang, misi-misi yang ada dan melayani pengunjung seperti anda!")
    input()
    print(f"Atda : Kami sangat senang melayani siapapun yang membutuhkan jasa guild.")
    input()
    print(f"Atda : Baiklah, itu saja yang bisa saya jelaskan kepada pengunjung. Semoga anda akan menjadi petualang kami suatu saat nanti!")

def status():
    global stat
    tabel_status = PrettyTable()
    tabel_status.add_column("STATUS", [
    f"Nama      : {stat[0]}",
    f"Pekerjaan : {stat[1]}",
    f"Misi      : {stat[2]}"
    ])
    tabel_status.align["STATUS"] = "l"
    print(tabel_status)

    global item
    tabel_item = PrettyTable()
    tabel_item.add_column("ITEM", item)
    tabel_item.align["ITEM"] = "l"
    print(tabel_item)


def adventurer():
    try:
        global stat
        global item
        nm = ("Atda", "Lily")
        print(f"{nm[0]} : Halo Petualang! Siapa nama anda?")
        nama = input("Nama : ")
        print()
        stat = [nama, "Petualang", "Tidak Ada"]
        item = ["ID Card Petualang", "Pedang", "Heal Potion"]
        print(f"{nm[0]} : Baiklah, tuan {stat[0]}, berikut status anda : ")
        status()
        print(f"""
    {nm[0]} : Karena hari ini damai dan hanya ada 1 misi hari ini, apakah anda bersedia menerimanya?
    Misi : Mencari Boneka Hilang [Y/N]
    """)
        choose = input("> ")
        print()
        if choose == "Y":
            print(f"{nm[0]} : Baik, selamat menjalankan misi!")
            stat[2] = "Mencari Boneka Hilang"
            status()

            print(f"{stat[0]} berjalan di kota, dekat perkiraan lokasi di mana boneka itu terjatuh.")
            input()
            print("Terdapat dua jalan besar yang mengarah ke tempat yang berlawanan. Satu mengarah ke daerah pasar dan satu mengarah ke daerah permukiman. Mana yang kamu pilih?\n[Pasar/Pemukiman]")
            choose = input("> ")

            if choose == "Pasar":
                print(f"{stat[0]} menemukan Boneka Beruang!")
                input()
                item.append("Boneka Beruang")
                status()
                print(f"{nm[1]} : Apakah kakak membawa bonekaku? [Y/N]")
                choose = input("> ")
                if choose == "Y":
                    item.remove("Boneka Beruang")
                    print(stat[0], "memberikan boneka beruang.")
                    status()
                    print(nm[1], ": Terima kasih banyak, kak! Ini bayarannya!")
                    item.append("5 Coin")
                    print("+5 coins!")
                    status()
                    print(f"{nm[0]}: Kerja bagus petualang {stat[0]}, sampai jumpa lagi!")
                    input()



            else:
                print(f"{stat[0]} sudah mencari ke manapun, tetapi tidak menemukan boneka yang dicari.")
                input()
                print(f"{nm[1]} : Kakak tidak menemukan bonekaku, ya ...")
                print("[MISSION FAILED]")

        else:
            print(f"{nm[0]} : Baiklah, sampai jumpa lagi!")
    except (KeyboardInterrupt, EOFError):
        print("Tolong memasukkan input dengan benar.")
    
mode_choosen = login()
print()

if mode_choosen == 1:
    visitor()

elif mode_choosen == 2:
    adventurer()

