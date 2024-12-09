import dash
from dash import html

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div(
    style={"width": "100%", "height": "100vh", "margin": 0, "padding": 0},
    children=[
        html.Iframe(
            # Using a relative path since viewer.html and the PDF are in the same directory
            src="/assets/web/viewer.html?file=your_local_file.pdf",
            style={"width": "100%", "height": "100%", "border": "none"}
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
