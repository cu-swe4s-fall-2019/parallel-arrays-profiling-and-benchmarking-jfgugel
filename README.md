# parallel-arrays-profiling-and-benchmarking
Parallel Arrays, Profiling, and Benchmarking

Files:
- https://github.com/swe4s/lectures/blob/master/data_integration/gtex/GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz?raw=true
- https://storage.googleapis.com/gtex_analysis_v8/annotations/GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt


# plot_gtex.py:
    # plot_gtex.py contains a linear search and a binary search to search arrays from GTEx
    # Cprofile was run to determine whether linear search or binary search is faster.
    # Binary search is faster. 
    # File contains benchmarking to measure the time of linear versus binary search
    # Uses data_viz.py to display data in boxplots
    
# data_viz.py:
    # data_viz.py was created to produce multiple blox plots
    # X axis label, Y axis label, and Title added

# plot_gtex.linear_search.py
    # Contains resutls of profile for plot_gtex.py