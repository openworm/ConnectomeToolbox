## The pharynx of Caenorhabditis elegans
_Donna G. Albertson and J. N. Thompson_ 

_Published: 10 August 1976  https://doi.org/10.1098/rstb.1976.0085_

```python
fig = go.Figure(data =
    go.Contour(
        z=[[10, 10.625, 12.5, 15.625, 20],
           [5.625, 6.25, 8.125, 11.25, 15.625],
           [2.5, 3.125, 5., 8.125, 12.5],
           [0.625, 1.25, 3.125, 6.25, 10.625],
           [0, 0.625, 2.5, 5.625, 10]],
        x=[-9, -6, -5 , -3, -1], # horizontal axis
        y=[0, 1, 4, 5, 7] # vertical axis
    ))
with open("./docs/assets/contour.json", "w") as f:
    f.write(fig.to_json())
```
```plotly
--8<-- "./assets/contour.json"
```
