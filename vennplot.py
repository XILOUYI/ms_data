#Import libraries
#import matplotlib_venn as venn
from matplotlib_venn import venn2, venn2_circles
from matplotlib_venn import venn3, venn3_circles
from matplotlib import pyplot as plt
import pandas as pd
df1 = pd.read_csv('data1.csv')
df2 = pd.read_csv('data2.csv')

set1 = set(df1.carat)
set2 = set(df2.carat)
# defining sets for both subjects
#English = {'John', 'Amy', 'Howard', 'Lucy', 'Alice', 'George', 'Jacob', 'Rajesh', 'Remy', 'Tom'}
#French = {'Arthur', 'Leonard', 'Karan', 'Debby', 'Bernadette', 'Alice', 'Ron', 'Penny', 'Sheldon', 'John'}
venn2([set1,set2])
plt.show()
