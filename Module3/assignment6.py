import pandas as pd
import matplotlib.pyplot as plt


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
df = pd.read_csv('Datasets/wheat.data', header=0, index_col = 0)

#
# TODO: Drop the 'id' feature, if you included it as a feature
# (Hint: You shouldn't have)
# 

# N/A

#
# TODO: Compute the correlation matrix of your dataframe
# 

corr_mat = df.corr()


#
# TODO: Graph the correlation matrix using imshow or matshow
# 

plt.imshow(corr_mat, interpolation='none', cmap=plt.cm.Blues)
plt.colorbar()
ticks = [ x for x in range(len(df.columns))]
plt.xticks(ticks, df.columns, rotation='vertical')
plt.yticks(ticks, df.columns)

plt.show()

# min
corr_mat.min().idxmax()

