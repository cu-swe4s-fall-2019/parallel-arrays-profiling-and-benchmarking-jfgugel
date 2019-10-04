import sys
import matplotlib
matplotlib.use('Agg')
import time
import data_viz
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
        
        if (key < D[mid]):
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
                if member_idx != -1:
                    group_counts[group_idx].append(int(A[member_idx]))

        break 


fig = plt.figure(figsize=(10,3), dpi=300)

ax = fig.add_subplot(1,1,1)

ax.boxplot(group_counts)

plt.savefig(ACTA2 + '.ls.png', bbox_inches='tight')


def main():
    D_num = int(sys.argv[1])
    D = [random.randint(0,1000000) for x in range(D_num)]



    Q_num = int(sys.argv[2])
    Q = [D[random.randint(0,D_num - 1)] for x in range(Q_num)]



    op = sys.argv[3]



    if op == 'L':



        t0 = time.time() 
        for q in Q:
            linear_search(q, D)
        t1 = time.time()
        print(t1-t0)



    elif op == 'B':
        t0 = time.time() 



        t0_sort = time.time() 
        D.sort()
        t1_sort = time.time() 



        t0_search = time.time() 
        for q in Q:
            binary_search(q, D)
        t1_search = time.time() 



        t1 = time.time()
        print(t1-t0, (t1_sort-t0_sort)/(t1-t0), (t1_search-t0_search)/(t1-t0))




if __name__ == '__main__':
    main()
