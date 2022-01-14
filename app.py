#from itertools import Predicate
from flask import Flask,render_template,request
import model 
app = Flask('__name__')

valid_userid = ['00sab00','1234','zippy','zburt5']
@app.route('/')
def view():
    return render_template('index.html')

@app.route('/recommend/',methods=['POST'])
def recommend_top5():
    user_name = request.form['User Name']
    if  user_name in valid_userid:
            top20_products = model.recommend_products(user_name)
            get_top5 = model.top5_products(top20_products)
            return render_template('index.html',tables=get_top5)
    else:
        return render_template('index.html')

    

if __name__ == '__main__':
    app.run(debug=True)
