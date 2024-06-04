import plotly.express as px
import plotly.graph_objects as go

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 size='petal_length', hover_data=['petal_width'])
with open("cect\data\witvliet_2020_8.json", "w") as f:
    f.write(fig.to_json())
