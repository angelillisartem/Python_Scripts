import email_validator #install library "email validator" with [pip install email_validator]

def validazione_email(email):
    try:
        email_validator.validate_email(email)
        return True
    except email_validator.EmailNotValidError:
        return False

email = str(input("Inserisci email da validare"))

if validazione_email(email):
    print("E-mail valida.")
else:
    print("E-mail non valida.")