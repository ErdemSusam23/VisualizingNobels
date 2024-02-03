import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


nobel = pd.read_csv("nobel.csv")
top_gender = nobel["sex"].value_counts()
top_country = nobel["birth_country"].value_counts()

#----------------PLOT 1----------------
plt.figure(figsize=(10,6))
#top_gender.plot(kind="bar", title = "Plot of Genders", xlabel = "Gender", ylabel = "Count")
plt.show()



#----------------PLOT 2----------------
plt.clf()
#top_country.head(10).plot(kind = "bar", title = "Plot of Countries", xlabel = "Country", ylabel="Count",)
plt.show()



print("Gender with the most nobel prizes: " + str(top_gender.index[0]))
print("Country with the most nobel prizes: " + str(top_country.index[0]))
print("\n")

nobel["usa_born_winners"] = nobel["birth_country"] == "United States of America"
nobel["decade"] = np.floor(nobel["year"] / 10) * 10

proportion = nobel.groupby("decade")["usa_born_winners"].mean()
proportion = proportion[::-1]


#----------------PLOT 3----------------
plt.clf()
#proportion.plot(kind = "bar", title = "Plot of Proportion", xlabel="Decade", ylabel="Proportion", grid=True)
plt.show()


max_decade_usa = proportion.idxmax()
print("Decade with most nobel prizes in USA: "+str(+max_decade_usa))
print("\n")

nobel["female"] = nobel["sex"] == "Female"
female_proportion = nobel.groupby(["decade","category"])["female"].mean()
female_proportion = female_proportion[::-1]


#----------------PLOT 4----------------
plt.clf()
"""female_proportion.sort_values(ascending = False).head(10).plot(kind="bar", xlabel="Decade", ylabel="Category", 
                                                               title="Plot of Female Proportions")"""
plt.show()

max_female_dict = {}
max_decade_females = female_proportion.idxmax()
data = {max_decade_females[0]:max_decade_females[1]}
max_female_dict = data
print("Decade and Category with the highest proportion of female award winners:")
print(max_female_dict)
print("\n")

nobel_sorted_by_year = nobel.sort_values("year")
nobel_female = nobel_sorted_by_year[nobel_sorted_by_year["sex"] == "Female"]
first_woman_name = nobel_female.iloc[0].loc[["full_name"]]
first_woman_category = nobel_female.iloc[0].loc[["category"]]
print("First Woman to win nobel prize: ")
print(first_woman_name)
print("\n")
print("Category of First female winner is: ")
print(first_woman_category)
print("\n")



nobel_grouped_by_name = nobel.groupby(["full_name"])
nobel_name_counts = nobel_grouped_by_name["full_name"].value_counts()
nobel_name_counts = nobel_name_counts.sort_values(ascending = False)
winners_more_than_one = nobel_name_counts[nobel_name_counts >= 2].index
repeat_list = list(winners_more_than_one)
print("List of peoples or organizations who has won more than 1 nobel prize")
for item in repeat_list:
    print(item)

plt.show()










