

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(user,passwd)
mail.select("inbox")
while True:
    result, idData = mail.uid('search', query, "ALL")
    processIDs(idData)
    time.sleep(60)