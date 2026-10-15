from datetime import datetime

def anonymize(people):
    for person in people:
        birth_date = datetime.strptime(person['birthdate'], '%Y-%m-%d')
        person['birth_year'] = birth_date.year
        del person['name']
        del person['birthdate']
        city = person.pop('city')
        person['city_initial'] = city[0] if city else None

    return people