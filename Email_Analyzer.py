import imaplib
import email

# Connect to the IMAP server and fetch the emails
imap_server = imaplib.IMAP4_SSL('imap.example.com')
imap_server.login('user@example.com', 'password')
imap_server.select('INBOX')
_, email_ids = imap_server.search(None, 'ALL')
for email_id in email_ids[0].split():
    _, msg = imap_server.fetch(email_id, '(RFC822)')
    # Parse the email using the email library
    email_message = email.message_from_bytes(msg[0][1])
    sender = email.utils.parseaddr(email_message['From'])[1]
    subject = email_message['Subject']
    body = ''
    if email_message.is_multipart():
        # Extract the plain text version of the email body
        for part in email_message.get_payload():
            if part.get_content_type() == 'text/plain':
                body = part.get_payload()
                break
    else:
        body = email_message.get_payload()
    attachments = []
    # Extract any attachments
    for part in email_message.walk():
        if part.get_content_disposition() == 'attachment':
            attachments.append(part.get_filename())
    # Analyze the email and determine whether it is suspicious
    suspicious = False
    if 'viagra' in body.lower():
        suspicious = True
    if sender in bad_senders:
        suspicious = True
    # Take appropriate action based on the analysis
    if suspicious:
        imap_server.store(email_id, '+FLAGS', '\\Deleted')
        print(f'Deleted suspicious email from {sender} with subject "{subject}"')
    else:
        print(f'Email from {sender} with subject "{subject}" is not suspicious')
imap_server.expunge()
imap_server.close()
imap_server.logout()
