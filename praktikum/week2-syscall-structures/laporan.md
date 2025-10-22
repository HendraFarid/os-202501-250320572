
# Laporan Praktikum Minggu [2]
Topik: Struktur System Call dan Fungsi Kernel

---

## Identitas
- **Nama**  : Hendra Farid Hidayat
- **NIM**   : 250320572
- **Kelas** : 1DSRA

---

## Tujuan
Tujuan praktikum minggu ini :
> Menjelaskan konsep dan fungsi system call dalam sistem operasi.
> Mengidentifikasi jenis-jenis system call dan fungsinya.
> Mengamati alur perpindahan mode user ke kernel saat system call terjadi.
> Menggunakan perintah Linux untuk menampilkan dan menganalisis system call.

---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.
Melakukan eksplorasi terhadap :
- Jenis-jenis system call yang umum digunakan (file, process, device, communication).
- Alur eksekusi system call dari mode user menuju mode kernel.
- Cara melihat daftar system call yang aktif di sistem Linux.

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.
A. **Setup Environment**
   - Gunakan Linux (Ubuntu/WSL).
   - Pastikan perintah `strace` dan `man` sudah terinstal.
   - Konfigurasikan Git (jika belum dilakukan di minggu sebelumnya).

B. **Eksperimen 1 – Analisis System Call**
   Jalankan perintah berikut:
   ```bash
   strace ls
   ```
   > Catat 5–10 system call pertama yang muncul dan jelaskan fungsinya.  
   Simpan hasil analisis ke `results/syscall_ls.txt`.

C. **Eksperimen 2 – Menelusuri System Call File I/O**
   Jalankan:
   ```bash
   strace -e trace=open,read,write,close cat /etc/passwd
   ```
   > Analisis bagaimana file dibuka, dibaca, dan ditutup oleh kernel.

D. **Eksperimen 3 – Mode User vs Kernel**
   Jalankan:
   ```bash
   dmesg | tail -n 10
   ```
   > Amati log kernel yang muncul. Apa bedanya output ini dengan output dari program biasa?

2. Perintah yang dijalankan.
   > terlampir docs.     
4. File dan kode yang dibuat.
   > terlampir docs.
5. Commit message yang digunakan.
   > terlampir docs.

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
A. ```bash
   strace ls
   ```
B. ```bash
   strace -e trace=open,read,write,close cat /etc/passwd
   ```
C. ```bash
   dmesg | tail -n 10
   ```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](<screenshots/syscall_ls.png>)
![Screenshot hasil](<screenshots/syscall_ls_1.png>)
![Screenshot hasil](<screenshots/syscall_ls_2.png>)
![Screenshot hasil](<screenshots/syscall_ls_3.png>)

---

## Analisis
- **EKSPERIMEN 1**
10 perintah pertama :
1. execve ("/usr/bin/ls", ["ls"], 0x7ffc3f991c40 /* 25 vers */)
Fungsinya adalah menjalankan program ls (menampilkan isi direktori). Maka, dalam hal ini adalah direktori dari strace ls, melacak semua system call yang digunakan oleh ls untuk berinteraksi dengan kernel.
2. brk(NULL)
Fungsinya adalah mengatur program break (batas memori heap), hanya untuk mengetahui posisi awal heap. Program ls memeriksa atau menginisialisasi area memori heap.
3. nmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP PRIVATE|MAP ANONYMOUS, -1, 0)
Fungsinya ialah memetakan isi file /etc/ld.so.cache ke memori, file cache library dibaca langsung ke memori agar lookup library cepat.
4. access("etc/ld.so.preload", R_OK)
Fungsinya adalah mengecek apakah file /etc/ld.so.preload ada dan bisa dibaca.
File ini digunakan oleh dynamic linker (ld.so) untuk memuat library tambahan sebelum library lain.
5. openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC)
Fungsinya adalah membuka file /etc/ld.so.cache yang berisi cache lokasi library dinamis agar loading lebih cepat.
6. read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\1\0\0\0\0\0\0\0\0\0\0\0"..., 832)
Fungsinya adalah menjadi langkah awal ketika loader membaca struktur biner program “ls” untuk dijalankan.
7. fstat(3, st_mode=S_IFREG|0644, st_size=17515, ...))
Fungsinya adalah mengetahui file (descriptor 3), mengetahui jenis file dan izin, serta ukuran file. 
8. map(NULL, 17515, PROT_READ, MAP_PRIVATE, 3, 0)
Fungsinya adalah memetakan file yang dibuka dengan deskriptor 3 ke memori sebesar 17.515 byte mulai dari awal file, hanya untuk dibaca, dan gunakan mode privat (tidak mengubah file asli). Biarkan kernel memilih lokasi memori.
9. close(3)
Fungsinya adalah menutup file descriptor nomor 3.

- **EKSPERIMEN 2**
close(3)		= 0
read(3, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\0\3\0>\1\0\0\0\220\234\2\0\0\0\0\0"..., 832)
close (3)		= 0
read(3, "# Locale name alias data base.\n#"..., 4096) = 2996
read(3, **, 4096)	= 0 
close(3)		= 0 
read(3, "root:x:0:0:root/root:/bin/bash\n"..., 131072) = 1426 
write(1, "root:x:0:0:root:/root:/bin/bash\n"..., 1426root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
…
…
) = 1426 
read(3, **, 131072)	= 0
close(3)		= 0
close(1)		= 0
close(2)		= 0


close(3) = 0
Menutup file descriptor 3. = 0 artinya sukses (0 = tidak ada error).

read(3, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\0\3\0>\1\0\0\0\220\234\2\0\0\0\0\0"..., 832)
Membaca sampai 832 byte dari FD 3. isi buffer dimulai dengan \177ELF 

close (3) = 0
Menutup FD 3 lagi (sukses).

read(3, "# Locale name alias data base.\n#"..., 4096) = 2996
Membaca file lain. = 2996 berarti 2996 byte berhasil dibaca.

read(3, **, 4096) = 0
Membaca lagi dari FD 3 tapi mengembalikan 0 → end-of-file (EOF). 

close(3) = 0
Menutup FD 3 (sukses).

read(3, "root:x:0:0:root/root:/bin/bash\n"..., 131072) = 1426
Membaca dari FD 3. Diminta buffer besar (131072) tapi terbaca 1426 byte — ukuran isi yang dibaca.

write(1, "root:x:0:0:root:/root:/bin/bash\n"..., 1426root:x:0:0:root:/root:/bin/bash daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin … ) = 1426
...
...
Menulis ke FD 1 (stdout) sejumlah 1426 byte — yaitu isi file passwd tadi. = 1426 menunjukkan jumlah byte yang benar-benar ditulis. Isi file "daemon". (...), file-file lain.

read(3, **, 131072) = 0
Baca lagi dari FD 3 → 0 (EOF). 

close(3) = 0
Menutup FD 3.

close(1) = 0
Menutup stdout (FD 1). Sukses.

close(2) = 0
Menutup stderr (FD 2). Sukses.

- **EKSPERIMEN 3** 
dmesg | tail -n 10
Berfungsi untuk menampilkan 10 baris terakhir dari log kernel (pesan yang dihasilkan oleh kernel Linux).
dmesg (display message), menampilkan pesan-pesan dari kernel ring buffer, yaitu catatan aktivitas yang dibuat oleh kernel sejak sistem boot.
tail -n 10, hanya menampilkan 10 baris terakhir dari output tersebut.
Bedanya dengan output program biasa, perintah dmesg | tail -n 10 menampilkan informasi sistem tingkat rendah, bukan data atau hasil proses aplikasi pengguna.

---

## Kesimpulan
1. System call dan sistem kernel saling berkaitan.
2. System call menjembatani antara user mode dan kernel mode.
3. System call hanya bisa dijalankan ketika mennggunakan layanan kernel.

---

## Tugas
1. Mengapa system call penting untuk keamanan OS? 
   **Jawaban:**  System call merupakan mekanisme penting yang menjadi jembatan antara program pengguna (user space) dan kernel (kernel space). Kernel adalah bagian inti dari sistem operasi yang mengatur seluruh sumber daya komputer, seperti memori, CPU, dan perangkat keras. Karena kernel memiliki hak akses tertinggi, maka setiap interaksi dengannya harus diatur secara hati-hati. Di sinilah system call berperan penting. Tanpa system call, program di user space bisa mengakses perangkat keras secara langsung. Hal ini berisiko tinggi karena dapat menyebabkan kerusakan sistem, pencurian data, atau gangguan stabilitas. Dengan adanya system call, setiap permintaan dari user program untuk mengakses sumber daya sistem akan melewati lapisan pengawasan kernel. Kernel akan memeriksa apakah permintaan tersebut sah, apakah proses memiliki izin yang cukup, dan apakah operasi tersebut aman untuk dijalankan. Dengan cara ini, system call bertindak sebagai filter keamanan yang mencegah aplikasi berbahaya atau rusak dari melakukan tindakan yang dapat merusak sistem. Selain itu, system call juga memungkinkan sistem operasi untuk mencatat aktivitas penting melalui mekanisme audit. Misalnya, setiap kali proses membuka file atau membuat koneksi jaringan, kernel dapat mencatatnya untuk tujuan keamanan atau forensik digital. Dengan demikian, system call berfungsi bukan hanya sebagai sarana komunikasi, tetapi juga sebagai benteng pertama perlindungan OS terhadap serangan atau kesalahan pengguna.
2. Bagaimana OS memastikan transisi user–kernel berjalan aman?
   **Jawaban:** Ketika program di user space memanggil system call, terjadi transisi dari user mode ke kernel mode. Proses ini sangat sensitif karena berpindah dari area dengan hak akses terbatas ke area dengan hak akses penuh. Untuk menjaga keamanan, sistem operasi menggunakan mekanisme kontrol perangkat keras (hardware privilege levels) dan instruksi khusus CPU, seperti syscall atau sysenter. Instruksi ini memastikan bahwa hanya jalur resmi yang diizinkan untuk masuk ke kernel mode. Kernel kemudian memvalidasi nomor system call, memeriksa parameter yang dikirim (seperti pointer memori dan izin akses), lalu mengeksekusi fungsi yang sesuai. Setelah selesai, kendali dikembalikan ke program pengguna melalui instruksi sysret. Proses ini menjaga agar tidak ada program yang dapat langsung mengeksekusi kode kernel tanpa izin, sehingga transisi tetap aman dan terkontrol.
3. Sebutkan contoh system call yang sering digunakan di Linux.
   **Jawaban:**  Beberapa system call yang umum digunakan di Linux antara lain:
read() dan write() → untuk membaca dan menulis data pada file atau perangkat.
open() dan close() → untuk membuka dan menutup file.
fork() → untuk membuat proses baru.
exec() → untuk mengeksekusi program lain.
exit() → untuk mengakhiri proses.
wait() → untuk menunggu proses anak selesai.
getpid() dan getuid() → untuk mendapatkan ID proses dan pengguna.

---

## Quiz
1. Apa fungsi utama system call dalam sistem operasi?  
   **Jawaban:**  Fungsi utama system call dalam sistem operasi adalah memberikan antarmuka (interface) antara program pengguna (user program) dan kernel sistem operasi, sehingga program bisa meminta layanan dari kernel dengan cara yang terkendali dan aman.
2. Sebutkan 4 kategori system call yang umum digunakan.
   **Jawaban:**  System call manajemen proses, system call manajemen berkas, system call manajemen memori, system call manajemen perangkat & komunikasi
3. Mengapa system call tidak bisa dipanggil langsung oleh user program?
   **Jawaban:**  System call tidak dapat dipanggil langsung oleh user program karena berjalan di mode kernel, sedangkan program pengguna hanya punya akses di mode user.
Dimaksudkan untuk melindungi sistem dari kesalahan atau tindakan berbahaya, serta memastikan semua akses ke sumber daya berjalan aman dan terkontrol.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?
> Bagian tersulit adalah menganalisis perintah-perintah.
- Bagaimana cara Anda mengatasinya?
> Cara saya mengatasinya adalah mencari referensi-referensi yang dapat membantu saya untuk menganalisis perintah-perintah yang dijalankan.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
