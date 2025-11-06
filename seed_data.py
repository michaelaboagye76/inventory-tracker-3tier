from app import db, Inventory, app  # Assuming your model class is Inventory

with app.app_context():
    db.drop_all()
    db.create_all()

    sample_data = [
        Inventory(Appliance_Name="Samsung 55\" Smart TV", Category="Television", Brand="Samsung", Model_Number="UA55TU8000",
                  Unit_Price=899.99, Quantity_In_Stock=15, Reorder_Level=5, Warranty_Period="24 months", Location="Aisle 1 - TV"),
        Inventory(Appliance_Name="LG 43\" LED TV", Category="Television", Brand="LG", Model_Number="43LM6300PLA",
                  Unit_Price=649.00, Quantity_In_Stock=10, Reorder_Level=3, Warranty_Period="18 months", Location="Aisle 1 - TV"),
        Inventory(Appliance_Name="Hisense 32\" HD TV", Category="Television", Brand="Hisense", Model_Number="32A4BG",
                  Unit_Price=329.50, Quantity_In_Stock=20, Reorder_Level=5, Warranty_Period="12 months", Location="Aisle 2 - TV"),
        Inventory(Appliance_Name="Samsung Refrigerator", Category="Refrigerator", Brand="Samsung", Model_Number="RT28T3922S8",
                  Unit_Price=999.00, Quantity_In_Stock=8, Reorder_Level=2, Warranty_Period="24 months", Location="Aisle 3 - Fridge"),
        Inventory(Appliance_Name="LG Smart Fridge", Category="Refrigerator", Brand="LG", Model_Number="GL-T292RPZN",
                  Unit_Price=1199.99, Quantity_In_Stock=6, Reorder_Level=2, Warranty_Period="24 months", Location="Aisle 3 - Fridge"),
        Inventory(Appliance_Name="Whirlpool Washer", Category="Washing Machine", Brand="Whirlpool", Model_Number="WH-XL900",
                  Unit_Price=749.99, Quantity_In_Stock=9, Reorder_Level=3, Warranty_Period="18 months", Location="Aisle 4 - Washer"),
        Inventory(Appliance_Name="Bosch Front Loader", Category="Washing Machine", Brand="Bosch", Model_Number="WAK24268IN",
                  Unit_Price=899.00, Quantity_In_Stock=7, Reorder_Level=3, Warranty_Period="24 months", Location="Aisle 4 - Washer"),
        Inventory(Appliance_Name="Panasonic Split AC 1.5HP", Category="Air Conditioner", Brand="Panasonic", Model_Number="CS/CU-YS12WKY",
                  Unit_Price=699.99, Quantity_In_Stock=12, Reorder_Level=4, Warranty_Period="18 months", Location="Aisle 5 - AC"),
        Inventory(Appliance_Name="Daikin Window AC 1HP", Category="Air Conditioner", Brand="Daikin", Model_Number="FTKP35QV16",
                  Unit_Price=549.99, Quantity_In_Stock=10, Reorder_Level=3, Warranty_Period="12 months", Location="Aisle 5 - AC"),
        Inventory(Appliance_Name="Philips Blender", Category="Kitchen Appliance", Brand="Philips", Model_Number="HR2222/20",
                  Unit_Price=99.99, Quantity_In_Stock=25, Reorder_Level=10, Warranty_Period="12 months", Location="Aisle 6 - Small"),
        Inventory(Appliance_Name="Panasonic Microwave Oven", Category="Kitchen Appliance", Brand="Panasonic", Model_Number="NN-ST266BFDG",
                  Unit_Price=149.99, Quantity_In_Stock=15, Reorder_Level=5, Warranty_Period="12 months", Location="Aisle 6 - Small"),
        Inventory(Appliance_Name="Russell Hobbs Toaster", Category="Kitchen Appliance", Brand="Russell Hobbs", Model_Number="RH-5600",
                  Unit_Price=49.99, Quantity_In_Stock=30, Reorder_Level=10, Warranty_Period="6 months", Location="Aisle 6 - Small"),
    ]

    db.session.add_all(sample_data)
    db.session.commit()

    print("Sample appliance data added successfully!")
