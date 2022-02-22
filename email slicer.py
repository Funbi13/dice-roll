email = input("Enter your email address: ").strip()
username = email[:email.index("@")]
domain_name = email[email.index("@")+1:]
res = "username is '{}' and doamin name is '{}'".format(username, domain_name)
print(res)