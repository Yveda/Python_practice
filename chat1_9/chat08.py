# def get_formatted_name(first_name, middle_name, last_name):
#     full_name = first_name + ' ' + middle_name + ' ' + last_name
#     return full_name.title()
# musician = get_formatted_name('join', 'lee', 'hooker')
# print(musician)

# def make_pizza(*toppings):
#     print(toppings)

# make_pizza('penenegg')
# make_pizza('gegeg','egeg','gegege')

def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('eleagae', 'fageg', localtion='gagrgr', filed='gagwega')
print(user_profile)