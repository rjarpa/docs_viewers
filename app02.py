import dash
from dash import html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    html.Div([
        #html.H1("PDF Viewer"),
        html.Iframe(
            id="pdf-viewer",
            src="/assets/pdfjs/web/viewer.html",
            #style={"width": "100%", "height": "500px", "border": "none"}
            style={"width": "100%", "height": "100%", "border": "none"}
        )
    ], style={"text-align": "center"})
])

if __name__ == "__main__":
    app.run_server(port=80,debug=True)
