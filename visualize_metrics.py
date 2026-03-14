import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 1. Veriyi Yükle
data_path = "results_snakemake/metrics/read_metrics.csv" # Veya results/metrics/
if not os.path.exists(data_path):
    print(f"Hata: {data_path} bulunamadı!")
    exit()

df = pd.read_csv(data_path)

# 2. İstatistikleri Hesapla ve Yazdır
metrics = ['Length', 'GC_Content', 'Mean_Quality']
print("--- TEMEL İSTATİSTİKLER ---")
summary = df[metrics].agg(['mean', 'median', 'std', 'min', 'max'])
print(summary)
summary.to_csv("results_snakemake/metrics/summary_statistics.csv")

# 3. Görselleştirme Ayarları
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# --- Grafik 1: Read Lengths (Histogram + KDE) ---
sns.histplot(df['Length'], kde=True, ax=axes[0], color='skyblue')
axes[0].set_title(f"Read Length Distribution\n(Mean: {df['Length'].mean():.2f})")
axes[0].set_xlabel("Length (bp)")

# --- Grafik 2: GC Content (Histogram + KDE) ---
sns.histplot(df['GC_Content'], kde=True, ax=axes[1], color='salmon')
axes[1].set_title(f"GC Content Distribution\n(Mean: {df['GC_Content'].mean():.2f}%)")
axes[1].set_xlabel("GC Content (%)")

# --- Grafik 3: Mean Quality Scores (Boxplot) ---
sns.boxplot(y=df['Mean_Quality'], ax=axes[2], color='lightgreen')
axes[2].set_title(f"Read Quality Scores\n(Median: {df['Mean_Quality'].median():.2f})")
axes[2].set_ylabel("Phred Quality Score")

plt.tight_layout()
plt.savefig("results_snakemake/metrics/data_visualization.png")
print("\nGrafik 'results_snakemake/metrics/data_visualization.png' olarak kaydedildi.")
plt.show()

