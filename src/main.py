import os

# Menggunakan konstanta dengan huruf kapital untuk variabel global agar mudah dikonfigurasi
FILE_NAME = "tugas.txt"

def muat_tugas():
    """Memuat daftar tugas dari file teks saat aplikasi pertama kali dijalankan.
    
    Mengembalikan list of dictionaries berisi nama tugas dan statusnya.
    """
    tugas = []
    
    # Mencegah eror jika file penyimpanan belum terbentuk pada pembukaan pertama
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                # Memisahkan baris berdasarkan tanda pemisah status terakhir ' ['
                parts = line.strip().rsplit(" [", 1)
                if len(parts) == 2:
                    nama_tugas = parts[0]
                    status = parts[1].replace("]", "")
                    tugas.append({
                        "nama": nama_tugas, 
                        "selesai": status == "Selesai"
                    })
    return tugas

def simpan_tugas(tugas):
    """Menyimpan seluruh daftar tugas ke dalam file teks (persitensi data)."""
    with open(FILE_NAME, "w") as file:
        for t in tugas:
            status = "Selesai" if t["selesai"] else "Belum Selesai"
            file.write(f"{t['nama']} [{status}]\n")

def tampilkan_tugas(tugas):
    """Menampilkan daftar tugas ke layar. 
    
    Mengembalikan True jika ada tugas, dan False jika kosong (untuk validasi fungsi lain).
    """
    if not tugas:
        print("\n[!] Belum ada tugas dalam daftar.")
        return False

    print("\n=== DAFTAR TUGAS ANDA ===")
    for i, t in enumerate(tugas, 1):
        # Menggunakan ikon visual yang jelas untuk membedakan status tugas
        status = "✔" if t["selesai"] else "❌"
        print(f"{i}. [{status}] {t['nama']}")
    return True

def tambah_tugas(tugas):
    """Menambahkan tugas baru ke dalam daftar dan langsung menyimpannya."""
    nama_tugas = input("\nMasukkan nama tugas baru: ").strip()
    
    # Validasi input untuk memastikan pengguna tidak memasukkan teks kosong
    if nama_tugas:
        tugas.append({"nama": nama_tugas, "selesai": False})
        simpan_tugas(tugas)
        print(f"[+] '{nama_tugas}' berhasil ditambahkan!")
    else:
        print("[!] Nama tugas tidak boleh kosong.")

def tandai_selesai(tugas):
    """Mengubah status tugas tertentu menjadi selesai berdasarkan nomor urut."""
    # Menggunakan nilai balik dari tampilkan_tugas() untuk menghentikan proses jika daftar kosong
    if not tampilkan_tugas(tugas):
        return
    
    try:
        nomor = int(input("\nMasukkan nomor tugas yang selesai: "))
        # Memastikan nomor yang dimasukkan ada di dalam jangkauan indeks list
        if 1 <= nomor <= len(tugas):
            tugas[nomor - 1]["selesai"] = True
            simpan_tugas(tugas)
            print(f"[+] Tugas nomor {nomor} berhasil ditandai selesai!")
        else:
            print("[!] Nomor tugas tidak ditemukan.")
    except ValueError:
        print("[!] Input harus berupa angka yang valid.")

def hapus_tugas(tugas):
    """Menghapus tugas tertentu dari daftar berdasarkan nomor urut."""
    if not tampilkan_tugas(tugas):
        return

    try:
        nomor = int(input("\nMasukkan nomor tugas yang ingin dihapus: "))
        if 1 <= nomor <= len(tugas):
            # Menggunakan .pop() untuk menghapus sekaligus mengambil data tugas yang dihapus
            tugas_dihapus = tugas.pop(nomor - 1)
            simpan_tugas(tugas)
            print(f"[-] '{tugas_dihapus['nama']}' telah dihapus dari daftar.")
        else:
            print("[!] Nomor tugas tidak ditemukan.")
    except ValueError:
        print("[!] Input harus berupa angka yang valid.")

def main():
    """Fungsi utama yang mengontrol alur menu aplikasi (Menu Loop)."""
    tugas_list = muat_tugas()
    
    while True:
        print("\n=== APLIKASI TO-DO LIST ===")
        print("1. Lihat Daftar Tugas")
        print("2. Tambah Tugas")
        print("3. Tandai Tugas Selesai")
        print("4. Hapus Tugas")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ").strip()
        
        if pilihan == "1":
            tampilkan_tugas(tugas_list)
        elif pilihan == "2":
            tambah_tugas(tugas_list)
        elif pilihan == "3":
            tandai_selesai(tugas_list)
        elif pilihan == "4":
            hapus_tugas(tugas_list)
        elif pilihan == "5":
            print("\nTerima kasih! Sampai jumpa lagi.")
            break
        else:
            print("[!] Pilihan tidak valid. Silakan masukkan angka 1 sampai 5.")

if __name__ == "__main__":
    main()