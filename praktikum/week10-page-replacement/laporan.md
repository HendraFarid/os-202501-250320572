
# Laporan Praktikum Minggu 10
Topik: Page Replacement 

---

## Identitas
- **Nama**  : Hendra Farid Hidayat
- **NIM**   : 250320572
- **Kelas** : 1DSRA

---

## Tujuan
1. Mengimplementasikan algoritma page replacement FIFO dalam program.
2. Mengimplementasikan algoritma page replacement LRU dalam program.
3. Menjalankan simulasi page replacement dengan dataset tertentu.
4. Membandingkan performa FIFO dan LRU berdasarkan jumlah *page fault*.
5. Menyajikan hasil simulasi dalam laporan yang sistematis.

---

## Dasar Teori
1. Silberschatz dkk. menyatakan bahwa tujuan utama algoritma page replacement adalah meminimalkan jumlah page fault, karena page fault sangat mahal dari sisi kinerja sistem.
2. Tanenbaum melihat page replacement sebagai konsekuensi langsung dari keterbatasan memori fisik dan meningkatnya jumlah proses. Sistem operasi harus membuat keputusan cerdas tentang halaman mana yang harus dikeluarkan dari memori.
3. Menurut OSTEP, keberhasilan algoritma diukur dari keseimbangan antara performa dan overhead.

---

## Langkah Praktikum
1. **Menyiapkan Dataset**

   Gunakan *reference string* berikut sebagai contoh:
   ```
   7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2
   ```
   Jumlah frame memori: **3 frame**.

2. **Implementasi FIFO**

   - Simulasikan penggantian halaman menggunakan algoritma FIFO.
   - Catat setiap *page hit* dan *page fault*.
   - Hitung total *page fault*.

3. **Implementasi LRU**

   - Simulasikan penggantian halaman menggunakan algoritma LRU.
   - Catat setiap *page hit* dan *page fault*.
   - Hitung total *page fault*.

4. **Eksekusi & Validasi**

   - Jalankan program untuk FIFO dan LRU.
   - Pastikan hasil simulasi logis dan konsisten.
   - Simpan screenshot hasil eksekusi.

5. **Analisis Perbandingan**

   Buat tabel perbandingan seperti berikut:

   | Algoritma | Jumlah Page Fault | Keterangan |
   |:--|:--:|:--|
   | FIFO | ... | ... |
   | LRU | ... | ... |


   - Jelaskan mengapa jumlah *page fault* bisa berbeda.
   - Analisis algoritma mana yang lebih efisien dan alasannya.

6. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 10 - Page Replacement FIFO & LRU"
   git push origin main
   ```

---

## Kode / Perintah
```bash
reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
frames = 3


def print_process_table(title, steps):
    print(f"\n{title}")
    print("+" + "-"*8 + "+" + "-"*10 + "+" + "-"*10 + "+" + "-"*10 + "+" + "-"*10 + "+")
    print("| Page   | Frame 1  | Frame 2  | Frame 3  | Status   |")
    print("+" + "-"*8 + "+" + "-"*10 + "+" + "-"*10 + "+" + "-"*10 + "+" + "-"*10 + "+")
    
    for page, mem, status in steps:
        print(f"| {page:<6} | {mem[0]:<8} | {mem[1]:<8} | {mem[2]:<8} | {status:<8} |")
    
    print("+" + "-"*8 + "+" + "-"*10 + "+" + "-"*10 + "+" + "-"*10 + "+" + "-"*10 + "+")


# ================= FIFO =================
def fifo_page_replacement(ref, frames):
    memory = ['-'] * frames
    fifo_index = 0
    steps = []
    page_fault = 0

    for page in ref:
        if page in memory:
            steps.append((page, memory.copy(), "HIT"))
        else:
            page_fault += 1
            memory[fifo_index] = page
            fifo_index = (fifo_index + 1) % frames
            steps.append((page, memory.copy(), "FAULT"))

    return page_fault, steps


# ================= LRU =================
def lru_page_replacement(ref, frames):
    memory = ['-'] * frames
    last_used = {}
    steps = []
    page_fault = 0

    for time, page in enumerate(ref):
        if page in memory:
            steps.append((page, memory.copy(), "HIT"))
        else:
            page_fault += 1
            if '-' in memory:
                index = memory.index('-')
            else:
                lru_page = min(last_used, key=last_used.get)
                index = memory.index(lru_page)
                del last_used[lru_page]

            memory[index] = page
            steps.append((page, memory.copy(), "FAULT"))

        last_used[page] = time

    return page_fault, steps


# ================= EKSEKUSI =================
fifo_fault, fifo_steps = fifo_page_replacement(reference_string, frames)
lru_fault, lru_steps = lru_page_replacement(reference_string, frames)

print_process_table("PROSES FIFO (First-In First-Out)", fifo_steps)
print_process_table("PROSES LRU (Least Recently Used)", lru_steps)

# ================= HASIL AKHIR =================
print("\nHASIL AKHIR")
print("+" + "-"*12 + "+" + "-"*14 + "+" + "-"*14 + "+")
print("| Algoritma | Jumlah Frame | Page Fault   |")
print("+" + "-"*12 + "+" + "-"*14 + "+" + "-"*14 + "+")
print(f"| FIFO      | {frames:^12} | {fifo_fault:^12} |")
print(f"| LRU       | {frames:^12} | {lru_fault:^12} |")
print("+" + "-"*12 + "+" + "-"*14 + "+" + "-"*14 + "+")
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](<screenshots/week10_page replacement.png>)

---
## Implementasi FIFO 
```bash
=== FIFO Page Replacement ===
Page: 7 -> Frames: [7] (Fault)
Page: 0 -> Frames: [7, 0] (Fault)
Page: 1 -> Frames: [7, 0, 1] (Fault)
Page: 2 -> Frames: [2, 0, 1] (Fault)
Page: 0 -> Frames: [2, 0, 1] (Hit)
Page: 3 -> Frames: [2, 3, 1] (Fault)
Page: 0 -> Frames: [2, 3, 0] (Fault)
Page: 4 -> Frames: [4, 3, 0] (Fault)
Page: 2 -> Frames: [4, 2, 0] (Fault)
Page: 3 -> Frames: [4, 2, 3] (Fault)
Page: 0 -> Frames: [0, 2, 3] (Fault)
Page: 3 -> Frames: [0, 2, 3] (Hit)
Page: 2 -> Frames: [0, 2, 3] (Hit)

=== HASIL AKHIR ===
Total Page Fault FIFO: 10
```

---

## Implementasi LRU 
```bash
=== LRU Page Replacement ===
Page: 7 -> Frames: [7] (Fault)
Page: 0 -> Frames: [7, 0] (Fault)
Page: 1 -> Frames: [7, 0, 1] (Fault)
Page: 2 -> Frames: [2, 0, 1] (Fault)
Page: 0 -> Frames: [2, 0, 1] (Hit)
Page: 3 -> Frames: [2, 0, 3] (Fault)
Page: 0 -> Frames: [2, 0, 3] (Hit)
Page: 4 -> Frames: [4, 0, 3] (Fault)
Page: 2 -> Frames: [4, 0, 2] (Fault)
Page: 3 -> Frames: [4, 3, 2] (Fault)
Page: 0 -> Frames: [0, 3, 2] (Fault)
Page: 3 -> Frames: [0, 3, 2] (Hit)
Page: 2 -> Frames: [0, 3, 2] (Hit)

=== HASIL AKHIR ===
Total Page Fault LRU : 9
```

---

## Analisis
 | Algoritma | Jumlah Page Fault | Keterangan |
   |:--|:--:|:--|
   | FIFO | 10 | Menggantikan halaman berdasarkan urutan masuk, paling pertama masuk akan diganti terlebih dahulu |
   | LRU | 9 | Menggantikan halaman berdasarkan periode pennggunaan, paling lama tidak digunakan akan diganti terlebih dahulu |

- Jelaskan mengapa jumlah *page fault* bisa berbeda.
> Hal ini dikarenakan cara keduanya memilih halaman (page) yang akan dikeluarkan dari memori sangat berbeda, sehingga respon terhadap pola akses memori juga berbeda. Berdasarkan keterangan tabel, FIFO mengeluarkan halaman yang pertama kali masuk terlebih dahulu. Sedangkan, LRU mengganti halaman yang paling lama digunakan. Misal saya memberi contoh, FIFO akan mengeluarkan barang yang paling lama berada di dalam laci meskipu masih dipakai. LRU akan mengeluarkan benda yang paling lama tidak dipakai dari dalam laci.
- Analisis algoritma mana yang lebih efisien dan alasannya.
> LRU lebih efisien dibanding FIFO karena menghasilkan jumlah page fault yang lebih sedikit dan lebih sesuai dengan pola akses memori program, meskipun implementasinya lebih kompleks.

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.
Berdasarkan percobaaan yang telah dilakukan, beberapa poin kesimpulannya : 
1. Menggunakan *reference string* yang sama , FIFO menghasilkan 6 page fault, LRU 9 fault.
2. Perbedaan disebabkan karena mekanisme keduanya yang berbeda. FIFO membuang halaman berdasarkan urutan masuk, sedangkan LRU berdasarkan periode paling lama tidak terpakainya suatu *page*.
3. FIFO lebih efisien karena fault lebih sedikit, mengurangi I/O, setelah percobaan dilakukan. Namun, umumnya LRU lebih efisien secara umum berkat prinsip lokalitas, pemilihan algoritma harus disesuaikan dengan pola akses beban kerja untuk optimasi memori sistem operasi.

---

## Quiz
1. Apa perbedaan utama FIFO dan LRU?
   **Jawaban:**
- FIFO: Menggantikan halaman yang paling lama masuk ke dalam memori, tanpa mempertimbangkan kapan halaman tersebut terakhir digunakan. Algoritma ini sederhana dan mudah diimplementasikan, tetapi dapat kurang efisien karena tidak memanfaatkan pola akses penggunaan halaman.
- LRU: Menggantikan halaman yang paling lama tidak digunakan (berdasarkan waktu akses terakhir). Algoritma ini lebih mempertimbangkan prinsip lokalitas temporal, di mana halaman yang baru saja diakses cenderung digunakan lagi, sehingga sering menghasilkan lebih sedikit page fault.
2. Mengapa FIFO dapat menghasilkan Belady’s Anomaly?
   **Jawaban:** FIFO tidak mempertimbangkan frekuensi atau pola penggunaan halaman, sehingga penambahan jumlah frame justru dapat meningkatkan jumlah page fault (Belady’s Anomaly).
3. Mengapa LRU umumnya menghasilkan performa lebih baik dibanding FIFO?
   **Jawaban:** LRU bekerja berdasarkan perilaku nyata dari sebuah program, sedangkan FIFO hanya bekerja berdasarkan urutan Waktu tanpa logika kegunaan.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?
> Memahami mengenai Belady’s Anomaly. 
- Bagaimana cara Anda mengatasinya?  
> Menggunakan analogi-analogi sederhana untuk membantu memahami Belady’s Anomaly. 
---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
