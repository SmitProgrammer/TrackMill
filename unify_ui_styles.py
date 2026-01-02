"""
Script to unify styling across all UI files based on customers.ui
"""

import re
import os

# Define the base styling template from customers.ui
BASE_STYLE_TEMPLATE = """QWidget#{widget_name} {{
    background-color: #f5f5f5;
}}

QLabel {{
    color: #333;
}}

QTableWidget {{
    color: #333;
}}

{button_styles}

{input_styles}

{combo_styles}

{table_styles}

{groupbox_styles}"""

# Button configurations for each module
BUTTON_CONFIGS = {
    'employees': [
        ('btnAddEmployee', '#4CAF50', '#45a049'),
        ('btnEditEmployee', '#2196F3', '#0b7dda'),
        ('btnDeleteEmployee', '#f44336', '#da190b'),
        ('btnBlockUnblock', '#FF9800', '#e68900'),
        ('btnCreateAccount', '#9C27B0', '#8E24AA'),
        ('btnRefresh', '#607D8B', '#546E7A'),
    ],
    'inventory': [
        ('btnAddMaterial', '#4CAF50', '#45a049'),
        ('btnAddStock', '#2196F3', '#0b7dda'),
        ('btnIssueStock', '#FF9800', '#e68900'),
        ('btnEditMaterial', '#9C27B0', '#8E24AA'),
        ('btnDeleteMaterial', '#f44336', '#da190b'),
        ('btnRefresh', '#607D8B', '#546E7A'),
    ],
    'orders': [
        ('btnAddOrder', '#4CAF50', '#45a049'),
        ('btnEditOrder', '#2196F3', '#0b7dda'),
        ('btnDeleteOrder', '#f44336', '#da190b'),
        ('btnRefresh', '#FF9800', '#e68900'),
    ],
    'machines': [
        ('btnAddMachine', '#4CAF50', '#45a049'),
        ('btnEditMachine', '#2196F3', '#0b7dda'),
        ('btnDeleteMachine', '#f44336', '#da190b'),
        ('btnMaintenance', '#FF9800', '#e68900'),
        ('btnRefresh', '#607D8B', '#546E7A'),
    ],
    'production': [
        ('btnNewJob', '#4CAF50', '#45a049'),
        ('btnEditJob', '#2196F3', '#0b7dda'),
        ('btnDeleteJob', '#f44336', '#da190b'),
        ('btnRefresh', '#FF9800', '#e68900'),
    ],
    'reports': [
        ('btnGenerateReport', '#2196F3', '#0b7dda'),
    ],
    'settings': [
        ('btnSaveSettings', '#4CAF50', '#45a049'),
        ('btnChangePassword', '#2196F3', '#0b7dda'),
    ],
}

def generate_button_styles(buttons):
    """Generate button style CSS for given buttons"""
    # First, the combined selector
    button_names = ', '.join([f'QPushButton#{btn[0]}' for btn in buttons])
    style = f"""{button_names} {{
    padding: 10px 20px;
    border-radius: 5px;
    font-size: 13px;
    font-weight: bold;
}}

"""

    # Then individual button styles
    for btn_name, color, hover_color in buttons:
        style += f"""QPushButton#{btn_name} {{
    background-color: {color};
    color: white;
    border: none;
}}

QPushButton#{btn_name}:hover {{
    background-color: {hover_color};
}}

"""

    return style.rstrip()

def has_combo_box(module_name):
    """Check if module has combo box filter"""
    return module_name in ['employees', 'orders', 'machines', 'production', 'reports']

def has_table(module_name):
    """Check if module has table widget"""
    return module_name in ['employees', 'inventory', 'orders', 'machines', 'production', 'customers']

def has_search(module_name):
    """Check if module has search input"""
    return module_name in ['employees', 'inventory', 'orders', 'machines', 'production', 'customers']

def is_settings(module_name):
    """Check if this is settings module"""
    return module_name == 'settings'

def generate_input_styles(module_name):
    """Generate input field styles"""
    if is_settings(module_name):
        return """QLineEdit {{
    padding: 10px;
    border: 2px solid #ddd;
    border-radius: 5px;
    font-size: 13px;
    background-color: white;
    color: #333;
}}

QLineEdit:focus {{
    border: 2px solid #2196F3;
}}"""
    elif has_search(module_name):
        return """QLineEdit#txtSearch {{
    padding: 10px;
    border: 2px solid #ddd;
    border-radius: 5px;
    font-size: 13px;
    background-color: white;
    color: #333;
}}

QLineEdit#txtSearch:focus {{
    border: 2px solid #2196F3;
}}"""
    elif module_name == 'reports':
        return """QTextEdit#txtReportPreview {{
    border: 1px solid #ddd;
    border-radius: 5px;
    background-color: #fafafa;
    color: #333;
}}"""
    return ''

def generate_combo_styles():
    """Generate combo box styles"""
    return """QComboBox#cmbFilterStatus, QComboBox#cmbReportType, QComboBox#cmbTimePeriod {{
    padding: 10px;
    border: 2px solid #ddd;
    border-radius: 5px;
    font-size: 13px;
    background-color: white;
    color: #333;
}}

QComboBox#cmbFilterStatus:focus, QComboBox#cmbReportType:focus, QComboBox#cmbTimePeriod:focus {{
    border: 2px solid #2196F3;
}}"""

def generate_table_styles(module_name):
    """Generate table widget styles"""
    if has_table(module_name):
        return """QTableWidget {{
    background-color: white;
    border: 1px solid #ddd;
    border-radius: 5px;
    gridline-color: #e0e0e0;
}}

QTableWidget::item {{
    padding: 5px;
}}

QTableWidget::item:selected {{
    background-color: #e3f2fd;
    color: #000;
}}

QHeaderView::section {{
    background-color: #f5f5f5;
    padding: 10px;
    border: none;
    border-bottom: 2px solid #2196F3;
    font-weight: bold;
    color: #333;
}}"""
    return ''

def generate_groupbox_styles(module_name):
    """Generate groupbox styles for settings"""
    if is_settings(module_name):
        return """QGroupBox {{
    background-color: white;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    margin-top: 15px;
    padding-top: 15px;
    font-size: 14px;
    font-weight: bold;
}}

QGroupBox::title {{
    subcontrol-origin: margin;
    subcontrol-position: top left;
    padding: 5px 10px;
    color: #2196F3;
}}"""
    elif module_name == 'reports':
        return """QWidget#reportCard {{
    background-color: white;
    border-radius: 10px;
    border: 1px solid #e0e0e0;
}}

QLabel#lblReportTitle {{
    font-size: 16px;
    font-weight: bold;
    color: #333;
}}"""
    return ''

def update_ui_file(file_path, widget_name, button_config):
    """Update a UI file with unified styling"""
    print(f"\nProcessing {os.path.basename(file_path)}...")

    module_name = widget_name.replace('Widget', '').lower()

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Generate styles
        button_styles = generate_button_styles(button_config)
        input_styles = generate_input_styles(module_name)
        combo_styles = generate_combo_styles() if has_combo_box(module_name) else ''
        table_styles = generate_table_styles(module_name)
        groupbox_styles = generate_groupbox_styles(module_name)

        # Create the full stylesheet
        stylesheet = BASE_STYLE_TEMPLATE.format(
            widget_name=widget_name,
            button_styles=button_styles,
            input_styles=input_styles,
            combo_styles=combo_styles,
            table_styles=table_styles,
            groupbox_styles=groupbox_styles
        )

        # Find and replace the stylesheet section
        pattern = r'<property name="styleSheet">\s*<string notr="true">.*?</string>\s*</property>'
        replacement = f'<property name="styleSheet">\n   <string notr="true">{stylesheet}</string>\n  </property>'

        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✓ Updated {os.path.basename(file_path)}")
        else:
            print(f"✗ No changes made to {os.path.basename(file_path)}")

    except Exception as e:
        print(f"✗ Error processing {os.path.basename(file_path)}: {e}")

# Process each file
ui_dir = "ui"

print("=" * 70)
print("  Unifying UI Styles Based on customers.ui")
print("=" * 70)

for module_name, buttons in BUTTON_CONFIGS.items():
    widget_name = f"{module_name.capitalize()}Widget"
    file_path = os.path.join(ui_dir, f"{module_name}.ui")

    if os.path.exists(file_path):
        update_ui_file(file_path, widget_name, buttons)
    else:
        print(f"✗ File not found: {file_path}")

print("\n" + "=" * 70)
print("  Style unification complete!")
print("=" * 70)
print("\nNext step: Run compile_ui.bat to compile the updated UI files")

