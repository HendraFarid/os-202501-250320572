
# Laporan Praktikum Minggu 11
Topik: Docker – Resource Limit (CPU & Memori)

---

## Identitas
- **Nama**  : Hendra Farid Hidayat  
- **NIM**   : 250320572  
- **Kelas** : 1DSRA

---

## Tujuan
1. Menulis Dockerfile sederhana untuk sebuah aplikasi/skrip.
2. Membangun image dan menjalankan container.
3. Menjalankan container dengan pembatasan **CPU** dan **memori**.
4. Mengamati dan menjelaskan perbedaan eksekusi container dengan dan tanpa limit resource.
5. Menyusun laporan praktikum secara runtut dan sistematis.


---

## Dasar Teori
1. Menurut OSTEP (Virtualization & Resource Management), sistem operasi modern melakukan resource virtualization agar CPU, memori, dan I/O dapat dibagi secara adil. Isolasi antar proses tetap terjaga. Tidak ada satu proses yang memonopoli sumber daya.
2. OSTEP menjelaskan bahwa CPU dibagi berdasarkan time-sharing dan scheduler menentukan berapa lama proses berjalan.
3. OSTEP memaparkan bahwa memori adalah resource terbatas. OS harus mencegah out-of-memory (OOM).

---

## Langkah Praktikum
1. **Persiapan Lingkungan**

   - Pastikan Docker terpasang dan berjalan.
   - Verifikasi:
     ```bash
     docker version
     docker ps
     ```

2. **Membuat Aplikasi/Skrip Uji**

   Buat program sederhana di folder `code/` (bahasa bebas) yang:
   - Melakukan komputasi berulang (untuk mengamati limit CPU), dan/atau
   - Mengalokasikan memori bertahap (untuk mengamati limit memori).

3. **Membuat Dockerfile**

   - Tulis `Dockerfile` untuk menjalankan program uji.
   - Build image:
     ```bash
     docker build -t week13-resource-limit .
     ```

4. **Menjalankan Container Tanpa Limit**

   - Jalankan container normal:
     ```bash
     docker run --rm week13-resource-limit
     ```
   - Catat output/hasil pengamatan.

5. **Menjalankan Container Dengan Limit Resource**

   Jalankan container dengan batasan resource (contoh):
   ```bash
   docker run --rm --cpus="0.5" --memory="256m" week13-resource-limit
   ```
   Catat perubahan perilaku program (mis. lebih lambat, error saat memori tidak cukup, dll.).

6. **Monitoring Sederhana**

   - Jalankan container (tanpa `--rm` jika perlu) dan amati penggunaan resource:
     ```bash
     docker stats
     ```
   - Ambil screenshot output eksekusi dan/atau `docker stats`.

7. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 13 - Docker Resource Limit"
   git push origin main
   ```

---

## Kode / Perintah
```bash
     docker version
     docker ps
```

```bash
     docker build -t week13-resource-limit .
```

```bash
     docker run --rm week13-resource-limit
```

```bash
   docker run --rm --cpus="0.5" --memory="256m" week13-resource-limit
```
   
```bash
     docker stats
```

---

## Hasil Eksekusi
![Screenshot hasil](<screenshots/docker_resource.png>)

---

## Analisis
Berdasarkan percobaan yang dilakukan : 
- Hasil percobaan menunjukkan bahwa Docker mampu menjalankan aplikasi uji secara stabil dan konsisten, sekaligus menyediakan mekanisme pembatasan sumber daya (resource limiting) yang bekerja sesuai dengan konfigurasi yang ditetapkan oleh pengguna, sehingga container tidak dapat menggunakan resource melebihi batas yang telah ditentukan.

- Pada kondisi tanpa pembatasan sumber daya, aplikasi di dalam container dapat memanfaatkan CPU secara maksimal sesuai kemampuan sistem host, yang menyebabkan proses eksekusi berjalan lebih cepat dan kinerja aplikasi menjadi optimal karena tidak ada pembatasan alokasi CPU.

- Ketika dilakukan pembatasan CPU, kinerja aplikasi mengalami penurunan kecepatan dibandingkan kondisi tanpa batasan, karena Docker hanya mengizinkan container menggunakan sebagian kapasitas CPU sesuai dengan nilai limit yang telah ditentukan, sehingga waktu pemrosesan menjadi lebih lama.

- Pada pengujian pembatasan memori, container terbukti tidak dapat menggunakan memori melebihi batas yang telah dikonfigurasi, dan ketika penggunaan memori mencapai ambang batas tersebut, proses aplikasi akan dihentikan secara otomatis oleh sistem untuk mencegah kelebihan penggunaan memori.

- Secara keseluruhan, hasil pengujian membuktikan bahwa Docker efektif dalam mengelola, mengontrol, dan membatasi penggunaan sumber daya sistem, baik CPU maupun memori, sehingga sangat berguna untuk menjaga stabilitas sistem, mencegah pemborosan resource, serta memastikan setiap aplikasi berjalan sesuai alokasi yang telah ditetapkan.


## Kesimpulan
1. Docker mampu menjalankan aplikasi dengan baik sekaligus mengelola penggunaan sumber daya secara efektif, karena container dapat dikonfigurasi untuk membatasi pemakaian CPU dan memori sesuai kebutuhan sistem.

2. Pembatasan sumber daya berdampak langsung terhadap kinerja aplikasi, di mana pembatasan CPU menyebabkan penurunan kecepatan eksekusi, sementara pembatasan memori mencegah penggunaan memori berlebih dan menghentikan proses saat batas tercapai.

3. Penerapan mekanisme resource limiting pada Docker membantu menjaga stabilitas dan efisiensi sistem, sehingga penggunaan sumber daya menjadi lebih terkontrol dan tidak mengganggu aplikasi atau proses lain pada sistem host.

---

## Quiz
1. Mengapa container perlu dibatasi CPU dan memori? 
   **Jawaban:**  Container tidak punya kernel sendiri. Semua container berjalan di kernel Linux yang sama dan menggunakan scheduler dan memory manager yang sama. Jika CPU tidak dibatasi, satu container bisa menggunakan 100% semua core dan menyebabkan CPU starvation pada container lain. Tanpa memory limit, container bisa mengalokasikan RAM terus-menerus, memicu OOM Killer pada level host yang mengakibatkan seluruh server crash dan semua container mati. Dengan memory limit, OOM hanya terjadi di dalam container dan host tetap aman.
2. Apa perbedaan VM dan container dalam konteks isolasi resource?
   **Jawaban:**  Perbedaan VM dan container dalam konteks isolasi resource saya paparkan dalam bentuk tabel sebagai berikut :
| Aspek    | VM               | Container       |
| -------- | ---------------- | --------------- |
| Kernel   | Sendiri          | Shared          |
| CPU      | Dialokasikan fix | Time-sharing    |
| Memori   | Reserved         | Dinamis + limit |
| Overhead | Tinggi           | Rendah          |
| Startup  | Lambat           | Cepat           |
| Isolasi  | Sangat kuat      | Lebih ringan    |

3. Apa dampak limit memori terhadap aplikasi yang boros memori? 
   **Jawaban:** Dampaknya terjadi bertahap, tidak langsung crash. Memory limit pada container menyebabkan aplikasi boros memori mengalami penurunan performa, penggunaan swap, dan akhirnya dihentikan oleh OOM Killer jika melewati batas. Hal ini melindungi sistem dan container lain, meskipun berdampak pada aplikasi yang tidak dirancang memory-aware.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
