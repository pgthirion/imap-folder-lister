import imaplib

IMAP_SERVER = ""
EMAIL_ACCOUNT = ""
PASSWORD = ""

mail = imaplib.IMAP4_SSL(IMAP_SERVER)
mail.login(EMAIL_ACCOUNT, PASSWORD)

status, folders = mail.list()
if status == "OK":
    for f in folders:
        print(f)
else:
    print("Could not list folders:", status)

mail.logout()
