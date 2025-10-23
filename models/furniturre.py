from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Furniture(db.Model):
    __tablename__ = 'furniture_inventory'

    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.String(20), unique=True, nullable=False)
    item_name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    material = db.Column(db.String(50))
    manufacturer = db.Column(db.String(100))
    unit_price = db.Column(db.Float, nullable=False)
    quantity_in_stock = db.Column(db.Integer, nullable=False)
    reorder_level = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(50))
    date_added = db.Column(db.DateTime, server_default=db.func.now())
    last_updated = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f"<Furniture {self.item_name}>"
