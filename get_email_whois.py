import whois

f=open("list_domain","r")
domain_name=f.read().splitlines()

for i in domain_name:
  print(whois.whois(i).emails)
