
# Laporan Praktikum Minggu 1
Arsitektur Sistem Operasi dan Kernel

---

## Identitas
- **Nama**  : Hendra Farid Hidayat  
- **NIM**   : 250320572
- **Kelas** : 1DSRA

---

## Tujuan
Tujuan praktikum minggu ini.  
> Menjelaskan peran sistem operasi dalam arsitektur komputer.
> Mengidentifikasi komponen utama OS (kernel, system call, device driver, file system).
> Membandingkan model arsitektur OS (monolithic, layered, microkernel).
> Menggambarkan diagram sederhana arsitektur OS menggunakan alat bantu digital (draw.io / mermaid).


---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.
1. Manajemen sumber daya: Kernel menentukan siapa yang mendapat CPU, memori, dan perangkat I/O → dasar efisiensi sistem (A.S. Tanenbaum, Modern Operating Systems (4th Ed); Silberschatz et al., Operating System Concepts).
2. Keamanan dan isolasi: Menjaga pemisahan antara ruang pengguna (user mode) dan kernel (privileged mode) untuk mencegah kerusakan dan serangan (A.S. Tanenbaum, Modern Operating Systems (4th Ed); Silberschatz et al., Operating System Concepts).
3. Debugging & performa: Pemahaman tentang proses scheduling, interrupt, dan concurrency membantu menemukan bottleneck (A.S. Tanenbaum, Modern Operating Systems (4th Ed); Silberschatz et al., Operating System Concepts).
4. Desain sistem: Jenis kernel (monolithic, microkernel, hybrid) memengaruhi kecepatan, stabilitas, dan skalabilitas sistem (A.S. Tanenbaum, Modern Operating Systems (4th Ed); Silberschatz et al., Operating System Concepts).

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.
a. Menginstall Ubuntu melalui Powershell Windows.
b. Mengkonfigurasi git.
c. Menjalankan perintah di Ubuntu dari Powershell Windows sesuai dengan perintah yang sudah diberikan di docs.
d. Screenshot hasil perintah.
e. Menganalisis hasil perintah.
2. Perintah yang dijalankan.
- git config --global user.name "Nama"
- git config --global user.email "Enail"
- uname -a
- whoami
- lsmod | head
- dmesg | head
3. File dan kode yang dibuat.
- Terlampir docs.
4. Commit message yang digunakan.
- Terlampir docs.

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
uname -a
lsmod | head
dmesg | head
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](<screenshots/Eksperimen Dasar.png>)

---

## Analisis
- Jelaskan makna hasil percobaan.
1. uname -a 
2. uname = unix name 
3. -a = all (menampilkan semua informasi yang trsedia) 
4. Linux, nama kernel yang digunakan
5. DEKSTOP-BG3RSLE , nama hostname dari sistem (nama komputer atau jaringan)
6. 5.15.167.4-micrsoft-standard-WSL2 , versi kernel Linux yang sedang berjalan  
7. #1 SMP Tue Nov 5 00:21:55 UTC 2024 , informasi tambahan tentang build kernel (nomor build, distributor, mode multiprosesor (SMP), dan tanggal kompilasi kernel) 
8. x86_64 , Arsitektur CPU kernel
9. x86_64 , arsitektur hardware mesin 
10. x86_64 , platform processor
11. GNU/Linux , sistem operasi berbasis kernel Linux dan utilitas GN
12. whoami , menunjukkan identitas pengguna yang menjalankan terminal
13. lsmod | head , menunjukkan module, size, used by
14. [ 0.000000 ] , waktu (dalam detik) sejak sistem mulai booting.
15. Linux version , versi kernel yang digunakan.
16. Command line ,  parameter boot kernel.
17. x86/fpu , inisialisasi dukungan hardware CPU.
18. BIOS-e820 , informasi peta memori dari BIOS.
19. DMI , identifikasi sistem perangkat keras (pabrikan, model, versi BIOS).
20. Memory , informasi alokasi memori.
    
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).
1. uname -a	: Identitas dan versi kernel (fungsi kernel) , 	uname() system call ,	Monolithic kernel (Linux) dari (arsitektur OS).
2. lsmod |	head :	Menunjukkan bahwa kernel mengelola perangkat keras melalui device drivers, kernel akan memanggil melalui system call, modul-modul kernel monolithic berjalan di ruang kernel.
3. dmesg |	head :	Pesan dmesg berasal langsung dari kernel yang menunjukkan fungsi-fungsi seperti manajemen memori, di system call untuk membaca buffer log kernel, di arsitektur OS pesan boot dan inisialisasi menunjukkan bagaimana kernel berinteraksi langsung dengan perangkat keras,
  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?
1. Hasil perintah dari uname -a, lsmod | head, dan dmesg | head hanya bisa dijalankan di Linux dan di Windows tidak bisa.
2. Masing-masing OS (Linux dan Windows) memiliki perintah yang berbeda.

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.
1. Kernel memiliki manfaat dalam manajemen sumber daya, keamanan dan isolasi, debugging & performa, serta desain system.
2. Sistem operasi Linux dan Windows memiliki perintah yang berbeda.

---

## Quiz
1. Sebutkan tiga fungsi utama sistem operasi.  
   **Jawaban:**  Pengelola sumber daya, penyedia layanan sistem (file & I/O), dan penghubung antara pengguna serta perangkat keras.
2. Jelaskan perbedaan antara kernel mode dan user mode.
   **Jawaban:**  Kernel mode merupakan mode operasi di mana sistem operasi (kernel) berjalan dengan akses penuh ke seluruh sumber daya hardware, sedangkan user mode merupakan mode tempat program pengguna dengan hak akses terbatas.
3. Sebutkan contoh OS dengan arsitektur monolithic dan microkernel.
   **Jawaban:**  Arsitektur monolithic contohnya Linux dan contoh arsitektur microkernel yaitu Mach.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?
  **Jawaban:** Bagian yang paling menantang pada minggu ini adalah cara menginstal Ubuntu di komputer karena ada beberapa yang mengalami error saat penginstalan menggunakan powershell Windows.  
- Bagaimana cara Anda mengatasinya?
  **Jawaban:** Cara saya mengatasinya adalah dengan meminta bantuan ke teman, kami berdiskusi bersama dengan menonton video tutorial dan bantuan dari ChatGPT hingga bisa menggunakan      Ubuntu/WSL.
---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
