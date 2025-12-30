def parse_address(full_address):
    parts = [p.strip() for p in full_address.split(",")]

    street_address = []
    city = ""
    zip_code = ""
    state = ""
    country = ""

    last_part_words = parts[-1].split()
    country = last_part_words[-1]

    if len(last_part_words) > 1:
        state = " ".join(last_part_words[:-1])

    city_zip_words = parts[-2].split()
    zip_code = city_zip_words[-1]
    city = " ".join(city_zip_words[:-1])

    if len(parts) > 2:
        street_address = parts[:-2]

    if street_address:
        print("address:", ", ".join(street_address))

    print("city:", city)
    print("zip:", zip_code)

    if state:
        print("state:", state)

    print("country:", country)


user_input = input("Enter full address: ")
parse_address(user_input)
