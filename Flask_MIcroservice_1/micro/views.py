from flask import Blueprint, render_template, request

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        amount = int(request.form.get('amount'))
        if amount > 99999999999999 or amount <= 0:
            return render_template('home.html')
        else:
            denominations = [500, 200, 100, 50, 20, 10, 5, 2, 1]
            change = {}
            for denomination in denominations:
                if amount >= denomination:
                    count = amount // denomination
                    amount = amount % denomination
                    change[denomination] = count
            return render_template('change.html', notes=change)


    return render_template('home.html')