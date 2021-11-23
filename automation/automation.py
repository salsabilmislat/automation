import re

with open('assets/potential-contacts.txt','r')as f:
    content=f.read()
    # print(content)

def get_email(content):
    
    match_email = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', content)
    sorted_match_email=sorted(set(match_email))
    join_email='\n'.join(sorted_match_email)
    # print(join_email)

    with open('assets/emails.txt','w')as f:
        f.write(join_email)



def get_phone( content ):

    match_phone_number = re.findall( r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})', content )
    
    all_phone_number = []

    for phone in match_phone_number:
        
        if "(" in phone:
            phone = phone.replace( "(", "" )
        if ")" in phone or "." in phone:
            phone = phone.replace( ")", "-" )
            phone = phone.replace( ".", "-" )
        if len( phone ) == 10:
            phone = f"{phone[:3]}-{phone[3:6]}-{phone[6:]}"
        if not phone in all_phone_number:
            all_phone_number.append( phone )
    all_phone_number = sorted( all_phone_number )


    with open( 'assets/phone_numbers.txt', 'w' ) as result:
        for phone in all_phone_number:
            result.write( f"{phone}\n" )



if __name__ == "__main__":
    email = get_email(content)
    # # print(email)
    phone_number = get_phone(content)


# print (get_phone_from_text(content))

# match_phone=re.findall(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})',content)
# sorted_match_phone=sorted(set(match_phone))
# join_phone='\n'.join(sorted_match_phone)


