RNA-seq Analysis of Anti-PD-1 Response in NSCLC (GSE126044)
Project Overview

This project investigates transcriptional differences associated with response to anti-PD-1 immunotherapy in non-small cell lung cancer (NSCLC) using publicly available RNA-seq data from GSE126044.

The original study focused on genome-wide DNA methylation profiling and identified promoter and enhancer methylation signatures associated with response to nivolumab or pembrolizumab treatment. In this project, I performed an independent transcriptomic analysis of the same cohort to determine whether responders and non-responders exhibit distinct gene expression and pathway-level immune signatures prior to treatment.

Original Study

This project reanalyzes transcriptomic data from:

Cho JW, Hong MH, Ha SJ, et al. Genome-wide identification of differentially methylated promoters and enhancers associated with response to anti-PD-1 therapy in non-small cell lung cancer. Experimental & Molecular Medicine. 2020;52(9):1550–1563. doi:10.1038/s12276-020-00493-8.

The original study focused on epigenetic mechanisms of immunotherapy response and identified promoter and enhancer methylation signatures associated with clinical benefit from PD-1 blockade. In contrast, this project examines the corresponding RNA-seq data to determine whether transcriptomic immune activation signatures support the epigenetic findings.

Performed an independent transcriptomic re-analysis of publicly available RNA-seq data from the cohort described in Cho et al. (2020) using Python-based bioinformatics workflows. Built an end-to-end RNA-seq pipeline including GEO acquisition, metadata curation, PCA, differential expression (PyDESeq2), volcano visualization, and GSEA pathway analysis. Independently recovered immune-related pathways reported in the original study, including antigen presentation and T-cell activation programs associated with response to anti-PD-1 therapy in NSCLC.


Research Question

Can pre-treatment transcriptional profiles distinguish responders from non-responders to anti-PD-1 therapy, and do these transcriptional patterns support the epigenetic mechanisms proposed in the original study?

Dataset

Study: GSE126044

Samples: 16 NSCLC tumors

5 responders
11 non-responders

Technology:

Bulk RNA-seq
Raw count matrix (GRCh38)
Pre-treatment tumor samples
Analysis Workflow
Raw RNA-seq Counts
        ↓
Quality Control & Filtering
        ↓
Log2 Transformation
        ↓
Metadata Construction
        ↓
Principal Component Analysis (PCA)
        ↓
Differential Expression Analysis (PyDESeq2)
        ↓
Volcano Plot Visualization
        ↓
Gene Set Enrichment Analysis (GSEA)
        ↓
Biological Interpretation
Methods
Data Processing

Raw count matrices were imported into Python and processed using Pandas and NumPy.

Steps included:

Removal of missing values
Conversion to numeric count matrices
Gene filtering
Log2(count + 1) transformation for exploratory analyses
Exploratory Analysis

Principal Component Analysis (PCA) was performed to assess global transcriptional structure and determine whether responder and non-responder samples exhibit distinct expression profiles.

Differential Expression

Differential expression analysis was performed using PyDESeq2.

Comparison:

Responder vs Non-Responder

Outputs:

Log2 fold change
Wald test p-values
Benjamini-Hochberg adjusted p-values (FDR)
Pathway Analysis

Gene Set Enrichment Analysis (GSEA) was performed using GSEApy with ranked differential expression statistics.

Databases:

KEGG pathways
Gene Ontology (GO)
Results
Figure 1 — Principal Component Analysis

PCA demonstrated partial separation between responders and non-responders, suggesting the presence of underlying transcriptional differences while also highlighting substantial biological heterogeneity within the cohort.

Figure 2 — Differential Expression Volcano Plot

Differential expression analysis identified genes exhibiting altered expression between treatment response groups. Individual gene-level signals were relatively modest, consistent with the limited sample size of the cohort.

Figure 3 — GSEA Pathway Analysis

Pathway enrichment analysis revealed strong immune-related signatures among genes associated with treatment response.

Top enriched pathways included:

Antigen processing and presentation
Natural killer cell mediated cytotoxicity
Th1 and Th2 cell differentiation
Hematopoietic cell lineage
Allograft rejection
Graft-versus-host disease

These pathways collectively indicate enhanced immune activation in tumors associated with clinical response to PD-1 blockade.

Biological Interpretation

The original publication reported extensive differential methylation of promoters and enhancers between responders and non-responders, highlighting the importance of epigenetic regulation in immunotherapy response.

My independent transcriptomic analysis identified enrichment of immune-related pathways involved in:

Antigen presentation
T-cell differentiation
Cytotoxic immune responses
Immune cell activation

These findings are consistent with the hypothesis that epigenetic remodeling influences transcriptional programs governing anti-tumor immunity.

Notably, pathway-level signals were substantially stronger than individual gene-level effects, illustrating the value of enrichment-based approaches for detecting coordinated biological processes in small clinical cohorts.

Limitations

Several limitations should be considered:

Small sample size (n = 16) limits statistical power.
Bulk RNA-seq cannot resolve cell-type-specific transcriptional programs.
Clinical response likely reflects complex interactions between tumor cells and the tumor microenvironment.
Findings should be validated in independent immunotherapy cohorts.
Future Directions

Potential extensions of this work include:

Cell-type deconvolution of bulk RNA-seq profiles
Integration of methylation and transcriptomic datasets
Investigation of biomarkers reported in the original study, including CYTIP and TNFSF8
Validation using additional NSCLC immunotherapy datasets
Development of predictive response models using multi-omic features
Technologies
Python
Pandas
NumPy
Matplotlib
Scikit-learn
PyDESeq2
GSEApy
Key Takeaway

This project demonstrates an end-to-end RNA-seq analysis workflow, from raw sequencing counts through differential expression and pathway enrichment analysis. The results support the hypothesis that pre-treatment immune activation programs contribute to clinical response to anti-PD-1 therapy and provide transcriptomic context for epigenetic mechanisms reported in the original study.