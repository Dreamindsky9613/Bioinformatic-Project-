import sys
import gzip
from Bio import SeqIO
import numpy as np

def calculate_metrics(fastq_file, output_file):
    # Dosya .gz ise ona göre açıyoruz
    handle = gzip.open(fastq_file, "rt") if fastq_file.endswith(".gz") else open(fastq_file, "r")
    
    with open(output_file, 'w') as f:
        f.write("Read_ID,Length,GC_Content,Mean_Quality\n")
        
        # SeqIO.parse belleği korumak için iteratör kullanır
        for record in SeqIO.parse(handle, "fastq"):
            length = len(record.seq)
            if length == 0: continue
            
            # GC içeriği hesaplama
            g_count = record.seq.count('G') + record.seq.count('g')
            c_count = record.seq.count('C') + record.seq.count('c')
            gc = (g_count + c_count) / length * 100
            
            # Kalite puanı (Long-read verilerinde çok hızlı hesaplama)
            qual_scores = record.letter_annotations["phred_quality"]
            mean_qual = np.mean(qual_scores) if qual_scores else 0
            
            f.write(f"{record.id},{length},{gc:.2f},{mean_qual:.2f}\n")
    handle.close()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Kullanım: python calculate_metrics.py input.fastq output.csv")
    else:
        calculate_metrics(sys.argv[1], sys.argv[2])

