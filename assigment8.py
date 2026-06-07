import matplotlib.pyplot as plt
import numpy as np

# 1. Keshni va tasodifiy sonlar generatorini tozalash
plt.close("all")
np.random.seed(None)

# 2. Tasodifiy ma'lumotlar generatori
n = 70
x_data = np.random.randint(10, 100, size=n)
y_data = np.random.randint(20, 200, size=n)
olchamlar = np.random.randint(50, 500, size=n)
ranglar = np.random.rand(n)

# Matplotlib-dagi barcha grafik shakllari (markerlar) ro'yxati
shakllar_ombori = ["o", "s", "^", "D", "X", "*", "p", "v", "P", "h"]

# HAR SAFAR RUN QILGANDA BARCHA NUQTALAR UCHUN BITTA YAGONA TASODIFIY SHAKL TANLASH
tanlangan_shakl = np.random.choice(shakllar_ombori)

# 3. Grafik oynasi parametrlari
plt.figure(figsize=(12, 7), dpi=100, facecolor="#f5f5f5")

# 4. SCATTER PLOT - BARCHA PARAMETRLARI BILAN
plt.scatter(
    x=x_data,  # X o'qi ma'lumotlari
    y=y_data,  # Y o'qi ma'lumotlari
    s=olchamlar,  # s (size): Nuqtalarning tasodifiy o'lchamlari
    c=ranglar,  # c (color): Nuqtalarning tasodifiy ranglari
    cmap="turbo",  # cmap: Ranglar palitrasi
    marker=tanlangan_shakl,  # HAR SAFAR RUN BO'LGANDA BUTKUL ALMASHADIGAN YAGONA SHAKL
    alpha=0.8,  # alpha: Shaffoflik darajasi
    linewidths=1.2,  # linewidths: Nuqta chetidagi chiziq qalinligi
    edgecolors="black",  # edgecolors: Nuqta atrofi (chegarasi) rangi
    label=f"Shakl turi: '{tanlangan_shakl}'",  # Legendda joriy shaklni ko'rsatish
)

# 5. Ranglar shkalasi (Colorbar) parametrlari
cbar = plt.colorbar(orientation="vertical", pad=0.02, shrink=0.85)
cbar.set_label("Dinamik ranglar gradienti", fontsize=10, fontweight="bold")

# 6. Sarlavha va O'q nomlari parametrlari
plt.title(
    "Har safar umumiy shakli va ma'lumotlari o'zgaruvchan Scatter Plot",
    fontsize=14,
    fontweight="bold",
    pad=15,
)
plt.xlabel("X tasodifiy ko'rsatkich", fontsize=11, labelpad=8)
plt.ylabel("Y tasodifiy ko'rsatkich", fontsize=11, labelpad=8)

# 7. Orqa fondagi katakchalar (Grid) parametrlari
plt.grid(
    visible=True,
    which="major",
    axis="both",
    color="gray",
    linestyle="--",
    linewidth=0.5,
    alpha=0.4,
)

# 8. Legend (Tushuntirish yozuvi) parametrlari
plt.legend(
    loc="upper left", frameon=True, facecolor="white", edgecolor="black", shadow=True
)

plt.tight_layout()

# 9. Grafikni ekranga chiqarish
plt.show()