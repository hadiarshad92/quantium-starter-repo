
import pandas as pd

from dash import Dash, dcc, html
import plotly.express as px

# Load the formatted sales data
df = pd.read_csv("formatted_sales.csv")

# Convert 'date' column to datetime
df["date"] = pd.to_datetime(df["date"])

# Group by date and sum sales
sales_by_date = df.groupby("date")["sales"].sum().reset_index()

# Create line chart
fig = px.line(
    sales_by_date,
    x="date",
    y="sales",
    title="Daily Sales of Pink Morsel",
    labels={"date": "Date", "sales_value": "Sales Value ($)"}
)

# Add a vertical line for the price increase date
fig.add_shape(
    type="line",
    x0=pd.to_datetime("2021-01-15"),
    x1=pd.to_datetime("2021-01-15"),
    y0=0,
    y1=1,
    xref='x',
    yref='paper',  # 'paper' makes y go from 0 to 1 relative to the height of the plot
    line=dict(color="red", width=2, dash="dash")
)

# Optional annotation
fig.add_annotation(
    x=pd.to_datetime("2021-01-15"),
    y=1,
    xref='x',
    yref='paper',
    text="Price Increase",
    showarrow=False,
    font=dict(color="red"),
    align="left"
)


# Initialize Dash app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualiser", style={"textAlign": "center"}),
    dcc.Graph(figure=fig)
])

# Run server
if __name__ == '__main__':
    app.run(port=8051,debug=True)
