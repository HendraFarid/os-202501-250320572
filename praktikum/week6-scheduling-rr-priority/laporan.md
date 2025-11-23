
# Laporan Praktikum Minggu 6
Topik: Penjadwalan CPU – Round Robin (RR) dan Priority Scheduling

---

## Identitas
- **Nama**  : Hendra Farid Hidayat  
- **NIM**   : 250320572
- **Kelas** : 1DSRA

---

## Tujuan
1. Menghitung *waiting time* dan *turnaround time* pada algoritma RR dan Priority.  
2. Menyusun tabel hasil perhitungan dengan benar dan sistematis.  
3. Membandingkan performa algoritma RR dan Priority.  
4. Menjelaskan pengaruh *time quantum* dan prioritas terhadap keadilan eksekusi proses.  
5. Menarik kesimpulan mengenai efisiensi dan keadilan kedua algoritma.  

---

## Dasar Teori
1. Round Robin merupakan algoritma penjadwalan preemptive yang memberikan setiap proses jatah waktu eksekusi yang sama (time quantum). Proses dieksekusi secara bergiliran berdasarkan urutan antrian siap (ready queue). Jika sebuah proses belum selesai ketika jatah waktunya habis, proses tersebut dipindahkan ke akhir antrian untuk menunggu giliran berikutnya. Tujuan utamanya adalah meningkatkan responsivitas sistem dan pemerataan penggunaan CPU (Silberschatz, Galvin, & Gagne, 2018).
2. Round Robin dirancang untuk lingkungan time-sharing sehingga setiap proses mendapat kesempatan eksekusi yang adil. Efisiensi algoritma sangat dipengaruhi oleh pemilihan ukuran quantum: quantum terlalu kecil meningkatkan context switching, sementara quantum terlalu besar mendekati penjadwalan FIFO (Tanenbaum, 2015).
3. Penjadwalan prioritas memilih proses dengan tingkat prioritas tertinggi untuk dieksekusi terlebih dahulu. Algoritma ini dapat bersifat preemptive maupun non-preemptive. Namun, ia memiliki kelemahan berupa starvation, di mana proses dengan prioritas rendah dapat tidak pernah mendapat giliran eksekusi jika proses prioritas tinggi terus datang (Silberschatz, 2018).

---

## Langkah Praktikum
1. **Siapkan Data Proses**
   Gunakan contoh data berikut (boleh dimodifikasi sesuai kebutuhan):
   | Proses | Burst Time | Arrival Time | Priority |
   |:--:|:--:|:--:|:--:|
   | P1 | 5 | 0 | 2 |
   | P2 | 3 | 1 | 1 |
   | P3 | 8 | 2 | 4 |
   | P4 | 6 | 3 | 3 |

2. **Eksperimen 1 – Round Robin (RR)**
   - Gunakan *time quantum (q)* = 3.  
   - Hitung *waiting time* dan *turnaround time* untuk tiap proses.  
   - Simulasikan eksekusi menggunakan Gantt Chart (manual atau spreadsheet).  
     ```
     | P1 | P2 | P3 | P4 | P1 | P3 | ...
     0    3    6    9   12   15   18  ...
     ```
   - Catat sisa *burst time* tiap putaran.

3. **Eksperimen 2 – Priority Scheduling (Non-Preemptive)**
   - Urutkan proses berdasarkan nilai prioritas (angka kecil = prioritas tinggi).  
   - Lakukan perhitungan manual untuk:
     ```
     WT[i] = waktu mulai eksekusi - Arrival[i]
     TAT[i] = WT[i] + Burst[i]
     ```
   - Buat tabel perbandingan hasil RR dan Priority.

4. **Eksperimen 3 – Analisis Variasi Time Quantum (Opsional)**
   - Ubah *quantum* menjadi 2 dan 5.  
   - Amati perubahan nilai rata-rata *waiting time* dan *turnaround time*.  
   - Buat tabel perbandingan efek *quantum*.

5. **Eksperimen 4 – Dokumentasi**
   - Simpan semua hasil tabel dan screenshot ke:
     ```
     praktikum/week6-scheduling-rr-priority/screenshots/
     ```
   - Buat tabel perbandingan seperti berikut:

     | Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
     |------------|------------------|----------------------|------------|-------------|
     | RR | ... | ... | Adil terhadap semua proses | Tidak efisien jika quantum tidak tepat |
     | Priority | ... | ... | Efisien untuk proses penting | Potensi *starvation* pada prioritas rendah |

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 6 - CPU Scheduling RR & Priority"
   git push origin main
   ```

---

## Kode/Perintah 
1. **Siapkan Data Proses**
   Gunakan contoh data berikut (boleh dimodifikasi sesuai kebutuhan):
   | Proses | Burst Time | Arrival Time | Priority |
   |:--:|:--:|:--:|:--:|
   | P1 | 5 | 0 | 2 |
   | P2 | 3 | 1 | 1 |
   | P3 | 8 | 2 | 4 |
   | P4 | 6 | 3 | 3 |
2. **Eksperimen 1 – Round Robin (RR)**
   - Gunakan *time quantum (q)* = 3.  
   - Hitung *waiting time* dan *turnaround time* untuk tiap proses.  
   - Simulasikan eksekusi menggunakan Gantt Chart (manual atau spreadsheet).
3. **Eksperimen 2 – Priority Scheduling (Non-Preemptive)**
   - Urutkan proses berdasarkan nilai prioritas (angka kecil = prioritas tinggi).  
   - Lakukan perhitungan manual untuk:
     ```
     WT[i] = waktu mulai eksekusi - Arrival[i]
     TAT[i] = WT[i] + Burst[i]
     ```
   - Buat tabel perbandingan hasil RR dan Priority.

4. **Eksperimen 3 – Analisis Variasi Time Quantum (Opsional)**
   - Ubah *quantum* menjadi 2 dan 5.  
   - Amati perubahan nilai rata-rata *waiting time* dan *turnaround time*.  
   - Buat tabel perbandingan efek *quantum*.

5. **Eksperimen 4 – Dokumentasi**
   - Simpan semua hasil tabel dan screenshot ke:
     ```
     praktikum/week6-scheduling-rr-priority/screenshots/
     ```
   - Buat tabel perbandingan seperti berikut:

     | Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
     |------------|------------------|----------------------|------------|-------------|
     | RR | ... | ... | Adil terhadap semua proses | Tidak efisien jika quantum tidak tepat |
     | Priority | ... | ... | Efisien untuk proses penting | Potensi *starvation* pada prioritas rendah |

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](<screenshots/scheduling-rr-priority.png>)

---

## Analisis
1. **Eksperimen 1**
   - Round Robin (RR)

| Proses        | Burst Time | Arrival Time | Priority | Finish (P1) | Finish (P2)  | Finish (P3)  | WT      | TAT    |
| ------------- | ---------- | ------------ | -------- | ----------- | ------------ | ------------ | ------- | ------ |
| **P1**        | 5          | 0            | 2        | 3 (sisa 2)  | 14 (selesai) |       -      | 9       | 14     |
| **P2**        | 3          | 1            | 1        | 6 (selesai) |       -      |       -      | 2       | 5      |
| **P3**        | 8          | 2            | 4        | 9 (sisa 5)  | 17 (sisa 2)  | 22 (selesai) | 12      | 20     |
| **P4**        | 6          | 3            | 3        | 12 (sisa 3) | 20 (selesai) |       -      | 11      | 17     |
| **Jumlah**    |            |              |          |             |              |              | **34**  | **46** |
| **Rata-rata** |            |              |          |             |              |              | **8,5** | **14** |
```
| P1 | P2 | P3 | P4 | P1 | P3 | P4 | P3 |
0    3    6    9   12   14   17    20   22
```

2. **Eksperimen 2**
   - Priority Scheduling

| Proses        | Burst Time | Arrival Time | Priority | Start | Finish | WT       | TAT       |
| ------------- | ---------- | ------------ | -------- | ----- | ------ | -------- | --------- |
| P1            | 5          | 0            | 2        | 0     | 5      | 0        | 5         |
| P2            | 3          | 1            | 1        | 5     | 8      | 4        | 7         |
| P3            | 6          | 3            | 4        | 8     | 14     | 5        | 11        |
| P4            | 8          | 2            | 3        | 14    | 22     | 12       | 20        |
| **Jumlah**    |            |              |          |       |        | **21**   | **43**    |
| **Rata-rata** |            |              |          |       |        | **5,25** | **10,75** |

```
|  P1  |  P2  |  P3  |  P4  |
0      5      8      14     22
```

- Tabel perbandingan hasil RR dan Priority
     
| Parameter                        | Round Robin (RR)                      | Priority Scheduling                               |
| -------------------------------- | ------------------------------------- | ------------------------------------------------- |
| Rata-rata Waiting Time (WT)      | **8,5**                               | **5,25**                                          |
| Rata-rata Turn Around Time (TAT) | **14**                                | **10,75**                                         |
| Jenis                            | Preemptive                            | Non-preemptive                                    |
| Kelebihan                        | Adil, setiap proses dapat jatah waktu | Waktu selesai cepat untuk proses prioritas tinggi |
| Kekurangan                       | Bisa menyebabkan waiting time besar   | Proses prioritas rendah menunggu sangat lama      |

3. **Eksperimen 3**
   - Quantum 2
  
| **Proses**    | **Burst Time** | **Arrival Time** | **Priority** | **Finish (P1)** | **Finish (P2)** | **Finish (P3)** | **Finish (P4)** | **WT**    | **TAT**   |
| ------------- | -------------- | ---------------- | ------------ | --------------- | --------------- | --------------- | --------------- | --------- | --------- |
| **P1**        | 5              | 0                | 2            | 2               | 10              | 16              | Selesai         | 16        | 11        |
| **P2**        | 3              | 1                | 1            | 4               | 11              | Selesai         | Selesai         | 10        | 7         |
| **P3**        | 8              | 2                | 4            | 6               | 13              | 18              | 22              | 20        | 12        |
| **P4**        | 6              | 3                | 3            | 8               | 15              | 20              | Selesai         | 17        | 11        |
| **Jumlah**    |                |                  |              |                 |                 |                 |                 | **63**    | **41**    |
| **Rata-rata** |                |                  |              |                 |                 |                 |                 | **15,75** | **10,25** |

```
| P1 | P2 | P3 | P1 | P4 | P3 | P4 | P3 |
0    3    6    9    11   14   17   20   22
```

- Quantum 5
  
| **Proses**    | **Burst Time** | **Arrival Time** | **Priority** | **Start** | **Finish** | **Finish (P2)** | **WT**   | **TAT** |
| ------------- | -------------- | ---------------- | ------------ | --------- | ---------- | --------------- | -------- | ------- |
| **P1**        | 5              | 0                | 2            | 0         | 5          | Selesai         | 5        | 0       |
| **P2**        | 3              | 1                | 1            | 5         | 8          | Selesai         | 7        | 4       |
| **P3**        | 8              | 2                | 4            | 8         | 13         | 21              | 19       | 13      |
| **P4**        | 6              | 3                | 3            | 14        | 18         | 22              | 19       | 11      |
| **Jumlah**    |                |                  |              |           |            |                 | **50**   | **28**  |
| **Rata-rata** |                |                  |              |           |            |                 | **12,5** | **7**   |

```
| P1 | P2 | P4 | P3 |
0    5    8   14    22
```

- Tabel perbandingan efek quantum.

| **Quantum**             | **Context Switching**     | **WT (Waktu Tunggu)** | **TAT (Waktu Penyelesaian)** | **Karakteristik**                                                          |
| ----------------------- | ------------------------- | --------------------- | ---------------------------- | -------------------------------------------------------------------------- |
| **Quantum = 2 (kecil)** | Banyak (frekuensi tinggi) | Lebih tinggi          | Lebih tinggi                 | Algoritma lebih adil, tapi boros waktu karena sering berpindah proses      |
| **Quantum = 5 (besar)** | Lebih sedikit             | Lebih rendah          | Lebih rendah                 | Lebih efisien, mirip FCFS karena proses berjalan lebih lama tanpa terputus |

4. **Eksperimen 4**

| Algoritma                 | Avg Waiting Time | Avg Turnaround Time | Kelebihan                    | Kekurangan                               |
| ------------------------- | ---------------: | ------------------: | ---------------------------- | ---------------------------------------- |
| RR (q=2)                  |             9.75 |               15.25 | Adil terhadap semua proses   | Tidak efisien jika quantum tidak tepat   |
| Priority (non-preemptive) |             5.25 |               10.75 | Efisien untuk proses penting | Potensi starvation pada prioritas rendah |
---

## Kesimpulan
Berdasarkan praktikum yang telah dilakukan, diambil poin-poin kesimpulan sebagai berikut : 
1. Priority Scheduling memberikan kemampuan terbaik karena dapat memproses tugas prioritas tinggi lebih cepat, meskipun berisiko menimbulkan starvation pada proses berprioritas rendah.
2. Round Robin memiliki kemampuan yang sangat dipengaruhi oleh time quantum. Quantum kecil meningkatkan respons tetapi membuat WT dan TAT tinggi karena banyak context switch. Quantum sedang memberikan hasil menengah. Quantum besar lebih efisien dan menghasilkan WT dan TAT lebih rendah.
3. Priority Scheduling cocok untuk tugas penting, sedangkan Round Robin ideal untuk sistem interaktif yang membutuhkan pemerataan CPU.

---

## Quiz
1. Apa perbedaan utama antara Round Robin dan Priority Scheduling?    
   **Jawaban:** Setelah melakukan eksperimen, perbedaan utama dari Round Robin dan Priority terletak pada cara menentukan urutan dan lama eksekusi proses. Round Robin berbasis pada waktu (time sharing), sedangkan priority scheduling berbais perioritas proses.
2. Apa pengaruh besar/kecilnya *time quantum* terhadap performa sistem?  
   **Jawaban:**  Quantum terlalu kecil menyebabkan sistem responsif tetapi kurang efisien. Sedangkan, quantum terlalu besar menyebabkan sistem efisien tetapi kurang responsif. Quantum yang ideal adalah saat context switching tidak terlalu sering tetapi tetap menjaga response time cepat. Umumnya, nilai time quantum sebaiknya sedikit lebih besar daripada rata-rata waktu eksekusi CPU burst proses, supaya sistem tetap seimbang antara respons dan efisiensi.
3. Mengapa algoritma Priority dapat menyebabkan *starvation*?  
   **Jawaban:**  Priority Scheduling menyebabkan starvation karena proses berprioritas rendah dapat terus menerus tidak dieksekusi selama ada proses lain yang berprioritas lebih tinggi masuk ke sistem.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?
  > Bagian yang paling menantang atau tersulit adalah memahami alur pergantian proses pada Round Robin serta cara menentukan urutan eksekusi pada Priority Scheduling.
- Bagaimana cara Anda mengatasinya?
  > Menghitung ulang secara manual dan memeriksa contoh di referensi-referensi yang digunakan selama proses.


---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
