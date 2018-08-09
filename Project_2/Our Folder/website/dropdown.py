from flask import Flask, render_template, request

app = Flask(__name__)


app.debug = True


@app.route('/', methods=['GET'])
def dropdown():
    stocks = ['A', 'AAPL', 'AMD', 'ARQL', 'AU', 'BHP', 'BLIN', 'BOSC', 'BP', 'BTI']
    return render_template('test.html', stocks=stocks)

if __name__ == "__main__":
    app.run()
