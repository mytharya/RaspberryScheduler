#get user email address
email = input ("What is your email address? ").strip()
#slice username
#bobdoe@email.com
user = email[:email.index("@")]
#slice domain name
domain = email[email.index("@") +1 :]
#display ouput message
output = "Your username is {} and your domain name is {}.".format(user,domain)
#display output
print(output)
