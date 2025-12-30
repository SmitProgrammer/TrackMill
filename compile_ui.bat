@echo off
echo ========================================
echo   CNC ERP - UI Files Compilation
echo ========================================
echo.

cd /d "D:\Study\B Tech\Sem 8\Major Project"
echo Activating virtual environment...
call .venv\Scripts\activate

echo.
echo Compiling UI files to Python...
echo.

pyside6-uic ui\login.ui -o ui_compiled\login_ui.py
echo [1/11] login.ui compiled

pyside6-uic ui\main_window.ui -o ui_compiled\main_window_ui.py
echo [2/11] main_window.ui compiled

pyside6-uic ui\dashboard.ui -o ui_compiled\dashboard_ui.py
echo [3/11] dashboard.ui compiled

pyside6-uic ui\customers.ui -o ui_compiled\customers_ui.py
echo [4/11] customers.ui compiled

pyside6-uic ui\orders.ui -o ui_compiled\orders_ui.py
echo [5/11] orders.ui compiled

pyside6-uic ui\inventory.ui -o ui_compiled\inventory_ui.py
echo [6/11] inventory.ui compiled

pyside6-uic ui\production.ui -o ui_compiled\production_ui.py
echo [7/11] production.ui compiled

pyside6-uic ui\machines.ui -o ui_compiled\machines_ui.py
echo [8/11] machines.ui compiled

pyside6-uic ui\employees.ui -o ui_compiled\employees_ui.py
echo [9/11] employees.ui compiled

pyside6-uic ui\reports.ui -o ui_compiled\reports_ui.py
echo [10/11] reports.ui compiled

pyside6-uic ui\settings.ui -o ui_compiled\settings_ui.py
echo [11/11] settings.ui compiled

echo.
echo ========================================
echo   ✅ All UI files compiled successfully!
echo ========================================
echo.
echo Compiled files are in: ui_compiled\
echo.
pause

