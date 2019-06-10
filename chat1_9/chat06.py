# alien = {'color': 'green', 'point': 5}
# print(alien['color'])
# print(alien['point'])
# del alien['color']
# print(alien)

# favorite_languages = {
#     'jen': 'python',
#     'sas': 'c',
#     'hhh': 'javascript',
#     'kkk': 'python'
# }

# print(favorite_languages.items())

# for name, language in favorite_languages.items():
#     print(name.title() + "'s favorite language is " + language.title() + ".")

# for name in favorite_languages.keys():
#     print(name.title())

# for name in sorted(favorite_languages.keys()):
#     print(name.title())

# for name in set(favorite_languages.values()):
#     print(name.title())

aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]: 
    print(alien)
print("...")
print("total number of aliens: " + str(len(aliens)))