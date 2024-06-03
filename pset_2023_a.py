def calculate_discount(courses):

    courses = courses * 10

    return courses // 100



courses = int(input("Enter amount of courses: "))

print("Can get Additional free courses: ", calculate_discount(courses)) if calculate_discount(courses) > 1 else print("Can get Addiotional free course: ", calculate_discount(courses))