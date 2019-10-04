import sys
import matplotlib
matplotlib.use('Agg')
import time
#import data_viz
import gzip


def linear_search(key, L):
    hit = -1
    for i in range(len(L)):
        curr = L[i]
        if key == curr:
            return i
    return -1
    pass

def binary_serach(key, D):
    lo = -1
    hi = len(D)
    while (hi - lo > 1):
        mid = (hi + lo)//2
        
        if key == D[mid]:
            return D[mid]
        
        if ( key < D[mid])
            hi = mid
        else: lo = mid
        
    return -1 
    pass


data_file_name='GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz'
sample_info_file_name='GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt'

group_col_name = 'SMTS'
sample_id_col_name = 'SAMPID'

gene_name = 'ACTA2'


samples = []
sample_info_header = None
for l in open(sample_info_file_name):
    if sample_info_header == None:
        sample_info_header = l.rstrip().split('\t')
    else:
        samples.append(l.rstrip().split('\t'))
        

group_col_idx = linear_search(group_col_name, sample_info_header)


sample_id_col_idx = linear_search(sample_id_col_name, sample_info_header)

groups = []
members = []

for row_idx in range(len(samples)):
    sample = samples[row_idx]
    sample_name = sample[sample_id_col_idx]
    curr_group = sample[group_col_idx]


    
    curr_group_idx = linear_search(curr_group, groups)

    if curr_group_idx == -1:
        curr_group_idx = len(groups)
        groups.append(curr_group)
        members.append([])

    members[curr_group_idx].append(sample_name)

version = None
dim = None
data_header = None

gene_name_col = 1

group_counts = [ [] for i in range(len(groups)) ]

for l in gzip.open(data_file_name, 'rt'):
    if version == None:
        version = l
        continue

    if dim == None:
        dim = [int(x) for x in l.rstrip().split()]
        continue

    if data_header == None:
        data_header = l.rstrip().split('\t')
        continue


    A = l.rstrip().split('\t')


    if A[gene_name_col] == gene_name:
        for group_idx in range(len(groups)):
            for member in members[group_idx]:
                member_idx = linear_search(member, data_header)
                if member_idx != -1
                    group_counts[group_idx].append(int(A[member_idx]))

        break 







#def binary_serach(key, D):
    #lo = -1
    #hi = len(D)
    #while (hi - lo > 1):
        #mid = (hi + lo)//2
        
        #if key == D[mid]:
            #return D[mid]
        
        #if ( key < D[mid])
            #hi = mid
        #else: lo = mid
        
    #return -1 

    #pass


#def main():


#if __name__ == '__main__':
    #main()
