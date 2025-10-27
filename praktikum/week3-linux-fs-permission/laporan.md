# Laporan Praktikum Minggu [3]
Topik: Linux FS Permission

---

## Identitas
- **Nama**  : Hendra Farid Hidayat 
- **NIM**   : 250320572
- **Kelas** : 1DSRA

---

## Tujuan
> Menggunakan perintah ls, pwd, cd, cat untuk navigasi file dan direktori.
> Menggunakan chmod dan chown untuk manajemen hak akses file.
> Menjelaskan hasil output dari perintah Linux dasar.
> Menyusun laporan praktikum dengan struktur yang benar.
> Mengunggah dokumentasi hasil ke Git Repository tepat waktu.

---
 
## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.
1. Mempelajari pengelolaan file dan
2. Mempelajari pengelolaan direktori menggunakan perintah dasar Linux
3. Mempelajari konsep permission dan ownership.
   
---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.
   ```bash
   pwd
   ls -l
   cd /tmp
   ls -a
   ```

   ```bash
   cat /etc/passwd | head -n 5
   ```

```bash
   echo "Hello <NAME><NIM>" > percobaan.txt
   ls -l percobaan.txt
   chmod 600 percobaan.txt
   ls -l percobaan.txt
   ```

3. File dan kode yang dibuat.
    praktikum/week3-linux-fs-permission/screenshots/praktik linux_fs_permission.png
4. Commit message yang digunakan.
   ```bash
   git add .
   git commit -m "Minggu 3 - Linux File System & Permission"
   git push origin main
   ```


---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
   ```bash
   pwd
   ls -l
   cd /tmp
   ls -a
   ```

   ```bash
   cat /etc/passwd | head -n 5
   ```

```bash
   echo "Hello <NAME><NIM>" > percobaan.txt
   ls -l percobaan.txt
   chmod 600 percobaan.txt
   ls -l percobaan.txt
   ```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](<screenshots/praktik linux_fs_permission.png>)

---

## Analisis
**Eksperimen 1 – Navigasi Sistem File**
   Jalankan perintah berikut:
   ```bash
   pwd
   ls -l
   cd /tmp
   ls -a
   ```
   - Jelaskan hasil tiap perintah.
1. pwd "print workinf directory", menampilkan lokasi direktori saat ini. Yaitu, /home/upb
2. ls -1 "list (one per line)", list (one per line). Jumlahnya 4.
3. cd "change directory", tmp "temprorary". Artinya, pindah direktori ke tempat penyimpanan file sementara
4. ls -a "list all". Artinya, tampilkan semua file, termasuk yang tersembunyi.
   - Catat direktori aktif, isi folder, dan file tersembunyi (jika ada).
 ## direktori aktif : . snap-private-tmp
 ## isi folder :
   - .. systemd-private-cd380bf617bf44ccdb05b4161b5fd4ee7-systemd-logind.service-y56o3r
   - .. systemd-private-cd380bf617bf44ccdb05b4161b5fd4ee7-systemd-resolved.service-IrDi60
   - .. systemd-private-cd380bf617bf44ccdb05b4161b5fd4ee7-systemd-timesyncd.service-MbYFxS
   - .. systemd-private-cd380bf617bf44ccdb05b4161b5fd4ee7-wsl-pro.service-q85gKw
 ## file tersembunyi :
   - .ICE-unix
   - .X11-unix
   - .XIM-unix
   - .font-unix 
     
**Eksperimen 2 – Membaca File**
   Jalankan perintah:
   ```bash
   cat /etc/passwd | head -n 5
   ```
   - Jelaskan isi file dan struktur barisnya (user, UID, GID, home, shell).
     > root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
1. user, username/nama login user.
   - root, dst.
2. UID, nomor identitas unik untuk user.
   - 0 (root), 1 (daemon), dst.
3. GID, nomor identitas grup untuk user, mengacu pada /etc/group.
   - 0 (root), 1 (daemon), dst.
4. home, lokasi folder pribadi user.
   - /root (root), /usr (daemon), /bin (bin), /dev (sys), /bin (sync)
5. shell, program shell yang dijalankan saat user login.
   - /bin/bash (root), /usr/sbin (daemon, bin, sys), /bin/sync (sync)

**Eksperimen 3 – Permission & Ownership**
   Buat file baru:
   ```bash
   echo "Hello <NAME><NIM>" > percobaan.txt
   ls -l percobaan.txt
   chmod 600 percobaan.txt
   ls -l percobaan.txt
   ```
   - Analisis perbedaan sebelum dan sesudah chmod.
     1. Sebelum chmod, kodenya berupa rw-r--r--
        > Artinya r, baca. w, tulis. Berarti memiliki akses untuk membaca dan menulis.
     2. Setelah chmod, kodenya berupa r-------
        > Berarti memiliki akses hanya baca
   - Ubah pemilik file (jika memiliki izin sudo):
     > Tidak memiliki izin sudo.

   ```bash
   sudo chown root percobaan.txt
   ls -l percobaan.txt
   ```
   - Catat hasilnya.
     > Tidak memiliki izin sudo.

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.
1. Sistem hak akses di Linux yang mengatur siapa yang dapat membaca (read), menulis (write), atau mengeksekusi (execute) file dan direktori di sistem file (filesystem).
2. UID dan GID memiliki angka yang sama, tetapi berbeda setiap username.

---
## Tugas 
1. Dokumentasikan hasil seluruh perintah pada tabel observasi di `laporan.md`.
   ![Screenshot hasil](<screenshots/tabel_observasi_fs_permission.png>)
2. Jelaskan fungsi tiap perintah dan arti kolom permission (`rwxr-xr--`).
   - rwx, milil pemilik, memiliki akses baca, tulis, jalankan
   - r-x, milik	grup, memiliki akses baca, jalankan
   - r--	milik lainnya, memiliki	hanya baca
3. Analisis peran `chmod` dan `chown` dalam keamanan sistem Linux.
   - chmod, mengatur izin akses (permissions)
   - chown, mengatur kepemilikan (ownership)
4. Upload hasil dan laporan ke repositori Git sebelum deadline.


## Quiz
1. Apa fungsi dari perintah `chmod`?
   **Jawaban:**  mengatur izin akses (permissions).
2. Apa arti dari kode permission `rwxr-xr--`?   
   **Jawaban:**  memilik arti dari sistem menunjukkan izin akses (permissions) untuk suatu file atau direktori.
3. Jelaskan perbedaan antara `chown` dan `chmod`.  
   **Jawaban:** chmod, mengatur izin akses (permissions). Sedangkan, chown, mengatur kepemilikan (ownership).

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?
  > Menganalisis perintah-perintah yang diberikan.
- Bagaimana cara Anda mengatasinya?
  > Mengamati dengan cermat hasil dari perintah-perintah dan mengamati dengan cermat perbedaan dari setiap perintah  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
