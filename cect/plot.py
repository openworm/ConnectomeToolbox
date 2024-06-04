import plotly.express as px
import plotly.graph_objects as go

df = px.data.iris()
fig = px.scatter(df, ids="sepal_width", post="sepal_length", pre="species",
                 syn='petal_length', type=['petal_width'])
with open("cect\data\witvliet_2020_8.json", "w") as f:
    f.write(fig.to_json())
