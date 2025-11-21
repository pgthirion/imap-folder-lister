# IMAP Folder Lister

A minimalist Python script that connects to an email server via IMAP and prints a list of all available folders (mailboxes).

This tool is useful for developers who need to find the exact folder paths (e.g., `"INBOX"`, `"Sent Items"`, `"PayFast/Orders"`) to use in other automation scripts.

## Features

* **Simple Connection:** Connects securely using SSL.
* **Complete Listing:** Retrieves all folders available on the account.
* **Debug Helper:** prints raw folder names exactly as the server sees them.

## Prerequisites

* Python 3.x

## Installation

1.  **Download:**
    * Click the green **<> Code** button at the top of this page.
    * Select **Download ZIP**.
    * Extract the ZIP file to a folder on your computer.

2.  **Dependencies:**
    This script uses the standard Python library, so no `pip install` is necessary.

## Configuration

1.  Open `listfolders.py` in a text editor.
2.  Fill in your email credentials at the top of the file:

    ```python
    IMAP_SERVER = "imap.gmail.com"  # Replace with your server
    EMAIL_ACCOUNT = "your-email@example.com"
    PASSWORD = "your-password"
    ```

## Usage

1.  **Run the Script:**
    ```bash
    python listfolders.py
    ```

2.  **Output:**
    The script will print a list of folders to your terminal.
    
    *Example Output:*
    ```text
    (\HasNoChildren) "/" "INBOX"
    (\HasNoChildren) "/" "Sent"
    (\HasChildren) "/" "PayFast"
    (\HasNoChildren) "/" "PayFast/Orders"
    ```

    You can then copy these names (e.g., `"PayFast/Orders"`) into your other automation scripts.
