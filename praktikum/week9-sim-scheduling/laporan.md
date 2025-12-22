
# Laporan Praktikum Minggu 9
Topik: Simulasi Algoritma Penjadwalan CPU  

---

## Identitas
- **Nama**  : Hendra Farid Hidayat
- **NIM**   : 250320572
- **Kelas** : 1DSRA

---

## Tujuan
1. Membuat program simulasi algoritma penjadwalan FCFS dan/atau SJF.  
2. Menjalankan program dengan dataset uji yang diberikan atau dibuat sendiri.  
3. Menyajikan output simulasi dalam bentuk tabel atau grafik.  
4. Menjelaskan hasil simulasi secara tertulis.  
5. Mengunggah kode dan laporan ke Git repository dengan rapi dan tepat waktu.

---

## Dasar Teori
1. Menurut Tanenbaum (2015), penjadwalan CPU merupakan bagian dari manajemen proses yang bertujuan untuk mengoptimalkan penggunaan prosesor dan meningkatkan respons sistem. Simulasi digunakan sebagai alat analisis untuk membandingkan algoritma scheduling secara teoritis.
2. Menurut Silberschatz et al. (2018), FCFS adalah algoritma penjadwalan non-preemptive paling sederhana. Proses dieksekusi berdasarkan urutan kedatangan ke ready queue. Dalam simulasi, proses diurutkan sesuai arrival time, lalu dihitung, *Waiting time*, *turnaround time*, kemudian *response time*.
3. Menurut Silberschatz et al. (2018), SJF (Shortest Job First) memilih proses dengan CPU burst terpendek. Dapat bersifat non-preemptive atau preemptive (Shortest Remaining Time First). Dalam simulasi, burst time tiap proses diasumsikan diketahui atau diprediksi.

---

## Langkah Praktikum
1. **Menyiapkan Dataset**

   Buat dataset proses minimal berisi:

   | Proses | Arrival Time | Burst Time |
   |:--:|:--:|:--:|
   | P1 | 0 | 6 |
   | P2 | 1 | 8 |
   | P3 | 2 | 7 |
   | P4 | 3 | 3 |

2. **Implementasi Algoritma**

   Program harus:
   - Menghitung *waiting time* dan *turnaround time*.  
   - Mendukung minimal **1 algoritma (FCFS atau SJF non-preemptive)**.  
   - Menampilkan hasil dalam tabel.

3. **Eksekusi & Validasi**

   - Jalankan program menggunakan dataset uji.  
   - Pastikan hasil sesuai dengan perhitungan manual minggu sebelumnya.  
   - Simpan hasil eksekusi (screenshot).

4. **Analisis**

   - Jelaskan alur program.  
   - Bandingkan hasil simulasi dengan perhitungan manual.  
   - Jelaskan kelebihan dan keterbatasan simulasi.

5. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 9 - Simulasi Scheduling CPU"
   git push origin main
   ```

---

## Kode / Perintah
 | Proses | Arrival Time | Burst Time |
   |:--:|:--:|:--:|
   | P1 | 0 | 6 |
   | P2 | 1 | 8 |
   | P3 | 2 | 7 |
   | P4 | 3 | 3 |

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
- ![Screenshot hasil](<screenshots/Simulasi FCFS 1.png>)
- ![Screenshot hasil](<screenshots/Simulasi FCFS 2.png>)

---

## Analisis
- Jelaskan alur program (Simulasi scheduling FCFS)
1. Inisialisasi Data Proses
```bash 
processes = [
    ("P1", 0, 6),
    ("P2", 1, 8),
    ("P3", 2, 7),
    ("P4", 3, 3)
]
```

Setiap elemen tuple berisi:

Nama Proses

Arrival Time (waktu kedatangan)

Burst Time (waktu eksekusi CPU)

Urutan data sudah sesuai FCFS, yaitu berdasarkan waktu kedatangan.

2. Inisialisasi Variabel
```bash
current_time = 0
total_wt = 0
total_tat = 0
```

current_time → menyimpan waktu CPU saat ini

total_wt → akumulasi seluruh waiting time

total_tat → akumulasi seluruh turnaround time

3. Menampilkan Header Output
```bash
print("FCFS Scheduling")
print("Proses | Arrival | Burst | Start | Finish")
```

Digunakan untuk menampilkan judul dan header tabel hasil simulasi.

4. Perulangan Setiap Proses (FCFS)
for p in processes => Program memproses setiap proses satu per satu sesuai urutan kedatangan.

5. Mengambil Data Proses
```bash
name, arrival, burst = p
```

name → nama proses

arrival → arrival time

burst → burst time

6. Menentukan Waktu Mulai Eksekusi
```bash
start = max(current_time, arrival)
```

Artinya:

Jika CPU masih sibuk (current_time > arrival), proses menunggu

Jika CPU idle (current_time < arrival), proses mulai saat dia datang

FCFS tidak memotong proses yang sedang berjalan

7. Menentukan Waktu Selesai
```bash
finish = start + burst
```

Waktu selesai = waktu mulai + burst time

8. Menghitung Waiting Time
```bash
waiting = start - arrival
```

Waiting Time = waktu mulai − waktu kedatangan

9. Menghitung Turnaround Time
```bash
turnaround = finish - arrival
```

Turnaround Time = waktu selesai − waktu kedatangan

10. Menjumlahkan Total WT dan TAT
```bash
total_wt += waiting
total_tat += turnaround
```
Digunakan untuk menghitung rata-rata.

11. Update Waktu CPU
```bash
current_time = finish
```

CPU sekarang berada di waktu selesainya proses ini, lalu lanjut ke proses berikutnya.

12. Menampilkan Hasil per Proses
```bash
print(f"{name:5} | {arrival:7} | {burst:5} | {start:5} | {finish:6}")
```
Menampilkan data dalam bentuk tabel:

Proses, Arrival, Burst, Start, Finish

13. Menghitung dan Menampilkan Rata-rata
```bash
print("\nRata-rata Waiting Time:", total_wt / len(processes))
print("Rata-rata Turnaround Time:", total_tat / len(processes))
```

Rumus:

Average Waiting Time = total waiting time / jumlah proses

Average Turnaround Time = total turnaround time / jumlah proses

- Bandingkan hasil simulasi dengan perhitungan manual.

a. Hasil Perhitungan Manual

| Proses | Arrival | Burst | Start | Finish | Waiting | Turnaround |
| ------ | ------- | ----- | ----- | ------ | ------- | ---------- |
| P1     | 0       | 6     | 0     | 6      | 0       | 6          |
| P2     | 1       | 8     | 6     | 14     | 5       | 13         |
| P3     | 2       | 7     | 14    | 21     | 12      | 19         |
| P4     | 3       | 3     | 21    | 24     | 18      | 21         |


Rata-rata Waiting Time
= (0 + 5 + 12 + 18) / 4 = 8.75

Rata-rata Turnaround Time
= (6 + 13 + 19 + 21) / 4 = 14.75

b. Hasil Simulasi Program

Output program yang telah dijalankan menghasilkan nilai yang sama dengan perhitungan manual.

c. Kesimpulan Perbandingan

Simulasi FCFS pada program valid dan akurat. Program sukses merepresentasikan konsep FCFS secara matematis. Simulasi mempermudah perhitungan tanpa risiko kesalahan hitung secara manual.

- Jelaskan kelebihan dan keterbatasan simulasi.

a. Kelebihan Simulasi

 Mengurangi kesalahan manusia dalam perhitungan. Cepat dan efisien untuk jumlah proses yang besar.  Mudah dimodifikasi untuk algoritma lain (SJF, Priority, Round Robin). Membantu visualisasi dan analisis performa CPU.

b. Keterbatasan Simulasi

Bergantung pada asumsi yang disederhanakan. Tidak merepresentasikan kondisi sistem nyata sepenuhnya
(contohnya seperti, I/O, interupsi, dan context switching). Hanya menunjukkan hasil numerik, bukan kondisi *real-time* sebenarnya. Tidak mencerminkan overhead sistem operasi. 

---

## Kesimpulan
1. Pada algoritma FCFS, proses dieksekusi berdasarkan urutan kedatangan (arrival time) tanpa memperhatikan lama burst time. Proses yang datang lebih awal akan dilayani terlebih dahulu dan berjalan sampai selesai sebelum proses berikutnya dijalankan.
2. Berdasarkan hasil simulasi:

- Rata-rata Waiting Time FCFS = 8,75

- Rata-rata Turnaround Time FCFS = 14,75

Hal ini menunjukkan bahwa pada FCFS, proses dengan burst time besar yang datang lebih awal dapat menyebabkan proses lain menunggu cukup lama. Mengakibatkan kondisi *convoy effect*, di mana proses-proses pendek harus menunggu proses panjang selesai terlebih dahulu.
3. Algoritma FCFS cocok digunakan pada sistem sederhana yang tidak memerlukan optimasi waktu tunggu, tetapi kurang efektif untuk sistem multiprogramming karena dapat menghasilkan waiting time dan turnaround time yang besar.

---

## Quiz
1. Mengapa simulasi diperlukan untuk menguji algoritma scheduling?   
   **Jawaban:**  Simulasi diperlukan untuk menguji algoritma CPU scheduling karena beberapa alasan, yaitu meniru kondisi sistem nyata tanpa risiko, mudah membandingkan beberapa algoritma, memahami cara kerja algoritma secara rinci, mengukur kinerja secara kuantitatif, menghemat biaya dan waktu, menguji berbagai skenario ekstrem.
2. Apa perbedaan hasil simulasi dengan perhitungan manual jika dataset besar?  
   **Jawaban:**  Perbedaan hasil simulasi dan perhitungan manual ketika dataset besar antara lain : 
- Akurasi hasil
Perhitungan manual pada dataset besar sangat rentan terhadap kesalahan hitung (human error), terutama saat menentukan waiting time dan turnaround time untuk banyak proses. Simulasi menggunakan program akan menghasilkan perhitungan yang konsisten dan lebih akurat karena dilakukan secara otomatis.
- Efisiensi waktu
Manual membutuhkan waktu sangat lama dan tidak praktis jika jumlah proses banyak. Simulasi dapat menyelesaikan perhitungan dalam hitungan detik meskipun dataset sangat besar.
- Detail hasil
Manual biasanya hanya menghitung sebagian data atau contoh kecil karena keterbatasan waktu. Simulasi mampu menampilkan detail lengkap setiap proses (urutan eksekusi, waiting time, turnaround time) tanpa batasan jumlah data.
- Konsistensi
Perhitungan manual sulit diulang jika data diubah sedikit saja. Simulasi mudah dijalankan ulang dengan dataset berbeda atau dimodifikasi untuk skenario lain.
- Skalabilitas
Pada dataset kecil, hasil simulasi dan manual secara teori sama. Pada dataset besar, simulasi jauh lebih unggul karena mampu menangani kompleksitas dan volume data tanpa kehilangan ketelitian.
3. Algoritma mana yang lebih mudah diimplementasikan? Jelaskan.
   **Jawaban:** Algoritma yang paling mudah diimplementasikan adalah FCFS (First Come First Serve). Alasannya:
- Konsep sangat sederhana, FCFS mengeksekusi proses berdasarkan urutan kedatangan. Proses yang datang lebih dulu akan dilayani lebih dulu tanpa preemption atau perhitungan tambahan.
- Struktur data sederhana, implementasi FCFS cukup menggunakan queue (antrian). Tidak perlu sorting berdasarkan burst time atau prioritas seperti pada SJF atau Priority Scheduling.
- Logika program mudah, FCFS hanya memerlukan: mengurutkan proses berdasarkan arrival time.
- Menjalankan proses satu per satu, titdak ada pengecekan proses terpendek atau pergantian proses di tengah eksekusi.
- Minim overhead komputasi, FCFS tidak membutuhkan perhitungan ulang setiap kali proses baru datang, sehingga lebih ringan dibandingkan algoritma lain.
- Cocok untuk pembelajaran dasar, karena kesederhanaannya, FCFS sering digunakan sebagai algoritma awal untuk memahami konsep scheduling sebelum mempelajari algoritma yang lebih kompleks.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?
> Bagian yang paling menantang pada minggu ini adalah pengaplikasian bahasa pemrograman python dalam pembuatan FCFS Scheduling.
- Bagaimana cara Anda mengatasinya?
> Meneliti bagian yang error, kemudian menggantinya dengan kode yang tepat.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
