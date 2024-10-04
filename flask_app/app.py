from flask import Flask, render_template, jsonify, request, redirect, url_for

from classes import Converter, WashingMachineThread, washing_state

app = Flask(__name__, template_folder='D:\python_work\\x-python\\flask_app\\templates')


@app.route('/', methods=['GET', "POST"])
def index():
    return render_template('index.html')


@app.route('/washing', methods=["GET", "POST"])
def washing():
    if request.method == 'POST':
        if washing_state['state'] == "waiting":
            form = request.form
            thread = WashingMachineThread()

            washing_time = int(form.get('washing_time'))
            rinsing_time = int(form.get('rinsing_time'))
            spinning_time = int(form.get('spinning_time'))

            thread.washing_cycle(washing_time=washing_time, rinsing_time=rinsing_time, spinning_time=spinning_time)

            thread.start()

        return redirect(url_for('index'))

    return jsonify(washing_state)


@app.route('/converter', methods=["GET", "POST"])
def converter():
    if request.method == 'POST':
        converter = Converter()
        form = request.form
        coef = float(form.get('coef'))
        value = float(form.get('value'))

        result = converter.convert(value, coef)

        return render_template('converter.html', result=result)

    return render_template('converter.html')


if __name__ == '__main__':
    app.run(debug=True)
