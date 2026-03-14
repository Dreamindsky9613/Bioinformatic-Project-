nextflow.enable.dsl=2

params.fastq = "data/*.fastq.gz" 
params.outdir = "results"

process QC_LONGREAD {
    publishDir "${params.outdir}/qc", mode: 'copy'

    input:
    path fastq

    output:
    path "NanoPlot_reports"

    script:
    """
    NanoPlot --fastq $fastq -o NanoPlot_reports
    """
}

process CALCULATE_METRICS {
    publishDir "${params.outdir}/metrics", mode: 'copy'

    input:
    path fastq

    output:
    path "read_metrics.csv"

    script:
    """
    python ${baseDir}/calculate_metrics.py $fastq read_metrics.csv
    """
}

workflow {
    fastq_ch = Channel.fromPath(params.fastq)
    
    QC_LONGREAD(fastq_ch)
    CALCULATE_METRICS(fastq_ch)
}
