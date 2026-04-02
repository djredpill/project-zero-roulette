import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

SMTP_SERVER = "smtp.mail.com"
SMTP_PORT = 587
SENDER_EMAIL = "djredpill@mail.com"
SENDER_PASSWORD = "4i8h2sMh$4jF92sM"
RECIPIENT_EMAIL = "misteek@gmail.com"

msg = MIMEMultipart()
msg['From'] = SENDER_EMAIL
msg['To'] = RECIPIENT_EMAIL
msg['Subject'] = "Project Zero Roulette - Revision 11b Update"

body = """Project Zero Roulette - Revision 11b

The latest revision has been pushed to GitHub and is now live at:
https://djredpill.github.io/project-zero-roulette/

Changes in Revision 11b:
1. Removed decimal points from ALL dollar amounts app-wide (e.g. $1,500 instead of $1,500.00)
2. Removed parentheses from side bet labels in Session History (e.g. "Odd $70" instead of "Odd ($70)")
3. Removed parentheses from pay line displays (e.g. "Pays: $180 total, $175 profit")
4. Tightened table column padding for better portrait mode display on iPhone
5. Fixed corrupted HTML tags in sticky header and session summary

IMPORTANT: Remember to Clear Saved App State in Settings after loading the updated site.

Attached:
- index.html - Latest source code for Textastic
"""

msg.attach(MIMEText(body, 'plain'))

html_path = "/home/ubuntu/project-zero-roulette/index.html"
with open(html_path, 'rb') as f:
    part = MIMEBase('text', 'html')
    part.set_payload(f.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="index.html"')
    msg.attach(part)

try:
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, msg.as_string())
    server.quit()
    print("Email sent successfully!")
except Exception as e:
    print(f"Error sending email: {e}")
