import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

# Email configuration
SMTP_SERVER = "smtp.mail.com"
SMTP_PORT = 587
SENDER_EMAIL = "djredpill@mail.com"
SENDER_PASSWORD = "4i8h2sMh$4jF92sM"
RECIPIENT_EMAIL = "misteek@gmail.com"

# Create message
msg = MIMEMultipart()
msg['From'] = SENDER_EMAIL
msg['To'] = RECIPIENT_EMAIL
msg['Subject'] = "Project Zero Roulette - Revision 11 Update"

body = """Project Zero Roulette - Revision 11

The latest revision has been pushed to GitHub and is now live at:
https://djredpill.github.io/project-zero-roulette/

Changes in Revision 11:
1. Numpad Auto-Submit - Tapping a number now immediately submits the spin (no more "Place Spin" button needed). Undo still works for mistakes.
2. Column Headers Updated - "Zeros Stake" changed to "0's Stake" and "Balance" abbreviated to "Bal." to reduce table cramping.
3. Side Bet Labels Shortened - Now shows compact labels with dollar amounts: "Odd ($70)", "Red ($50)", "1/12 ($30)", "Col2 ($40)".

IMPORTANT: Remember to Clear Saved App State in Settings after loading the updated site to avoid cache conflicts.

Attached:
- Revision_11_Summary.pdf - Full summary of changes
- index.html - Latest source code for Textastic

GitHub Token expires: June 30, 2026
"""

msg.attach(MIMEText(body, 'plain'))

# Attach PDF
pdf_path = "/home/ubuntu/project-zero-roulette/Revision_11_Summary.pdf"
with open(pdf_path, 'rb') as f:
    part = MIMEBase('application', 'pdf')
    part.set_payload(f.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename="Revision_11_Summary.pdf"')
    msg.attach(part)

# Attach index.html
html_path = "/home/ubuntu/project-zero-roulette/index.html"
with open(html_path, 'rb') as f:
    part = MIMEBase('text', 'html')
    part.set_payload(f.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename="index.html"')
    msg.attach(part)

# Send email
try:
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, msg.as_string())
    server.quit()
    print("Email sent successfully!")
except Exception as e:
    print(f"Error sending email: {e}")
