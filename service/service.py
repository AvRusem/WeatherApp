from flask import Flask, render_template, request, redirect, url_for

from enum import Enum
from functions import GetRecommendation, Response

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        start_point = request.form['start_point']
        end_point = request.form['end_point']

        response = GetRecommendation(start_point, end_point)

        message = ''
        if response == Response.GOOD:
            message = 'Погода супер'
        elif response == Response.BAD:
            message = 'Ой-ой, погода плохая'
        elif response == Response.USER_ERROR:
            message = 'Ошибка: Перепроверьте написание названия городов'
        else:
            message = 'Ошибка: Не удалось получить информацию о погоде'
        message = request.args.get('message', message)

        return render_template('message.html', message=message)

    return render_template('main.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
