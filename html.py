
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(data=go.Bar(y=[2, 3, 1]))
pio.write_html(fig, file='index.html', auto_open=False)
