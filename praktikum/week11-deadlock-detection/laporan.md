
# Laporan Praktikum Minggu 11
Topik: Simulasi dan Deteksi Deadlock

---

## Identitas
- **Nama**  : Hendra Farid Hidayat  
- **NIM**   : 250320572  
- **Kelas** : 1DSRA

---

## Tujuan
1. Membuat program sederhana untuk mendeteksi deadlock.
2. Menjalankan simulasi deteksi deadlock dengan dataset uji.
3. Menyajikan hasil analisis deadlock dalam bentuk tabel.
4.Memberikan interpretasi hasil uji secara logis dan sistematis.
5. Menyusun laporan praktikum sesuai format yang ditentukan.

---

## Dasar Teori
1. Menurut Silberschatz, Deadlock adalah kondisi global system state, bukan kesalahan lokal satu proses. Implikasinya adalah simulasi akan membantu untuk mencegah terjadinya deadlock di masa depan.
2. Berdasarkan OSTEP sistem dibagi menjadi, safe state, yaitu masih ada urutan eksekusi yang memungkinkan semua proses selesai. Unsafe state, berpotensi deadlock. Deadlock state, tidak ada urutan yang memungkinkan progres.
3. Menurut OSTEP, simulasi dilakukan karena, pencegahan berisfat mahal dan tidak fleksibel. Penghindaran memerlukan info maksimum (Banker’s Algorithm) sehingga kurang efisien. Deteksi dan recovery, lebih realistis untuk sistem umum

---

## Langkah Praktikum
1. **Menyiapkan Dataset**

   Gunakan dataset sederhana yang berisi:
   - Daftar proses  
   - Resource Allocation  
   - Resource Request / Need

   Contoh tabel:

   | Proses | Allocation | Request |
   |:--:|:--:|:--:|
   | P1 | R1 | R2 |
   | P2 | R2 | R3 |
   | P3 | R3 | R1 |

2. **Implementasi Algoritma Deteksi Deadlock**

   Program minimal harus:
   - Membaca data proses dan resource.  
   - Menentukan apakah sistem berada dalam kondisi deadlock.  
   - Menampilkan proses mana saja yang terlibat deadlock.

3. **Eksekusi & Validasi**

   - Jalankan program dengan dataset uji.  
   - Validasi hasil deteksi dengan analisis manual/logis.  
   - Simpan hasil eksekusi dalam bentuk screenshot.

4. **Analisis Hasil**

   - Sajikan hasil deteksi dalam tabel (proses deadlock / tidak).  
   - Jelaskan mengapa deadlock terjadi atau tidak terjadi.  
   - Kaitkan hasil dengan teori deadlock (empat kondisi).

5. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 11 - Deadlock Detection"
   git push origin main
   ```

---

## Kode / Perintah
```
processes = {
    "P1": {"allocation": "R1", "request": "R2"},
    "P2": {"allocation": "R2", "request": "R3"},
    "P3": {"allocation": "R3", "request": "R1"},
}

wait_for_graph = {}

for p1, data1 in processes.items():
    wait_for_graph[p1] = []
    for p2, data2 in processes.items():
        if data1["request"] == data2["allocation"]:
            wait_for_graph[p1].append(p2)

def detect_cycle(graph):
    visited = set()
    stack = set()

    def dfs(node):
        if node in stack:
            return True
        if node in visited:
            return False

        visited.add(node)
        stack.add(node)

        for neighbor in graph[node]:
            if dfs(neighbor):
                return True

        stack.remove(node)
        return False

    for node in graph:
        if dfs(node):
            return True
    return False

print("Wait-For Graph:")
for p, waits in wait_for_graph.items():
    print(f"{p} -> {waits}")

if detect_cycle(wait_for_graph):
    print("\n⚠️ Deadlock TERDETEKSI!")
else:
    print("\n✅ Tidak ada deadlock.")
```

---

## Hasil Eksekusi
![Screenshot hasil](<screenshots/deadlock_detection.png>)

---

## Analisis
- Sajikan hasil deteksi dalam tabel (proses deadlock / tidak).
Berdasarkan simulasi wait-for graph, hasilnya sebagai berikut:
| Proses | Menunggu Proses |  Status  |
| :----: | :-------------: | :------: |
|   P1   |        P2       | Deadlock |
|   P2   |        P3       | Deadlock |
|   P3   |        P1       | Deadlock |
 
- Jelaskan mengapa deadlock terjadi atau tidak terjadi.
Terjadi karena adanya kondisi circular wait.
Terjadi kondisi:
P1 menahan R1, menunggu R2 (dipegang P2)
P2 menahan R2, menunggu R3 (dipegang P3)
P3 menahan R3, menunggu R1 (dipegang P1)
Sehingga, membentuk rantai ketergantungan melingkar: P1 → P2 → P3 → P1. Karena, tidak ada proses yang bisa maju tanpa resource yang dipegang proses lain, maka semua proses berhenti selamanya dan deadlock terjadi.
- Kaitkan hasil dengan teori deadlock (empat kondisi).
Menurut teori deadlock (Silberschatz & Tanenbaum), deadlock terjadi jika dan hanya jika keempat kondisi berikut terpenuhi secara bersamaan:
|  No | Kondisi Deadlock     | Terpenuhi? | Penjelasan                                                  |
| :-: | :------------------- | :--------: | :---------------------------------------------------------- |
|  1  | **Mutual Exclusion** |    ✅ Ya    | Resource (R1, R2, R3) hanya bisa dipakai satu proses        |
|  2  | **Hold and Wait**    |    ✅ Ya    | Proses memegang satu resource sambil menunggu resource lain |
|  3  | **No Preemption**    |    ✅ Ya    | Resource tidak bisa diambil paksa dari proses               |
|  4  | **Circular Wait**    |    ✅ Ya    | P1 → P2 → P3 → P1                                           |

---

## Kesimpulan
1. Simulasi deteksi deadlock diperlukan karena sistem operasi tidak dapat mengetahui secara pasti apakah suatu alokasi sumber daya akan menyebabkan deadlock di masa depan sehingga simulasi dilakukan untuk mendeteksi ada/tidaknya deadlock supaya tidak terjadi di masa depan.
2. Kondisi deadlock terjadi hanya jika keempat kondisi (syarat) terpenuhi.

---

## Quiz
1. Apa perbedaan antara deadlock prevention, avoidance, dan detection?
   **Jawaban:**
- Prevention: Memastikan salah satu dari 4 syarat deadlock (Mutual Exclusion, Hold & Wait, No Preemption, Circular Wait) tidak terpenuhi. Sangat ketat dan bisa menurunkan utilitas sistem
- Avoidance: Sistem memeriksa setiap permintaan resource secara dinamis. Jika permintaan tersebut berpotensi membawa sistem ke "Unsafe State", permintaan ditunda.
- Detection: Membiarkan deadlock terjadi, lalu menjalankan algoritma secara periodik untuk mendeteksi dan memulihkannya.
2. Mengapa deteksi deadlock tetap diperlukan dalam sistem operasi?
   **Jawaban:** Pendeteksian deadlock dibutuhkan sebagai kompromi antara keamanan dan efisiensi sistem , terutama pada lingkungan multi-proses dan multi-sumber daya kompleks, saat skrip dan kinerja menjadi prioritas utama. 
3. Apa kelebihan dan kekurangan pendekatan deteksi deadlock?
   **Jawaban:**
- Kelebihan: Penggunaan resource lebih optimal (tidak dibatasi di awal).
- Kekurangan: Ada biaya overhead untuk menjalankan algoritma deteksi secara berkala. Jika deadlock terdeteksi, pemulihannya (recovery) bisa menyebabkan kehilangan data jika proses harus dihentikan paksa.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
