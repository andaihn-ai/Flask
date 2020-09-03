from flask import Flask, render_template, url_for

app = Flask('__name__')

@app.route('/fine_weight/<tall>')
def weightCompute(tall):
    result = int(tall) - 110
    return render_template('result.html', fineWeight=result, tall=tall)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='80', debug=True)