def mask(people):
    for person in people:
        phone_number = person['phone']
        masked_phone_number = '*' * (len(phone_number) - 2) + phone_number[-2:]
        person['phone'] = masked_phone_number
    
    return people