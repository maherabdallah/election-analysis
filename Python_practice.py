# counties = ["Arapahoe","Denver","Jefferson"]
# if counties[1] == 'Denver':
#     print(counties[1])

# # counties = ["Arapahoe","Denver","Jefferson"]
# # if "El Paso" in counties:
# #     print("El Paso is in the list of counties.")
# # else:
# #     print("El Paso is not the list of counties.")


#     if "Arapahoe" in counties and "El Paso" not in counties:
#         print("Only Arapahoe is in the list of counties.")
#     else:
#         print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# for county, voters in counties_dict.items():
#     print(county, "county has", voters, "registered voters.")
# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                 {"county":"Denver", "registered_voters": 463353},
#                 {"county":"Jefferson", "registered_voters": 432438}]

# for county_dict in voting_data:
#     print(county_dict)
# for i in range(len(voting_data)):

#       print(voting_data[i]['county'])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

county_and_voters = (
    f"{counties_dict.keys[0]} county has {counties_dict.value[0]}"
)