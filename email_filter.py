""" Filtering personal and enterprise emails """

emails = [
    "antonio@gmail.com",
    "juan@hotmail.com",
    "pedro@amazon.com",
    "julian@dyc.net",
    "pablo@yahoo.com"
]

personal = ("gmail", "hotmail", "yahoo")

personal_emails = []
corporative_emails = []

for email in emails:
    for domain in personal:
        if domain in email:
            personal_emails.append(email)
    if email not in personal_emails:
        corporative_emails.append(email)

print(f"Personal emails: {personal_emails}")
print(f"Corporative emails: {corporative_emails}")
