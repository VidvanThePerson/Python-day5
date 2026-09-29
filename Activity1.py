print("Smart School Planner")
print("Answer 3 quick questions and I will plan your day!\n")
day = input("What day is it? (Monday to Sunday):").strip().capitalize()
weather = input("What is the weather today? (sunny/rainy/cloudy):").strip().lower()
homework = input("Have you done your homework? (Yes/No):").strip().lower()
print()
print(f"Your plan for the {day}")
print("-"*35)
if day in ("Saturday","Sunday"):
    print("Day type: Weekend|Enjoy your free time!")
elif day == "Monday":
    print("Day type: Weekday|First day of the week, Pack your weekly planner!")
elif day == "Friday":
    print("Daytype: Weekday|Last day of the week, dont forget something!")
elif day in ("Tuesday","Wednesday","Thursday"):
    print("Daytype: Weekday|A Regular School day, Stay Focused!")
else:
    print("Daytype:Unrecognized|Please put a valid day")

if weather == "sunny" and homework == "yes":
    print("After School,Head to the park, Excellent weather, and homework done, enjoy")
if weather == "rainy" or weather == "cloudy":
    print("Things may get wet, pack a raincoat or an umbrella for the way to school and back to home!")
if not(homework == "yes"):
    print("Not done yet, make sure to finish your homework!")
if weather == "rainy" and not (homework == "yes"):
    print("Finish your homework and watch your favourite TV show afterwards!")
elif weather == "sunny" and homework == "yes" and not (day in("Saturday","Sunday")):
    print("All set for a FANTASTIC school day!")
elif weather == "sunny" and homework == "yes" and day in("Saturday","Sunday"):
    print("A perfect Weekend weather, Enjoy!")
else:
    print("Take it one step at a time, You got this!")
print()
print("Plan complete! Have a wonderful day!")

