from package import app
from flask import render_template, redirect, url_for, flash
#from package.models import Item, User
from package.forms import RequestForm, ShoppingListAddNewItem, UpdateAvailableWeight
from package import mysql
from flask_login import login_user, logout_user, login_required
from random import randint
from datetime import datetime, timedelta
from dateutil import parser

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')


@app.route("/request", methods=['GET','POST'])
def request_page():
    form = RequestForm()

    if form.validate_on_submit():
        #get max id
        query = 'SELECT MAX(Form_ID) FROM request_form LIMIT 1'
        cur = mysql.connection.cursor()
        cur.execute(query)
        id = int(cur.fetchall()[0][0]) + 1

        #request_to_submit = [form.student_id, form.student_name,form.phone_number,form.email_address,form.group_number,form.item_id,form.item_name,form.item_quantity,form.delivery_date,form.comments]
        query = 'INSERT INTO request_form VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        values = (id,form.student_id.data, form.student_name.data,form.phone_number.data,form.email_address.data,form.group_number.data,form.item_id.data,form.item_name.data,form.item_quantity.data,form.delivery_date.data, form.comments.data)        
        cur = mysql.connection.cursor()
        cur.execute(query, values)
        mysql.connection.commit()

        flash(f'Request form submiited succesfully Form ID {id}', category='success')
        #add request
        #add_request()




    return render_template('requestForm.html', form = form)

@app.route("/shoppinglist", methods=['GET','POST'])
def shopping_list():

    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM food_item''')

    # check if the item is low in stock

    result = [i for i in cur.fetchall() if i[-1] <= i[-2]]

    #adding items
    new_item = ShoppingListAddNewItem()
   
# adding data into food item
    query = 'SELECT MAX(Food_ID) FROM food_item LIMIT 1'
    cur = mysql.connection.cursor()
    cur.execute(query)

    if new_item.validate_on_submit():
        item_id = int(cur.fetchall()[0][0]) + 1
        name = new_item.item_name.data
        indv_weight = new_item.individual_weight.data
        category = new_item.category.data
        exp_date = new_item.expriry_date.data
        barcode = new_item.barcode.data
        container_id = new_item.container_id.data
        last_checkout_date = ""
        last_checkout_time = ""
        status = ""
        food_thresh = new_item.alert_at.data
        total = new_item.quantity.data

        query = "INSERT INTO food_item(Food_ID, food_name, Individual_Weight_Grams, Category, Expiry_Date, Barcode, Container_ID, Last_Checkout_Date, Last_Checkout_Time, Status, Food_Threshold, Total_Available) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (item_id, name, indv_weight, category, exp_date, barcode, container_id, last_checkout_date, last_checkout_time, status, food_thresh, total)
        cur.execute(query, values)
        mysql.connection.commit()

        query = "INSERT INTO container(Container_ID, Barcode, Container_Weight, Food_ID, expiration_date) VALUES (%s, %s, %s, %s, %s)"
        values = (container_id,barcode,total,item_id,exp_date)
        cur.execute(query, values)
        mysql.connection.commit()


        flash(f"Added item: {name}, Item ID: {item_id}", category="success")
        #Test_list = [[12, "Apples", 300,"12-Nov-2021", 2000], [42, "Cheese", 200,"15-Nov-2021", 3000]]

        

        return redirect(url_for('food_items'))

    #getting container info
    cur.execute('''SELECT * FROM container''')

    containers = cur.fetchall()

    # checking if expire date is close
    containers_to_expire = [i for i in containers if parser.parse(i[-1]) <= datetime.now() + timedelta(days=2)]
    

    #updating weight
    update_weight = UpdateAvailableWeight()

    
    if update_weight.validate_on_submit():

        print("aaaaaaaaaaaaaaaaaaaaaaaaa", update_weight.weight_to_add.data, update_weight.item_id.data)

        
        cur = mysql.connection.cursor()
        cur.execute(f"SELECT Total_Available FROM food_item WHERE Food_ID = {update_weight.item_id.data}")
        current_weight = cur.fetchone()[0]


        query = f'UPDATE food_item SET Total_Available = {update_weight.weight_to_add.data + current_weight} WHERE food_ID = {update_weight.item_id.data}'
        cur.execute(query)
        mysql.connection.commit()
        flash(f"{update_weight.weight_to_add.data} grams added to Item ID {update_weight.item_id.data}", category="info")
        return redirect(url_for('food_items'))
        

    return render_template("shoppingListPage.html", form = new_item , shop_list = result, containers_to_expire = containers_to_expire, update_weight=update_weight)

@app.route("/showrequests")
def show_requests():


    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM request_form''')

    result = cur.fetchall()
    return render_template('showRequests.html', request_forms= result)

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
    
    return render_template("containerPage.html", containers = result)
    #return str(result)

@app.route("/fooditems")
def food_items():

    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM food_item''')

    result = cur.fetchall()



    return render_template('foodItemPage.html', items = result)

