import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

blood_counts = [1, 4, 3, 3, 3]
gene_name_1 = 'test_plot'
gene_name_2
gene_name_3
gene_name_4

width=3
height=3
fig = plt.figure(figsize=(width, height), dpi=300)
ax1 = fig.add_subplot(2, 2, 1)
ax1.boxplot(blood_counts)
plt.savefig(gene_name_1 + '.ls.png', bbox_inches='tight')

ax2 = fig.add_subplot(2, 2, 2)
ax2.boxplot(blood_counts)
plt.savefig(gene_name_2 + '.ls.png', bbox_inches='tight')

ax3 = fig.add_subplot(2, 2, 3)
ax3.boxplot(blood_counts)
plt.savefig(gene_name_3 + '.ls.png', bbox_inches='tight')

ax4 = fig.add_subplot(2, 2, 4)
ax4.boxplot(blood_counts)
plt.savefig(gene_name_4 + '.ls.png', bbox_inches='tight')
                
                
   