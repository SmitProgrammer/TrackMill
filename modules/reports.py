from datetime import datetime, timedelta
from PySide6.QtWidgets import QWidget

from ui_compiled.reports_ui import Ui_ReportsWidget
from database import cloud_first_db


class ReportsWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_ReportsWidget()
        self.ui.setupUi(self)

        self.setup_connections()
        self.setup_dates()

    def setup_connections(self):
        if hasattr(self.ui, 'btnGenerateReport'):
            self.ui.btnGenerateReport.clicked.connect(self.generate_report)
        if hasattr(self.ui, 'cmbTimePeriod'):
            self.ui.cmbTimePeriod.currentTextChanged.connect(self.on_time_period_changed)

    def setup_dates(self):
        """Setup default dates"""
        if hasattr(self.ui, 'dateFrom'):
            self.ui.dateFrom.setDate(datetime.now().date())
        if hasattr(self.ui, 'dateTo'):
            self.ui.dateTo.setDate(datetime.now().date())

    def on_time_period_changed(self, period):
        """Update date range based on selected period"""
        today = datetime.now().date()

        if period == "Today":
            start_date = today
            end_date = today
        elif period == "This Week":
            start_date = today - timedelta(days=today.weekday())
            end_date = today
        elif period == "This Month":
            start_date = today.replace(day=1)
            end_date = today
        elif period == "Last Month":
            last_month = today.replace(day=1) - timedelta(days=1)
            start_date = last_month.replace(day=1)
            end_date = last_month
        elif period == "This Year":
            start_date = today.replace(month=1, day=1)
            end_date = today
        else:  # Custom Range
            return

        if hasattr(self.ui, 'dateFrom'):
            self.ui.dateFrom.setDate(start_date)
        if hasattr(self.ui, 'dateTo'):
            self.ui.dateTo.setDate(end_date)

    def generate_report(self):
        """Generate report based on selected type and date range"""
        report_type = self.ui.cmbReportType.currentText()
        start_date = self.ui.dateFrom.date().toString("yyyy-MM-dd")
        end_date = self.ui.dateTo.date().toString("yyyy-MM-dd")

        report_content = ""

        if report_type == "Production Summary":
            report_content = self.generate_production_summary(start_date, end_date)
        elif report_type == "Inventory Status":
            report_content = self.generate_inventory_status()
        elif report_type == "Order Analysis":
            report_content = self.generate_order_analysis(start_date, end_date)
        elif report_type == "Machine Utilization":
            report_content = self.generate_machine_utilization(start_date, end_date)
        elif report_type == "Employee Productivity":
            report_content = self.generate_employee_productivity(start_date, end_date)
        elif report_type == "Material Consumption":
            report_content = self.generate_material_consumption(start_date, end_date)

        if hasattr(self.ui, 'txtReportPreview'):
            self.ui.txtReportPreview.setHtml(report_content)

    def generate_production_summary(self, start_date, end_date):
        """Generate production summary report"""
        # Firebase-only: get all jobs and filter in memory
        all_jobs = cloud_first_db.get_all_jobs()
        jobs = [j for j in all_jobs if start_date <= j.get('start_time', '')[:10] <= end_date]

        total_jobs = len(jobs)
        completed = len([j for j in jobs if j['status'] == 'Completed'])
        in_progress = len([j for j in jobs if j['status'] == 'In Progress'])
        pending = len([j for j in jobs if j['status'] == 'Pending'])

        html = f"""
        <h2>Production Summary Report</h2>
        <p><b>Period:</b> {start_date} to {end_date}</p>
        <hr>
        <h3>Overview</h3>
        <ul>
            <li><b>Total Jobs:</b> {total_jobs}</li>
            <li><b>Completed:</b> {completed}</li>
            <li><b>In Progress:</b> {in_progress}</li>
            <li><b>Pending:</b> {pending}</li>
        </ul>
        <hr>
        <h3>Job Details</h3>
        <table border="1" cellpadding="5" cellspacing="0" style="width:100%; border-collapse: collapse;">
            <tr style="background-color: #f0f0f0;">
                <th>Job ID</th>
                <th>Product</th>
                <th>Machine</th>
                <th>Operator</th>
                <th>Status</th>
            </tr>
        """

        for job in jobs:
            html += f"""
            <tr>
                <td>{job['id']}</td>
                <td>{job['product_name']}</td>
                <td>{job['machine_name']}</td>
                <td>{job['operator_name']}</td>
                <td>{job['status']}</td>
            </tr>
            """

        html += "</table>"
        return html

    def generate_inventory_report(self):
        """Generate inventory summary report"""
        materials = cloud_first_db.get_all_inventory()

        total_materials = len(materials)
        low_stock = len([m for m in materials if m['current_stock'] < m['min_stock']])
        total_value = sum([m['current_stock'] * m.get('unit_cost', 0) for m in materials])

        html = f"""
        <h2>Inventory Status Report</h2>
        <p><b>Generated:</b> {datetime.now().strftime('%Y-%m-%d %H:%M')}</p>
        <hr>
        <h3>Overview</h3>
        <ul>
            <li><b>Total Materials:</b> {total_materials}</li>
            <li><b>Low Stock Items:</b> {low_stock}</li>
            <li><b>Total Inventory Value:</b> ₹{total_value:,.2f}</li>
        </ul>
        <hr>
        <h3>Material Details</h3>
        <table border="1" cellpadding="5" cellspacing="0" style="width:100%; border-collapse: collapse;">
            <tr style="background-color: #f0f0f0;">
                <th>Material</th>
                <th>Current Stock</th>
                <th>Min Stock</th>
                <th>Unit</th>
                <th>Status</th>
            </tr>
        """

        for material in materials:
            status = "Low Stock" if material['current_stock'] < material['min_stock'] else "Available"
            status_color = "red" if status == "Low Stock" else "green"
            html += f"""
            <tr>
                <td>{material['material_name']}</td>
                <td>{material['current_stock']}</td>
                <td>{material['min_stock']}</td>
                <td>{material['unit']}</td>
                <td style="color: {status_color}; font-weight: bold;">{status}</td>
            </tr>
            """

        html += "</table>"
        return html

    def generate_order_analysis(self, start_date, end_date):
        """Generate order analysis report"""
        # Firebase-only: get all orders and filter in memory
        all_orders = cloud_first_db.get_all_orders()
        orders = [o for o in all_orders if start_date <= o.get('order_date', '')[:10] <= end_date]

        total_orders = len(orders)
        completed = len([o for o in orders if o['status'] == 'Completed'])
        in_progress = len([o for o in orders if o['status'] == 'In Progress'])
        pending = len([o for o in orders if o['status'] == 'Pending'])

        html = f"""
        <h2>Order Analysis Report</h2>
        <p><b>Period:</b> {start_date} to {end_date}</p>
        <hr>
        <h3>Overview</h3>
        <ul>
            <li><b>Total Orders:</b> {total_orders}</li>
            <li><b>Completed:</b> {completed}</li>
            <li><b>In Progress:</b> {in_progress}</li>
            <li><b>Pending:</b> {pending}</li>
        </ul>
        <hr>
        <h3>Order Details</h3>
        <table border="1" cellpadding="5" cellspacing="0" style="width:100%; border-collapse: collapse;">
            <tr style="background-color: #f0f0f0;">
                <th>Order ID</th>
                <th>Customer</th>
                <th>Product</th>
                <th>Quantity</th>
                <th>Status</th>
            </tr>
        """

        for order in orders:
            html += f"""
            <tr>
                <td>{order['id']}</td>
                <td>{order['customer_name']}</td>
                <td>{order['product_name']}</td>
                <td>{order['quantity']}</td>
                <td>{order['status']}</td>
            </tr>
            """

        html += "</table>"
        return html

    def generate_machine_utilization(self, start_date, end_date):
        """Generate machine utilization report"""
        machines = cloud_first_db.get_all_machines()

        html = f"""
        <h2>Machine Utilization Report</h2>
        <p><b>Period:</b> {start_date} to {end_date}</p>
        <hr>
        <h3>Machine Status</h3>
        <table border="1" cellpadding="5" cellspacing="0" style="width:100%; border-collapse: collapse;">
            <tr style="background-color: #f0f0f0;">
                <th>Machine</th>
                <th>Type</th>
                <th>Status</th>
                <th>Last Maintenance</th>
                <th>Next Maintenance</th>
            </tr>
        """

        for machine in machines:
            html += f"""
            <tr>
                <td>{machine['machine_name']}</td>
                <td>{machine['machine_type']}</td>
                <td>{machine['status']}</td>
                <td>{machine['last_maintenance']}</td>
                <td>{machine['next_maintenance']}</td>
            </tr>
            """

        html += "</table>"
        return html

    def generate_employee_productivity(self, start_date, end_date):
        """Generate employee productivity report"""
        all_employees = cloud_first_db.get_all_employees()
        employees = [e for e in all_employees if e.get('role') == 'Operator']

        html = f"""
        <h2>Employee Productivity Report</h2>
        <p><b>Period:</b> {start_date} to {end_date}</p>
        <hr>
        <h3>Employee Performance</h3>
        <table border="1" cellpadding="5" cellspacing="0" style="width:100%; border-collapse: collapse;">
            <tr style="background-color: #f0f0f0;">
                <th>Employee</th>
                <th>Role</th>
                <th>Jobs Completed</th>
                <th>Status</th>
            </tr>
        """

        for emp in employees:
            # Firebase-only: count jobs in memory
            all_jobs = cloud_first_db.get_all_jobs()
            count = len([j for j in all_jobs if j.get('operator_id') == emp['id'] and start_date <= j.get('start_time', '')[:10] <= end_date and j.get('status') == 'Completed'])

            html += f"""
            <tr>
                <td>{emp['name']}</td>
                <td>{emp['role']}</td>
                <td>{count}</td>
                <td>{emp['status']}</td>
            </tr>
            """

        html += "</table>"
        return html

    def generate_material_consumption(self, start_date, end_date):
        """Generate material consumption report"""
        materials = cloud_first_db.get_all_inventory()

        html = f"""
        <h2>Material Consumption Report</h2>
        <p><b>Period:</b> {start_date} to {end_date}</p>
        <hr>
        <h3>Material Usage</h3>
        <table border="1" cellpadding="5" cellspacing="0" style="width:100%; border-collapse: collapse;">
            <tr style="background-color: #f0f0f0;">
                <th>Material</th>
                <th>Current Stock</th>
                <th>Min Stock</th>
                <th>Unit</th>
                <th>Supplier</th>
            </tr>
        """

        for material in materials:
            html += f"""
            <tr>
                <td>{material['material_name']}</td>
                <td>{material['current_stock']}</td>
                <td>{material['min_stock']}</td>
                <td>{material['unit']}</td>
                <td>{material.get('supplier', 'N/A')}</td>
            </tr>
            """

        html += "</table>"
        return html


