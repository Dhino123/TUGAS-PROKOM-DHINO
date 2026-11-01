glosarium = {
    "variabel": "tempat nyimpen nilai, dikasih nama biar gampang dipakai.",
    "list": "kumpulan banyak isi yang urut dan bisa diubah.",
    "tuple": "kumpulan banyak isi yang urut tapi nggak bisa diubah.",
    "loop": "perintah buat ngulang sesuatu untuk tiap isi list.",
    "if": "perintah buat milih jalan, jalan kalau syaratnya benar.",
    "string": "teks yang ditulis di dalam tanda kutip.",
    "indeks": "nomor urut isi di dalam list, mulai dari 0.",
    "append": "perintah buat nambah isi baru di akhir list.",
    "dictionary": "kumpulan pasangan kunci dan nilai, dicari pakai kunci.",
    "range": "pembuat deretan angka, berhenti sebelum angka akhir.",
}

for kata, arti in glosarium.items():
    print(f"{kata}: {arti}\n")