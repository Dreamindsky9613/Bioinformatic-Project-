import glob

# data klasöründeki ilk .fastq.gz dosyasını otomatik bulur
RAW_DATA = glob.glob("data/*.fastq.gz")[0]
RESULT_DIR = "results_snakemake"

rule all:
    input:
        f"{RESULT_DIR}/qc/NanoPlot-report.html",
        f"{RESULT_DIR}/metrics/read_metrics.csv"

rule long_read_qc:
    input:
        RAW_DATA
    output:
        f"{RESULT_DIR}/qc/NanoPlot-report.html"
    shell:
        "NanoPlot --fastq {input} -o {RESULT_DIR}/qc"

rule calculate_metrics:
    input:
        RAW_DATA
    output:
        f"{RESULT_DIR}/metrics/read_metrics.csv"
    shell:
        "python calculate_metrics.py {input} {output}"
