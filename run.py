from pywinauto.application import Application
import time
"""
run.py

This script automates data entry into the Crystal PM application using the pywinauto library.
It connects to the running Crystal PM window, locates specific input fields by their automation IDs,
and enters predefined values (such as payment amount and last 4 digits of a card).
If the automation IDs are incorrect or controls are not found, it prints the control identifiers
to help the user adjust the script.

Usage:
- Ensure Crystal PM is running and visible.
- Adjust the auto_id values if necessary by inspecting the control identifiers.
- Run this script to automate filling in payment information.

Dependencies:
- pywinauto
- pywin32
"""


# --- Step 1: Connect to your application ---
try:
    app = Application(backend="uia").connect(title_re=".*Crystal PM.*", timeout=10)
    print("Successfully connected to the Crystal PM application.")
except Exception as e:
    print(f"Error: Could not connect to the application. Details: {e}")
    exit()

# --- Step 2: Get a handle on the main window ---
main_win = app.window(title_re=".*Crystal PM.*")
main_win.set_focus()

# --- Step 3: Find the input fields by their 'auto_id' and enter text ---
try:
    print("Targeting input fields by their auto_id...")

    # Find the Amount field and enter text
    # amount_input = main_win.child_window(auto_id="textAmount", control_type="Edit")
    amount_input = main_win.child_window(auto_id="txtPayCreditAmount", control_type="Edit")
    amount_input.set_text("250.00")
    print("   Set Amount to '250.00'")

    # Find the Last4 field and enter text
    last4_input = main_win.child_window(auto_id="textLast4", control_type="Edit")
    last4_input.set_text("1234")
    print("   Set Last4 to '1234'")
    
    # # Find the Memo field and enter text
    # memo_input = main_win.child_window(auto_id="textMemo", control_type="Edit")
    # memo_input.set_text("Patient co-payment")
    # print("   Set Memo to 'Patient co-payment'")

except Exception as e:
    print("Error: Could not find one of the input fields.")
    print("   My guess for an auto_id might be wrong.")
    print("   Please check the full output of print_control_identifiers() for the correct auto_id.")
    print(f"   Details: {e}")

    # For Debugging: If it fails, run this again to get the complete list of controls
    main_win.print_control_identifiers()