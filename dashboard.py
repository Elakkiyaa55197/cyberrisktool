from flask import Flask, render_template_string

app = Flask(__name__)

data = {
"Critical":1,
"High":2,
"Medium":1,
"Low":1
}

@app.route("/")
def dashboard():

    html = """
    <h1>Risk Dashboard</h1>

    <p>Critical: {{data['Critical']}}</p>
    <p>High: {{data['High']}}</p>
    <p>Medium: {{data['Medium']}}</p>
    <p>Low: {{data['Low']}}</p>

    <h2>Overall Risk Score : 8/10</h2>
    """

    return render_template_string(html,data=data)


app.run(debug=True)