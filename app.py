from flask import Flask, render_template, request, redirect, url_for
from models.furniture import db, Furniture
import os

app = Flask(__name__)

# --- Database Configuration (RDS or local MySQL) ---
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL',  # format: mysql+pymysql://user:password@host:port/dbname
    'sqlite:///furniture.db'  # fallback for local testing
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

# --- Routes ---
@app.route('/')
def index():
    items = Furniture.query.all()
    return render_template('index.html', inventory=items)


@app.route('/add', methods=['POST'])
def add_item():
    item = Furniture(
        item_id=request.form['Item_ID'],
        item_name=request.form['Item_Name'],
        category=request.form['Category'],
        material=request.form['Material'],
        manufacturer=request.form['Manufacturer'],
        unit_price=float(request.form['Unit_Price']),
        quantity_in_stock=int(request.form['Quantity_In_Stock']),
        reorder_level=int(request.form['Reorder_Level']),
        location=request.form['Location']
    )
    db.session.add(item)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/summary')
def summary():
    items = Furniture.query.all()
    total_items = sum(i.quantity_in_stock for i in items)
    total_categories = len(set(i.category for i in items))
    below_reorder = sum(1 for i in items if i.quantity_in_stock <= i.reorder_level)
    total_value = sum(i.unit_price * i.quantity_in_stock for i in items)
    return render_template(
        'summary.html',
        total_items=total_items,
        total_categories=total_categories,
        below_reorder=below_reorder,
        total_value=total_value
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
