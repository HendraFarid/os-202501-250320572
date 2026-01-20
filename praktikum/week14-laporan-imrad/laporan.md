# Tugas Praktikum Minggu 14  
Topik: Penyusunan Laporan Praktikum Format IMRAD


---

## Identitas
- **Nama**  : Hendra Farid Hidayat
- **NIM**   : 250320572
- **Kelas** : 1DSRA

---

## Pendahuluan 
Penjadwalan CPU merupakan salah satu komponen penting yang berfungsi untuk mengatur urutan eksekusi proses agar penggunaan sumber daya prosesor dapat berjalan secara efisien. Penjadwalan yang baik dapat meningkatkan kinerja sistem, mengurangi waktu tunggu proses, serta memastikan keadilan dalam pembagian waktu CPU. Menurut Tanenbaum (2015), penjadwalan CPU merupakan bagian dari manajemen proses yang bertujuan untuk mengoptimalkan penggunaan prosesor dan meningkatkan respons sistem. Simulasi digunakan sebagai alat analisis untuk membandingkan algoritma scheduling secara teoritis. Oleh karena itu, pemahaman terhadap algoritma penjadwalan CPU menjadi hal yang fundamental dalam pembelajaran sistem operasi.

Salah satu algoritma penjadwalan CPU yang paling sederhana adalah First Come First Served (FCFS). Algoritma ini bekerja dengan prinsip bahwa proses yang pertama kali datang ke sistem akan dieksekusi lebih dahulu hingga selesai tanpa adanya preemption. Menurut Silberschatz et al. (2018), FCFS adalah algoritma penjadwalan non-preemptive paling sederhana. Proses dieksekusi berdasarkan urutan kedatangan ke ready queue. Dalam simulasi, proses diurutkan sesuai arrival time, lalu dihitung, Waiting time, turnaround time, kemudian response time. Kesederhanaan algoritma FCFS menjadikannya mudah untuk dipahami dan diimplementasikan, namun di sisi lain algoritma ini juga memiliki keterbatasan dalam hal efisiensi, terutama ketika terdapat proses dengan waktu eksekusi yang panjang.

Untuk memahami cara kerja serta karakteristik algoritma FCFS, diperlukan sebuah pendekatan yang sistematis, salah satunya melalui simulasi. Simulasi memungkinkan pengujian algoritma penjadwalan dengan data tertentu sehingga dapat dianalisis nilai waiting time dan turnaround time yang dihasilkan. Dengan adanya simulasi, proses perhitungan dapat dilakukan secara otomatis dan akurat, serta meminimalkan kesalahan yang mungkin terjadi dalam perhitungan manual. Berdasarkan hal tersebut, dilakukan simulasi penjadwalan CPU menggunakan algoritma FCFS dengan beberapa proses yang memiliki waktu kedatangan dan waktu eksekusi yang berbeda. Simulasi ini bertujuan untuk membandingkan hasil perhitungan manual dengan hasil program, serta menganalisis kelebihan dan keterbatasan algoritma FCFS dalam mengatur eksekusi proses pada CPU.

---


## Metode 
1. **Menyiapkan Dataset**

   Buat dataset proses minimal berisi:

   | Proses | Arrival Time | Burst Time |
   |:--:|:--:|:--:|
   | P1 | 0 | 6 |
   | P2 | 1 | 8 |
   | P3 | 2 | 7 |
   | P4 | 3 | 3 |
2. Melakukan perhitungan dengan rumus

- Average Waiting Time = total waiting time / jumlah proses

- Average Turnaround Time = total turnaround time / jumlah proses.
3. Menggunakan bahasa pemrograman python sebagai sarana untuk melakukan uji simulasi algoritma penjadwalan CPU.  


---

## Hasil 
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

## Pembahasan 
Berdasarkan hasil uji simulasi dan perhitungan manual, dapat disimpulkan bahwa algoritma First Come First Served (FCFS) telah diimplementasikan dengan benar dan konsisten. FCFS merupakan algoritma penjadwalan CPU paling sederhana, di mana proses dieksekusi berdasarkan urutan waktu kedatangan tanpa adanya preemption (pemotongan proses).

Pada simulasi yang dilakukan, data proses telah diurutkan sesuai arrival time sehingga sesuai dengan prinsip FCFS. Hasil perhitungan waktu mulai (start time), waktu selesai (finish time), waiting time, dan turnaround time yang dihasilkan oleh program sepenuhnya sama dengan perhitungan manual. Hal ini menunjukkan bahwa logika program valid dan akurat dalam merepresentasikan mekanisme FCFS secara matematis.

Nilai rata-rata waiting time sebesar 8,75 dan rata-rata turnaround time sebesar 14,75 mengindikasikan bahwa FCFS dapat menyebabkan waktu tunggu yang cukup besar, khususnya bagi proses yang datang belakangan dengan burst time yang relatif kecil. Fenomena ini dikenal sebagai convoy effect, di mana proses pendek harus menunggu proses panjang yang datang lebih awal, sehingga efisiensi sistem menjadi kurang optimal.

Dari sisi kelebihan, simulasi memberikan kemudahan dalam menganalisis performa algoritma penjadwalan tanpa harus melakukan perhitungan manual yang rentan kesalahan. Selain itu, simulasi bersifat fleksibel karena dapat dengan mudah dimodifikasi untuk menguji algoritma penjadwalan lain seperti SJF, Priority Scheduling, maupun Round Robin. Hal ini menjadikan simulasi sebagai alat pembelajaran dan analisis yang efektif dalam memahami konsep penjadwalan CPU.

Namun demikian, simulasi ini juga memiliki keterbatasan. Model yang digunakan masih bersifat ideal dan belum mencerminkan kondisi sistem operasi yang sebenarnya. Faktor-faktor penting seperti context switching, interrupt, proses I/O, dan overhead sistem operasi tidak diperhitungkan. Selain itu, simulasi hanya menampilkan hasil numerik dan tidak menggambarkan perilaku sistem secara real-time.

Secara keseluruhan, simulasi FCFS yang dilakukan sudah tepat untuk tujuan pembelajaran dan analisis dasar algoritma penjadwalan CPU. Meskipun demikian, untuk merepresentasikan sistem nyata secara lebih akurat, diperlukan model simulasi yang lebih kompleks dan mendekati kondisi operasional sistem operasi sesungguhnya.

--- 

## Kesimpulan
Berdasarkan hasil uji simulasi dan perhitungan manual yang telah dilakukan, dapat disimpulkan bahwa algoritma penjadwalan First Come First Served (FCFS) telah berhasil diimplementasikan dengan benar. Hasil simulasi program menunjukkan nilai waiting time dan turnaround time yang sama dengan perhitungan manual, sehingga membuktikan bahwa simulasi bersifat valid dan akurat. Simulasi FCFS mampu membantu dalam memahami konsep dasar penjadwalan CPU serta mempermudah proses perhitungan kinerja sistem secara efisien. Namun, algoritma FCFS memiliki kelemahan utama berupa waktu tunggu yang relatif besar bagi proses yang datang belakangan, terutama ketika proses dengan burst time panjang dieksekusi lebih dahulu. Hal ini dapat menurunkan efisiensi sistem secara keseluruhan. Sehingga, FCFS cocok digunakan untuk sistem dengan beban kerja sederhana, namun kurang optimal untuk sistem yang membutuhkan efisiensi dan responsivitas tinggi. Untuk meningkatkan performa, diperlukan algoritma penjadwalan lain yang lebih adaptif terhadap karakteristik.

---

## Daftar Pustaka 
1. Tanenbaum, A. *Modern Operating Systems*, 4th Ed.
2. OSTEP – referensi sesuai topik praktikum yang dipilih.
3. Praktik dilakukan dengan hasil yang diuji dalam tugas ke-9. https://github.com/HendraFarid/os-202501-250320572/blob/main/praktikum/week9-sim-scheduling/laporan.md. 


---

## Quiz
1. Mengapa format IMRAD membantu membuat laporan praktikum lebih ilmiah dan mudah dievaluasi?
   **Jawaban:**  Frmat IMRAD dibuat ilmiah supaya terdapat patokan yang baku sehingga memiliki isi dengan kerangka yang sama dan mempermuaadah proses evaluasi. 
2. Apa perbedaan antara bagian **Hasil** dan **Pembahasan**?
   **Jawaban:**  Pembahasan memiliki isi dari penelitian atau tugas ilmiah yang dikerjakan secara teoritis. Sedangkan, hasil memiliki isi dari tugas ilmiah yang dikerjakan secara praktik. 
3. Mengapa sitasi dan daftar pustaka penting, bahkan untuk laporan praktikum?
   **Jawaban:**  Daftar pustaka memiliki maksud bahwa penelitian atau tugas ilmiah memiliki integritas dan valid.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?
> Bagian yang paling sulit adalah mengerjakan bagian pembahasan.  
- Bagaimana cara Anda mengatasinya?
> Mencari dan memperbanyak sumber yang valid.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
