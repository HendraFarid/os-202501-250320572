import time

print("=== Program Uji CPU & Memori ===")

# =====================
# UJI CPU
# =====================
print("\n[UJI CPU] Komputasi berulang dimulai...")
start_time = time.time()

counter = 0
while True:
    counter += 1
    # operasi matematis sederhana (membebani CPU)
    result = counter * counter

    if counter % 10_000_000 == 0:
        elapsed = time.time() - start_time
        print(f"Iterasi: {counter:,} | Waktu: {elapsed:.2f} detik")

# =====================
# UJI MEMORI (opsional, aktifkan jika perlu)
# =====================
"""
print("\n[UJI MEMORI] Alokasi memori bertahap...")
memory_hog = []

try:
    while True:
        memory_hog.append("X" * 10**6)  # alokasi ~1 MB
        print(f"Memori teralokasi: {len(memory_hog)} MB")
        time.sleep(0.2)
except MemoryError:
    print("MemoryError: Batas memori tercapai!")
"""