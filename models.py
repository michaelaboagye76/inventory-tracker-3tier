from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Appliance(db.Model):
    __tablename__ = 'appliances'
    
    Appliance_ID = db.Column(db.Integer, primary_key=True)
    Appliance_Name = db.Column(db.String(100), nullable=False)
    Category = db.Column(db.String(50), nullable=False)
    Brand = db.Column(db.String(50), nullable=False)
    Model_Number = db.Column(db.String(50), nullable=False)
    Unit_Price = db.Column(db.Float, nullable=False)
    Quantity_In_Stock = db.Column(db.Integer, nullable=False)
    Reorder_Level = db.Column(db.Integer, nullable=False)
    Warranty_Period = db.Column(db.String(30))
    Location = db.Column(db.String(50))
    
    def __repr__(self):
        return f"<Appliance {self.Appliance_Name}>"
