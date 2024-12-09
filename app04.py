from dash import Dash, html, Input, Output

app = Dash(__name__)

app.layout = html.Div([
    html.Iframe(
        id="pdf-viewer",
        src="",
        style={"width": "100%", "height": "600px", "border": "none"}
    ),
    html.Button("Load PDF", id="load-pdf"),
])

@app.callback(
    Output("pdf-viewer", "src"),
    Input("load-pdf", "n_clicks"),
    prevent_initial_call=True
)
def load_pdf(n_clicks):
    return "/assets/pdfjs/web/viewer.html?file=/assets/pdfjs/web/sample.pdf"

if __name__ == "__main__":
    app.run_server(debug=True)
