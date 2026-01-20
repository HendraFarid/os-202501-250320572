
# Laporan Praktikum Minggu [X]
Topik: Virtualisasi Menggunakan Virtual Machine


---

## Identitas
- **Nama**  : Hendra Farid Hidayat  
- **NIM**   : 250320572
- **Kelas** : 1DSRA

---

## Tujuan
1. Menginstal perangkat lunak virtualisasi (VirtualBox/VMware).
2. Membuat dan menjalankan sistem operasi guest di dalam VM.
3. Mengatur konfigurasi resource VM (CPU, RAM, storage).
4. Menjelaskan mekanisme proteksi OS melalui virtualisasi.
5. Menyusun laporan praktikum instalasi dan konfigurasi VM secara sistematis.

---

## Dasar Teori
1. Silberschatz dkk. menjelaskan bahwa virtualisasi bekerja dengan menciptakan lapisan abstraksi antara perangkat keras fisik dan sistem operasi. Lapisan ini disebut Virtual Machine Monitor (VMM) atau Hypervisor.Silberschatz dkk. menjelaskan bahwa virtualisasi bekerja dengan menciptakan lapisan abstraksi antara perangkat keras fisik dan sistem operasi. Lapisan ini disebut Virtual Machine Monitor (VMM) atau Hypervisor.
2. Menurut Oracle VirtualBox Documentation, VirtualBox secara default memisahkan file sistem guest dari host dan mengontrol device access (USB, shared folder, network mode).

---

## Langkah Praktikum
1. **Instalasi Virtual Machine**
   - Instal VirtualBox atau VMware pada komputer host.  
   - Pastikan fitur virtualisasi (VT-x / AMD-V) aktif di BIOS.

2. **Pembuatan OS Guest**
   - Buat VM baru dan pilih OS guest (misal: Ubuntu Linux).  
   - Atur resource awal:
     - CPU: 1–2 core  
     - RAM: 2–4 GB  
     - Storage: ≥ 20 GB

3. **Instalasi Sistem Operasi**
   - Jalankan proses instalasi OS guest sampai selesai.  
   - Pastikan OS guest dapat login dan berjalan normal.

4. **Konfigurasi Resource**
   - Ubah konfigurasi CPU dan RAM.  
   - Amati perbedaan performa sebelum dan sesudah perubahan resource.

5. **Analisis Proteksi OS**
   - Jelaskan bagaimana VM menyediakan isolasi antara host dan guest.  
   - Kaitkan dengan konsep *sandboxing* dan *hardening* OS.

6. **Dokumentasi**
   - Ambil screenshot setiap tahap penting.  
   - Simpan di folder `screenshots/`.

7. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 12 - Virtual Machine"
   git push origin main
   ```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](<screenshots/display.png>)
![Screenshot hasil](<screenshots/storage.png>)
![Screenshot hasil](<screenshots/system.png>)

---

## Analisis Proteksi OS
   - Jelaskan bagaimana VM menyediakan isolasi antara host dan guest.
Virtual Machine (VM) menyediakan isolasi antara host dan guest melalui lapisan perangkat lunak yang disebut hypervisor (Virtual Machine Monitor/VMM). Isolasi ini memastikan bahwa sistem operasi guest berjalan seolah-olah berada pada komputer fisik tersendiri, tanpa akses langsung ke sistem host. Mekanismenya dijelaskan sebagai berikut:
1. Perantara antara hardware dan guest OS
> Hypervisor berada di antara hardware fisik dan guest OS. Semua akses guest ke CPU, memori, storage, dan perangkat I/O harus melalui hypervisor. Guest tidak dapat berkomunikasi langsung dengan hardware host.
2. Isolasi memori (memory isolation)
> Setiap VM memiliki ruang alamat memori virtual sendiri. Hypervisor, dibantu mekanisme proteksi hardware (seperti MMU dan page tables), memastikan guest tidak bisa membaca atau menulis memori milik host maupun VM lain.
3. Kontrol hak istimewa (privilege separation)
> Instruksi yang bersifat sensitif dari guest OS tidak dijalankan langsung di hardware. Instruksi tersebut akan ditangkap (trap) oleh hypervisor dan ditangani secara aman, sehingga guest tidak bisa mengambil alih kontrol sistem host.
4. Virtualisasi perangkat (device isolation)
> Perangkat keras (disk, jaringan, USB) disajikan sebagai perangkat virtual. Guest hanya berinteraksi dengan perangkat virtual ini, sementara hypervisor mengatur akses ke perangkat fisik yang sebenarnya.
5. Fault dan security isolation
> Jika terjadi kesalahan, crash, atau serangan di dalam guest OS, dampaknya terbatas pada VM tersebut. Host dan VM lain tetap berjalan normal karena berada dalam lingkungan terisolasi.
   - Kaitkan dengan konsep *sandboxing* dan *hardening* OS.****
1. Kaitan dengan konsep sandboxing
> Sandboxing adalah teknik menjalankan aplikasi atau sistem dalam lingkungan terbatas dan embatasi dampak jika terjadi kesalahan atau serangan. VM sebagai Sandbox dalam artian VM adalah sandbox tingkat sistem operasi. Guest OS dibatasi oleh hypervisor. Aktivitas berbahaya di dalam VM tidak langsung memengaruhi host.
2. Kaitan VM dengan Hardening OS
> Hardening OS adalah proses mengurangi attack surface, membatasi layanan dan hak akses, dan meningkatkan konfigurasi keamanan. VM mendukung Hardening dengan cara isolasi layanan dan setiap layanan berjalan di VM terpisah. Jika satu VM diserang, VM lain tetap aman. VM dapat diinstal dengan OS minimal, lebih sedikit service → lebih sedikit celah keamanan. Jika terjadi kompromi, sistem dapat dikembalikan.
---

## Kesimpulan
1. VM menyediakan isolasi host–guest dengan memanfaatkan hypervisor sebagai pengendali penuh akses resource, pemisahan memori dan hak akses, serta virtualisasi perangkat. Dengan demikian, setiap VM beroperasi secara independen dan aman, seolah-olah berjalan di mesin fisik yang terpisah.
2. VM memisahkan host dan guest melalui hypervisor, menyediakan lingkungan terkontrol untuk aplikasi/OS, mengurangi dampak serangan dan memperkuat keamanan, dan mencegah propagasi kesalahan dan serangan.

---

## Quiz
1. Apa perbedaan antara host OS dan guest OS?  
   **Jawaban:** Perbedaan dijelaskan dalam tabel
- Tabel Perbedaan host OS dan guest OS
| Aspek            | Host OS                  | Guest OS                |
| ---------------- | ------------------------ | ----------------------- |
| Lokasi instalasi | Langsung di hardware     | Di mesin virtual        |
| Akses hardware   | Langsung                 | Melalui Host OS         |
| Peran            | Mengendalikan sistem     | Sistem tamu             |
| Ketergantungan   | Tidak bergantung OS lain | Bergantung pada Host OS |
| Contoh           | Windows, Linux, macOS    | Linux/Windows di VM     |

3. Apa peran hypervisor dalam virtualisasi? 
   **Jawaban:**
- Peran Hypervisor dalam Virtualisasi
1. Menghubungkan hardware dengan Guest OS
> Hypervisor menjadi perantara antara perangkat keras fisik dan Guest OS, sehingga banyak sistem operasi dapat berjalan secara bersamaan di satu komputer.
2. Mengelola dan membagi sumber daya hardware
> Hypervisor mengatur pembagian, CPU, RAM, Storage, Perangkat I/O agar setiap VM mendapat jatah sumber daya tanpa saling mengganggu.
3. Isolasi antar mesin virtual
> Jika satu Guest OS mengalami crash atau error, VM lain tetap aman, karena hypervisor menjaga isolasi antar VM.
4. Menyediakan abstraksi hardware
> Guest OS seolah-olah melihat hardware sendiri, padahal sebenarnya itu adalah hardware virtual yang disediakan hypervisor.
5. Mengatur siklus hidup VM
> Hypervisor memungkinkan membuat VM, menjalankan / menghentikan VM, snapshot & rollback
3. Mengapa virtualisasi meningkatkan keamanan sistem?  
   **Jawaban:** Virtualisasi meningkatkan keamanan sistem karena ia memisahkan (mengisolasi) lingkungan eksekusi, membatasi dampak serangan, dan memberi kontrol yang lebih kuat terhadap sumber daya dan sistem operasi.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?
> Tidak ada.
- Bagaimana cara Anda mengatasinya?
> Tidak ada. 

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
