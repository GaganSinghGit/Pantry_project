from package import app
from flask import render_template, redirect, url_for, flash
#from package.models import Item, User
from package.forms import RequestForm, ShoppingListAddNewItem
from package import mysql
from flask_login import login_user, logout_user, login_required
from random import randint


@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')


@app.route("/request", methods=['GET','POST'])
def request_page():
    form = RequestForm()

    if form.validate_on_submit():

        id = randint(0, 100)
        request_to_submit = [form.student_id, form.student_name,form.phone_number,form.email_address,form.group_number,form.item_id,form.item_name,form.item_quantity,form.delivery_date,form.comments]
        query = 'INSERT INTO request_form VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        values = (id,form.student_id.data, form.student_name.data,form.phone_number.data,form.email_address.data,form.group_number.data,form.item_id.data,form.item_name.data,form.item_quantity.data,form.delivery_date.data, form.comments.data)        
        cur = mysql.connection.cursor()
        cur.execute(query, values)
        mysql.connection.commit()
        #add request
        #add_request()

    return render_template('requestForm.html', form = form)

@app.route("/shoppinglist", methods=['GET','POST'])
def shopping_list():



    #adding items
    new_item = ShoppingListAddNewItem()


    Test_list = [[12, "Apples", 300,"12-Nov-2021", 2000], [42, "Cheese", 200,"15-Nov-2021", 3000]]
    return render_template("shoppingListPage.html", form = new_item , shop_list = Test_list)

@app.route("/showrequests")
def show_requests():
    request_forms = [["453","123213","abc@deakin.edu.au","Apple",200],["454","125513","ksksk@deakin.edu.au","Apple",300]]
    return render_template('showRequests.html', request_forms= request_forms)

@app.route("/test")
def test():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM test_gagan''')

    result = cur.fetchall()

    return str(result)

@app.route("/containers")
def containers():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM container''')

    result = cur.fetchall()
    print(result)
    return render_template("containerPage.html", containers = result)
    #return str(result)

@app.route("/fooditems")
def food_items():

    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM food_item''')

    result = cur.fetchall()
    

    return render_template('foodItemPage.html', items = result)