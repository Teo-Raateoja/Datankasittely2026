def anonymize(people):
    for person in people:
        name = person.get("name", "")
        first_name = name.split(maxsplit=1)[0] if name.split() else ""
        person["name"] = first_name[0] if first_name else None

        ##Tässä käytin AI:n apua, jotta sain toimimaan.

    return people