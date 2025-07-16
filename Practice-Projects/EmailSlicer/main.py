def email_slicer():
   
   
    email = input("Enter your email address: ").strip()

   
    try:
        username, domain = email.split('@')
        print(f"Username: {username}")
        print(f"Domain: {domain}")
    except ValueError:
        print("Invalid email format. Please make sure the email contains '@'.")


email_slicer()
