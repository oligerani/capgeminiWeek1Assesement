def verification():
    users = [
    {"email": "alice@example.com", "verified": True},
    {"email": "bob@example.com", "verified": False},
    {"email": "charlie@example.com", "verified": True},
    {"email": "daisy@example.com", "verified": False}
	 ]
    corrected_user=[user["email"] for user in filter(lambda x:(x["verified"]),users)]
    
    
    print(corrected_user)
     
    
verification()    