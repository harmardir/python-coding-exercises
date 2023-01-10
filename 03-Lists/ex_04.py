# Cross-Referencing Colors
#Write a program that cross-references a list of random colors with lists of warm, cool, and neutral colors. 
# Keep track of how many warm, cool, and neutral colors are in the list of random colors. 
# Also keep track of how many colors do not appear in any of the lists.

warm = ["red", "orange", "yellow", "burgundy", "pink", "rose", "pumpkin", "marigold", "gold", "citron", "amber"]
cool = ["blue", "green", "purple", "cyan", "violet", "indigo", "azure", "teal", "mint", "lime", "emerald"]
neutral = ["black", "white", "gray", "grey", "brown", "beige"]


colors = ["red", "black", "pink", "beige", "dark green", "azure", "amber", "light yellow"]
warm_count = 0
cool_count = 0
neutral_count = 0
misc_count = 0

for color in colors:
    if color in warm:
        warm_count += 1
    elif color in cool:
        cool_count += 1
    elif color in neutral:
        neutral_count += 1
    else:
        misc_count += 1

print("The total # of colors is ", len(colors))
print("There are ", warm_count, " warm colors")
print("There are ", cool_count, " cool colors")
print("There are ", neutral_count, " neutral colors")
print("There are ", misc_count, " miscellaneous colors")


