"""
Script to populate Firebase database with dummy data for testing
"""

from datetime import datetime, timedelta
import random
from database import cloud_first_db

print("=" * 60)
print("  POPULATING FIREBASE WITH DUMMY DATA")
print("=" * 60)

# Sample data
customer_names = [
    "Tata Motors", "Mahindra & Mahindra", "Bajaj Auto",
    "Hero MotoCorp", "TVS Motors", "Ashok Leyland",
    "Maruti Suzuki", "Hyundai Motors", "Royal Enfield", "Eicher Motors"
]

customer_contacts = [
    "+91-9876543210", "+91-9876543211", "+91-9876543212",
    "+91-9876543213", "+91-9876543214", "+91-9876543215",
    "+91-9876543216", "+91-9876543217", "+91-9876543218", "+91-9876543219"
]

product_names = [
    "Engine Block", "Gear Box Housing", "Brake Disc", "Cylinder Head",
    "Connecting Rod", "Crankshaft", "Camshaft", "Piston Housing",
    "Valve Cover", "Oil Pan", "Transmission Case", "Differential Housing"
]

material_types = ["Aluminum", "Steel", "Cast Iron", "Brass", "Stainless Steel"]

machine_names = [
    "CNC Lathe Machine 1", "CNC Milling Machine 1", "CNC Drilling Machine 1",
    "CNC Grinding Machine 1", "CNC Boring Machine 1"
]

operator_names = [
    "Rajesh Kumar", "Amit Sharma", "Suresh Patel", "Vikram Singh",
    "Ramesh Verma", "Anil Gupta", "Sanjay Yadav", "Manoj Tiwari"
]

# Add Customers
print("\nAdding customers...")
customer_ids = []
for i, name in enumerate(customer_names):
    customer_id = f"CUST{datetime.now().strftime('%Y%m%d')}{i:03d}"
    customer_ids.append(customer_id)

    data = {
        'name': name,
        'contact': customer_contacts[i],
        'email': f"{name.lower().replace(' ', '').replace('&', '')}@example.com",
        'company': name,
        'address': f"{random.randint(1, 999)}, Industrial Area, {random.choice(['Mumbai', 'Delhi', 'Pune', 'Bangalore', 'Chennai'])}",
    }

    if cloud_first_db.create_customer(customer_id, data):
        print(f"  ✓ Added customer: {name}")
    else:
        print(f"  ✗ Failed to add customer: {name}")

# Add Inventory/Materials
print("\nAdding inventory items...")
material_ids = []
for i in range(15):
    material_id = f"MAT{datetime.now().strftime('%Y%m%d')}{i:03d}"
    material_ids.append(material_id)

    current_stock = random.uniform(100, 1000)
    min_stock = random.uniform(50, 200)

    data = {
        'material_name': f"{random.choice(material_types)} Sheet/Bar {i+1}",
        'material_type': random.choice(material_types),
        'current_stock': round(current_stock, 2),
        'unit': random.choice(['kg', 'meters', 'pieces']),
        'min_stock': round(min_stock, 2),
        'supplier': f"Supplier {random.choice(['A', 'B', 'C', 'D', 'E'])} Ltd.",
        'status': 'Low Stock' if current_stock < min_stock * 1.5 else 'Available',
    }

    if cloud_first_db.create_material(material_id, data):
        print(f"  ✓ Added material: {data['material_name']}")
    else:
        print(f"  ✗ Failed to add material: {data['material_name']}")

# Add Machines
print("\nAdding machines...")
machine_ids = []
for i, name in enumerate(machine_names):
    machine_id = f"MCH{datetime.now().strftime('%Y%m%d')}{i:03d}"
    machine_ids.append(machine_id)

    last_maintenance = (datetime.now() - timedelta(days=random.randint(30, 90))).strftime('%Y-%m-%d')
    next_maintenance = (datetime.now() + timedelta(days=random.randint(30, 60))).strftime('%Y-%m-%d')

    data = {
        'machine_name': name,
        'machine_type': name.split()[1],
        'model': f"Model-{random.randint(1000, 9999)}",
        'status': random.choice(['Available', 'Available', 'Available', 'In Use', 'Maintenance']),
        'last_maintenance': last_maintenance,
        'next_maintenance': next_maintenance,
        'specifications': f"Max Speed: {random.randint(3000, 8000)} RPM, Power: {random.randint(5, 20)} HP",
    }

    if cloud_first_db.create_machine(machine_id, data):
        print(f"  ✓ Added machine: {name}")
    else:
        print(f"  ✗ Failed to add machine: {name}")

# Add Employees (Operators)
print("\nAdding employees...")
employee_ids = []
for i, name in enumerate(operator_names):
    employee_id = f"EMP{datetime.now().strftime('%Y%m%d')}{i:03d}"
    employee_ids.append(employee_id)

    data = {
        'name': name,
        'role': 'Operator',
        'contact': f"+91-98765432{20+i}",
        'email': f"{name.lower().replace(' ', '.')}@cnc.com",
        'address': f"{random.randint(1, 99)}, Worker Colony, Industrial Area",
        'has_login': 0,
        'firebase_uid': '',
        'status': random.choice(['Active', 'Active', 'Active', 'Blocked']),
    }

    if cloud_first_db.create_employee(employee_id, data):
        print(f"  ✓ Added employee: {name}")
    else:
        print(f"  ✗ Failed to add employee: {name}")

# Add Orders
print("\nAdding orders...")
order_ids = []
for i in range(20):
    order_id = f"ORD{datetime.now().strftime('%Y%m%d')}{i:03d}"
    order_ids.append(order_id)

    customer_id = random.choice(customer_ids)
    customers = cloud_first_db.get_all_customers()
    customer = next((c for c in customers if c['id'] == customer_id), None)

    if not customer:
        continue

    order_date = (datetime.now() - timedelta(days=random.randint(0, 60))).strftime('%Y-%m-%d')
    delivery_date = (datetime.now() + timedelta(days=random.randint(10, 90))).strftime('%Y-%m-%d')

    data = {
        'customer_id': customer_id,
        'customer_name': customer.get('name'),
        'product_name': random.choice(product_names),
        'quantity': random.randint(10, 500),
        'specifications': f"Material: {random.choice(material_types)}, Tolerance: ±0.01mm, Surface Finish: Ra 3.2",
        'order_date': order_date,
        'delivery_date': delivery_date,
        'priority': random.choice(['Low', 'Medium', 'High', 'Urgent']),
        'status': random.choice(['Pending', 'In Progress', 'Completed', 'Completed']),
    }

    if cloud_first_db.create_order(order_id, data):
        print(f"  ✓ Added order: {order_id} - {data['product_name']}")
    else:
        print(f"  ✗ Failed to add order: {order_id}")

# Add Job Cards
print("\nAdding job cards...")
for i in range(15):
    job_id = f"JOB{datetime.now().strftime('%Y%m%d')}{i:03d}"

    if not order_ids:
        continue

    order_id = random.choice(order_ids)
    orders = cloud_first_db.get_all_orders()
    order = next((o for o in orders if o['id'] == order_id), None)

    if not order:
        continue

    machine_id = random.choice(machine_ids)
    machines = cloud_first_db.get_all_machines()
    machine = next((m for m in machines if m['id'] == machine_id), None)

    if not machine:
        continue

    operator_id = random.choice(employee_ids)
    employees = cloud_first_db.get_all_employees()
    operator = next((e for e in employees if e['id'] == operator_id), None)

    if not operator:
        continue

    start_time = (datetime.now() - timedelta(days=random.randint(0, 30), hours=random.randint(0, 8))).strftime('%Y-%m-%d %H:%M:%S')
    end_time = (datetime.now() - timedelta(days=random.randint(0, 25), hours=random.randint(0, 8))).strftime('%Y-%m-%d %H:%M:%S')

    data = {
        'order_id': order_id,
        'product_name': order.get('product_name'),
        'machine_id': machine_id,
        'machine_name': machine.get('machine_name'),
        'operator_id': operator_id,
        'operator_name': operator.get('name'),
        'start_time': start_time,
        'end_time': end_time,
        'status': random.choice(['Pending', 'In Progress', 'Completed', 'Completed']),
        'material_used': f"{random.choice(material_types)} - {random.uniform(10, 50):.2f} kg",
    }

    if cloud_first_db.create_job(job_id, data):
        print(f"  ✓ Added job card: {job_id}")
    else:
        print(f"  ✗ Failed to add job card: {job_id}")

print("\n" + "=" * 60)
print("  DUMMY DATA POPULATION COMPLETED!")
print("=" * 60)
print(f"\nSummary:")
print(f"  Customers: {len(customer_ids)}")
print(f"  Materials: {len(material_ids)}")
print(f"  Machines: {len(machine_ids)}")
print(f"  Employees: {len(employee_ids)}")
print(f"  Orders: {len(order_ids)}")
print(f"  Job Cards: 15")
print("\nAll data has been uploaded to Firebase!")
print("You can now login and see the data in the application!")


