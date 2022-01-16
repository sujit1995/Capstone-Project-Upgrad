#from cgitb import text
from flask import Flask,render_template,request
import model 
app = Flask('__name__')

valid_userid = ['00sab00','1234','zippy','zburt5','joshua','dorothy w','rebecca','walker557','samantha','raeanne','kimmie','cassie','moore222']
@app.route('/')
def view():
    return render_template('index.html')

@app.route('/recommend',methods=['POST','GET'])
def recommend_top5():
    print(request.method)
    user_name = request.form['User Name']
    print('User name=',user_name)
    
    if  user_name in valid_userid and request.method == 'POST':
        
            top20_products = model.recommend_products(user_name)
            #print(top20_products)
            #print(top20_products.columns)
            get_top5 = model.top5_products(top20_products)
            #print(get_top5)
            #print(get_top5.to_html())
            return render_template('index.html',tables=[get_top5.to_html(classes='data',header=False,index=False)],text='Recommended products')
    elif not user_name in  valid_userid:
        return render_template('index.html',text='User not Found')
    else:
        return render_template('index.html')

    

if __name__ == '__main__':
    app.debug=False

    app.run()
