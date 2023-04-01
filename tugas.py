import time

# Class Method Kuis
class Kuis:
    #init method
    def __init__(self, pertanyaan, jawaban):
        self.pertanyaan = pertanyaan
        self.jawaban = jawaban

    #return type tanpa parameter
    def welcome_message():
        return "\nSelamat datang di program Quiz Sederhana!"
    print(welcome_message())

    #non-return type
    def tampilkan_pertanyaan(self):
        print(self.pertanyaan)

    #return type berparameter
    def periksa_jawaban(self, jawaban_pengguna):
        if jawaban_pengguna.lower() == self.jawaban.lower():
            print("BENAR!")
            return True
        else:
            print("SALAH!")
            return False

# Function untuk menjalankan kuis
def jalankan_kuis(kuis_list):
    skor = 0
    for kuis in kuis_list:
        kuis.tampilkan_pertanyaan()
        jawaban_pengguna = input("Jawaban: ")
        if kuis.periksa_jawaban(jawaban_pengguna):
            skor += 1
    time.sleep(2)
    print("Skor Anda:", skor, "dari", len(kuis_list))

# List pertanyaan dan jawaban kuis
pertanyaan_list = [
    "1. Ibu Kota Jerman",
    "2. Ibu Kota Perancis",
    "3. Ibu Kota Inggris",
    "4. Ibu Kota Italia",
    "5. Ibu Kota Belanda",
    "6. Ibu Kota Rusia",
    "7. Ibu Kota Hungaria",
    "8. Ibu Kota Spanyol",
    "9. Ibu Kota Denmark",
    "10. Ibu Kota Austria"
]
jawaban_list = [
    "berlin",
    "paris",
    "london",
    "roma",
    "amsterdam",
    "moskow",
    "budapest",
    "madrid",
    "kopenhagen",
    "vienna"
]

# Membuat objek-objek kuis dari list pertanyaan dan jawaban
kuis1 = Kuis(pertanyaan_list[0], jawaban_list[0])
kuis2 = Kuis(pertanyaan_list[1], jawaban_list[1])
kuis3 = Kuis(pertanyaan_list[2], jawaban_list[2])
kuis4 = Kuis(pertanyaan_list[3], jawaban_list[3])
kuis5 = Kuis(pertanyaan_list[4], jawaban_list[4])
kuis6 = Kuis(pertanyaan_list[5], jawaban_list[5])
kuis7 = Kuis(pertanyaan_list[6], jawaban_list[6])
kuis8 = Kuis(pertanyaan_list[7], jawaban_list[7])
kuis9 = Kuis(pertanyaan_list[8], jawaban_list[8])
kuis10 = Kuis(pertanyaan_list[9], jawaban_list[9])


# Menjalankan kuis
nama = input("Masukkan nama Anda: ")
print(f"Halo {nama}! Anda berada dalam Quiz Tebak Ibu Kota Negara di Eropa. \nMohon tunggu selama 3 detik untuk mulai mengerjakan.\n")

time.sleep(3)

kuis_list = [kuis1, kuis2, kuis3, kuis4, kuis5, kuis6, kuis7, kuis8, kuis9, kuis10]
jalankan_kuis(kuis_list)

time.sleep(2)

print("Quiz telah selesai. \nTerimakasih atas partisipasinya.")
