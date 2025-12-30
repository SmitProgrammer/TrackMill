from datetime import datetime, timedelta
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QHeaderView
from PySide6.QtCore import Qt

from ui_compiled.reports_ui import Ui_ReportsWidget
from database import sqlite_db
from utils import show_error


class ReportsWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_ReportsWidget()
        self.ui.setupUi(self)

        self.setup_tables()
        self.setup_connections()
        self.load_reports()

    def setup_tables(self):
        self.ui.tableOrderReport.setColumnWidth(0, 100)
        self.ui.tableOrderReport.setColumnWidth(1, 150)
        self.ui.tableOrderReport.setColumnWidth(2, 150)
        self.ui.tableOrderReport.setColumnWidth(3, 80)
        self.ui.tableOrderReport.setColumnWidth(4, 100)

        header = self.ui.tableOrderReport.horizontalHeader()
        header.setSectionResizeMode(2, QHeaderView.Stretch)

        self.ui.tableInventoryReport.setColumnWidth(0, 150)
        self.ui.tableInventoryReport.setColumnWidth(1, 100)
        self.ui.tableInventoryReport.setColumnWidth(2, 80)
        self.ui.tableInventoryReport.setColumnWidth(3, 100)

        header2 = self.ui.tableInventoryReport.horizontalHeader()
        header2.setSectionResizeMode(0, QHeaderView.Stretch)

        self.ui.tableProductionReport.setColumnWidth(0, 100)
        self.ui.tableProductionReport.setColumnWidth(1, 150)
        self.ui.tableProductionReport.setColumnWidth(2, 120)
        self.ui.tableProductionReport.setColumnWidth(3, 120)
        self.ui.tableProductionReport.setColumnWidth(4, 100)

        header3 = self.ui.tableProductionReport.horizontalHeader()
        header3.setSectionResizeMode(1, QHeaderView.Stretch)

    def setup_connections(self):
        self.ui.btnGenerateOrders.clicked.connect(self.generate_order_report)
        self.ui.btnGenerateInventory.clicked.connect(self.generate_inventory_report)
        self.ui.btnGenerateProduction.clicked.connect(self.generate_production_report)

    def load_reports(self):
        self.generate_order_report()
        self.generate_inventory_report()
        self.generate_production_report()

    def generate_order_report(self):
        self.ui.tableOrderReport.setRowCount(0)

        start_date = self.ui.dateOrderStart.date().toString('yyyy-MM-dd')
        end_date = self.ui.dateOrderEnd.date().toString('yyyy-MM-dd')

        query = """
            SELECT id, customer_name, product_name, quantity, status 
            FROM orders 
            WHERE order_date BETWEEN ? AND ?
            ORDER BY order_date DESC
        """

        orders = sqlite_db.fetch_all(query, (start_date, end_date))

        total_orders = len(orders)
        pending_count = 0
        in_progress_count = 0
        completed_count = 0

        for order in orders:
            row = self.ui.tableOrderReport.rowCount()
            self.ui.tableOrderReport.insertRow(row)

            self.ui.tableOrderReport.setItem(row, 0, QTableWidgetItem(order['id']))
            self.ui.tableOrderReport.setItem(row, 1, QTableWidgetItem(order['customer_name'] or ''))
            self.ui.tableOrderReport.setItem(row, 2, QTableWidgetItem(order['product_name']))
            self.ui.tableOrderReport.setItem(row, 3, QTableWidgetItem(str(order['quantity'])))

            status_item = QTableWidgetItem(order['status'] or 'Pending')
            if order['status'] == 'Completed':
                status_item.setForeground(Qt.GlobalColor.darkGreen)
                completed_count += 1
            elif order['status'] == 'In Progress':
                status_item.setForeground(Qt.GlobalColor.blue)
                in_progress_count += 1
            elif order['status'] == 'Pending':
                status_item.setForeground(Qt.GlobalColor.darkYellow)
                pending_count += 1

            self.ui.tableOrderReport.setItem(row, 4, status_item)

        summary = f"Total: {total_orders} | Pending: {pending_count} | In Progress: {in_progress_count} | Completed: {completed_count}"
        self.ui.lblOrderSummary.setText(summary)

    def generate_inventory_report(self):
        self.ui.tableInventoryReport.setRowCount(0)

        query = """
            SELECT material_name, current_stock, unit, status 
            FROM inventory 
            ORDER BY current_stock ASC
        """

        materials = sqlite_db.fetch_all(query)

        low_stock_count = 0
        out_of_stock_count = 0

        for material in materials:
            row = self.ui.tableInventoryReport.rowCount()
            self.ui.tableInventoryReport.insertRow(row)

            self.ui.tableInventoryReport.setItem(row, 0, QTableWidgetItem(material['material_name']))

            stock_item = QTableWidgetItem(f"{material['current_stock']:.2f}")
            if material['current_stock'] <= 0:
                stock_item.setForeground(Qt.GlobalColor.red)
                out_of_stock_count += 1
            elif material['status'] == 'Low Stock':
                stock_item.setForeground(Qt.GlobalColor.darkYellow)
                low_stock_count += 1

            self.ui.tableInventoryReport.setItem(row, 1, stock_item)
            self.ui.tableInventoryReport.setItem(row, 2, QTableWidgetItem(material['unit'] or ''))

            status_item = QTableWidgetItem(material['status'] or 'Available')
            if material['status'] == 'Available':
                status_item.setForeground(Qt.GlobalColor.darkGreen)
            elif material['status'] == 'Low Stock':
                status_item.setForeground(Qt.GlobalColor.darkYellow)
            elif material['status'] == 'Out of Stock':
                status_item.setForeground(Qt.GlobalColor.red)

            self.ui.tableInventoryReport.setItem(row, 3, status_item)

        summary = f"Total Items: {len(materials)} | Low Stock: {low_stock_count} | Out of Stock: {out_of_stock_count}"
        self.ui.lblInventorySummary.setText(summary)

    def generate_production_report(self):
        self.ui.tableProductionReport.setRowCount(0)

        start_date = self.ui.dateProductionStart.date().toString('yyyy-MM-dd')
        end_date = self.ui.dateProductionEnd.date().toString('yyyy-MM-dd')

        query = """
            SELECT id, product_name, machine_name, operator_name, status 
            FROM jobs 
            WHERE start_time BETWEEN ? AND ?
            ORDER BY start_time DESC
        """

        jobs = sqlite_db.fetch_all(query, (start_date, end_date))

        total_jobs = len(jobs)
        pending_count = 0
        in_progress_count = 0
        completed_count = 0

        for job in jobs:
            row = self.ui.tableProductionReport.rowCount()
            self.ui.tableProductionReport.insertRow(row)

            self.ui.tableProductionReport.setItem(row, 0, QTableWidgetItem(job['id']))
            self.ui.tableProductionReport.setItem(row, 1, QTableWidgetItem(job['product_name']))
            self.ui.tableProductionReport.setItem(row, 2, QTableWidgetItem(job['machine_name'] or ''))
            self.ui.tableProductionReport.setItem(row, 3, QTableWidgetItem(job['operator_name'] or ''))

            status_item = QTableWidgetItem(job['status'] or 'Pending')
            if job['status'] == 'Completed':
                status_item.setForeground(Qt.GlobalColor.darkGreen)
                completed_count += 1
            elif job['status'] == 'In Progress':
                status_item.setForeground(Qt.GlobalColor.blue)
                in_progress_count += 1
            elif job['status'] == 'Pending':
                status_item.setForeground(Qt.GlobalColor.darkYellow)
                pending_count += 1

            self.ui.tableProductionReport.setItem(row, 4, status_item)

        summary = f"Total Jobs: {total_jobs} | Pending: {pending_count} | In Progress: {in_progress_count} | Completed: {completed_count}"
        self.ui.lblProductionSummary.setText(summary)

