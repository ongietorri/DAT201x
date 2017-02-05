#
# This code is intentionally missing!
# Read the directions on the course lab page!
#
import pandas as pd
import matplotlib.pyplot as plt
from pandas.tools.plotting import andrews_curves

# first question
df = pd.read_csv('Datasets/wheat.data', header=0, index_col = 0)

df_light = df.drop(['area', 'perimeter'], axis=1)

pd.tools.plotting.andrews_curves(df_light, 'wheat_type', alpha = .4)

plt.show()

# add area and perimeter columns
# In fact, we could simply use the original 'df', but this is just for the excercise
df_light['perimeter'] = df.perimeter
df_light['area'] = df.area

pd.tools.plotting.andrews_curves(df, 'wheat_type', alpha = .4)

plt.show()