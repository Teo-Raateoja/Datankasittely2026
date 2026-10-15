def mask(people):
    for person in people:
        email = person['email']
        local_part, domain_part = email.split('@')
        masked_local_part = '*' * len(local_part)
        person['email'] = masked_local_part + '@' + domain_part
        
        phone_number = person['phone']
        masked_phone_number = '*' * (len(phone_number) - 2) + phone_number[-2:]
        person['phone'] = masked_phone_number
    
    return people