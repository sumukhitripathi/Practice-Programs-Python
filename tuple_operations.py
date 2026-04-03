n=int(input("Enter no of students: "))
emails=[]
for i in range(n):
    email=input("Enter email: ")
    emails.append(email)
email_t=tuple(emails)
usernames=[]
domains=[]
for email in email_t:
    username,domain=email.split("@")
    usernames.append(username)
    domains.append(domain)
usernames_t=tuple(usernames)
domains_t=tuple(domains)
print("Email addresses: ",email_t)
print("Usernames: ",usernames_t)
print("Domains: ",domains_t)