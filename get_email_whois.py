import os

get_email_whois= 'for i in `cat list_domain`; do echo $i: $(whois $i | grep "Registrant Email" | cut -d: -f2);done'
os.system(get_email_whois)