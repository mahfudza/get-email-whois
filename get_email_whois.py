import whois

f=open("list_domain","r")
domain_name=f.read().splitlines()

for i in domain_name:
  emails=''
  email_list=whois.whois(i).emails
  #check if emails is list or not
  is_list=isinstance(email_list, list)

  #if list then doing for loop and make it as string
  #if not then just print as is
  #store it into variable then embed that variable with domain name
  if is_list:
      for x in email_list:
          emails+=x+", "
  else:
      emails=email_list
  
  print(i+" : "+emails.rstrip(', '));

  