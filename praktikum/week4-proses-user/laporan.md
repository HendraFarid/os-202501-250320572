
# Laporan Praktikum Minggu 4
Topik: Manajemen Proses dan User di Linux

---

## Identitas
- **Nama**  : Hendra Farid Hidayat 
- **NIM**   : 250320572  
- **Kelas** : 1DSRA 

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
> Menjelaskan konsep proses dan user dalam sistem operasi Linux.
> Menampilkan daftar proses yang sedang berjalan dan statusnya.
> Menggunakan perintah untuk membuat dan mengelola user.
> Menghentikan atau mengontrol proses tertentu menggunakan PID.
> Menjelaskan kaitan antara manajemen user dan keamanan sistem.
---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.
- Membuat dan mengatur proses (process management).
- Mengelola user, group, serta hak akses pengguna.
- Menampilkan, menghentikan, dan mengontrol proses yang sedang berjalan.
- Menghubungkan konsep user management dengan keamanan sistem operasi.

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.
   > menurut pedoman github  mhbahara/os-202501.
2. Perintah yang dijalankan.
 ```bash
   whoami
   id
   groups
   ```

 ```bash
   ps aux | head -10
   top -n 1
   ```

```bash
   sleep 1000 &
   ps aux | grep sleep
   ```
- setelah mencatat PID, hentikaan proses :

```bash
   kill <PID>
   ```

 ```bash
   pstree -p | head -20
   ```
  
3. File dan kode yang dibuat.
   - praktikum/week4-proses-user/screenshots/proses_user.png 
4. Commit message yang digunakan.
   > edit dan kirim di `laporan.md`

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
 ```bash
   whoami
   id
   groups
   ```

 ```bash
   ps aux | head -10
   top -n 1
   ```

```bash
   sleep 1000 &
   ps aux | grep sleep
   ```
- setelah mencatat PID, hentikaan proses :

```bash
   kill <PID>
   ```

 ```bash
   pstree -p | head -20
   ```
  
---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](<screenshots/top.png>)

---

## Analisis
- Jelaskan makna hasil percobaan.
- **Eksperimen 1 – Identitas User**
> Setelah dilakukan percobaan, tidak memiliki izin sudo sehingga tidak dapat mengganti nama user.
- **Eksperimen 2 – Monitoring Proses**
  - PID
    > PID (Proccess ID), nomor unik yang diberikan oleh kernel untuk mengidentifikasi setiap proses yang sedang berjalan. Kegunaannya adalah untuk mengontrol atau menghentikan proses. 
  - USER
    > Untuk menunjukkan nama pengguna (user) yang menjalankan proses tersebut. Kegunaannya adalah untuk menentukan hak akses proses.
  - %CPU
    > Untuk menunjukkan persentase penggunaan CPU oleh proses tersebut. Kegunaan pada nilainya adalah untuk menunjukkan berapa banyak waktu CPU yang digunakan oleh proses selama periode.
  - %MEM
    > Untuk menunjukkan persentase penggunaan RAM (memori fisik) oleh proses. Kegunannya adalah untuk memantau proses yang terlalu boros memori.
  - COMMAND
    > Command adalah nama program yang sedang berjalan. Kegunaannya adalah sebagai perintah untuk menjalankan program.
**Eksperimen 3 – Kontrol Proses**
  - Catat PID Proses ```sleep``` : [1] 417
**Eksperimen 4 – Analisis Hierarki Proses**
- `sysytem(1)-+-`, berarti sistem yang dijalankan dengan PID 1
- `agetty(162)`, agetty(174), berarti proses agetty "alternative getty" dengan PID 162 serta 174
- `cron(146)`, sebuah perintah untuk menjalankan suatu tugas secara otomatis dengan PID 146
- `dbus-daemon(147)`, sebagai layanan sistem untuk komunikasi antarproses untuk menghubungkan proses sebelumnya dengan proses selanjutnya dengan PID 147
- `init-system(Ub(2)-+-....`, adakah root dari semua proses yang dijalankan di Ubuntu dengan PID 2.
- `rsyslogd(168)`, rsysgold adalah sebuah perintah yang menangkap seluruh perintah log sistem dari `sistem(1)` hingga `init-system` sesuai urutan dengan PID 168.
- `sytemd(327)`, `systemd.....,`, sebuah perintah untuk mengelola layanan (services) dengan PID 327 dengan urutam layanan services `systemd` selanjutnya.
- `unattended-upgr(184)`, sebuah perintah untuk membantu menjaga sistem tetap aman dan up-to-date dengan PID 184.
- `wsl-pro-service(157)`, mwnunjukkan perintah bahwa peritah dijalankan di wsl dengan PID 157.

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.
1. User memberikan perintah melalui ubuntu untuk kemudian di proses
2. Proses melalui tahapam-tahapan yang terstruktur dan logis dari sistem 

---

## Quiz
1. Apa fungsi dari proses init atau systemd dalam sistem Linux?
   **Jawaban:**  Menginisialisasi sistem, mengelola layanan (daemons), menangani level run, serta menangani shutdown dan reboot.
2. Apa perbedaan antara kill dan killall?
   **Jawaban:**  kill mengirimkan sinyal ke proses berdasarkan PID. Sedangkan killall mengirimkan sinyal ke semua proses dengan nama programnya.
3. Mengapa user root memiliki hak istimewa di sistem Linux?
   **Jawaban:**  User root merupakan user yang istimewa karena memiliki kontrol yang penuh terhadap seluruh sistem 

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?
  > Menganalisis perbedaan dari hasil perintah tertentu yang telah dijalankan.
- Bagaimana cara Anda mengatasinya?
  > Mengamati dengan cermat perbedaan dari setiap hasil perintah yang telah dijalankan dengan menggunakan referensi atau sumber-sumber yang valid.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
