from flask import Flask, render_template, request, redirect, url_for
from models import db, Appliance
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///appliances.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def index():
    appliances = Appliance.query.all()
    return render_template('index.html', appliances=appliances)

@app.route('/add', methods=['POST'])
def add_appliance():
    new_item = Appliance(
        Appliance_Name=request.form['Appliance_Name'],
        Category=request.form['Category'],
        Brand=request.form['Brand'],
        Model_Number=request.form['Model_Number'],
        Unit_Price=request.form['Unit_Price'],
        Quantity_In_Stock=request.form['Quantity_In_Stock'],
        Reorder_Level=request.form['Reorder_Level'],
        Warranty_Period=request.form['Warranty_Period'],
        Location=request.form['Location']
    )
    db.session.add(new_item)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/summary')
def summary():
    total_items = db.session.query(db.func.count(Appliance.Appliance_ID)).scalar()
    total_value = db.session.query(db.func.sum(Appliance.Unit_Price * Appliance.Quantity_In_Stock)).scalar()
    low_stock = db.session.query(db.func.count(Appliance.Appliance_ID)).filter(Appliance.Quantity_In_Stock <= Appliance.Reorder_Level).scalar()
    return render_template('summary.html', total_items=total_items, total_value=total_value, low_stock=low_stock)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
