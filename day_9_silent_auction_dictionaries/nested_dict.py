# travel_log = {
#     "countries_visited": {"France": ["Paris", "Lille", "Dijon"], "Germany": ["Berlin", "Hamburg", "Stuttgart"]}
# }
#
# for key in travel_log:
#     key_value = travel_log[key]
#     print(key_value)

# nesting dictionaries in dictionaries, accessed by keys
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "China": {"cities_visited": ["Nanjing", "Suzhou", "Beijing"], "total_visits": 1}
}
# Dict with two entries, each entry has three values with diff types of values
travel_log2 = {
    {"country": "France", "cities_visited": ["Paris", "Lillie", "Dijon"], "total_visits": 12},
    {"country": "China", "cities_visited": ["Nanjing", "Suzhou", "Beijing"], "total_visits": 1}
}
