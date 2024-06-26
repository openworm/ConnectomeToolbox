import plotly.express as px
import pandas as pd

df = pd.read_excel('cect/data/CElegansNeuronTables.xls')
fig = px.density_contour(df, x="Origin", y="Target")
fig.update_traces(contours_coloring="fill", contours_showlabels = True)
fig.show()

df = pd.read_csv('cect/data/herm_full_edgelist_MODIFIED.csv')
fig = px.density_contour(df, x="Source", y="Target")
fig.update_traces(contours_coloring="fill", contours_showlabels = True)
fig.show()