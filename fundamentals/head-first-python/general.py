from datetime import datetime
vowel = set('aeiou')

word = input("enter you word: ")

# an easier way instead of checking one by one and append it to a list(data should be always set)
for w in vowel.intersection(set(word)):
    print(w)



# assets/data.png
flight_times = {
    '09:35': 'FREEPORT',
    '09:55': 'WEST END',
    '12:00': 'TREASURE CAY',
    '10:45': 'TREASURE CAY',
    '11:45': 'ROCK SOUND',
    '17:00': 'FREEPORT',
    '17:55': 'ROCK SOUND',
    '19:00': 'WEST END',
    '20:00': 'fdsfsd',
}

def convert2ampms(time24: str) -> str:
    try:
        return datetime.strptime(time24, "%H:%M").strftime("%I:%M %p")
    except ValueError as e:
        return "Invalid time format"

dirty_data = {}
res = {convert2ampms(key): value for key , value in flight_times.items()}
print(res)

cleaned_data = {}
for des in set(res.values()):
    times = [key for key , value in res.items() if value == des]
    cleaned_data[des] = times
    if len(times) != 2 or any("Invalid time format" in time for time in times):
        dirty_data[des] = times
    else:
        print(des , '->' , times)

print("Dirty Data: ")
for des, value in dirty_data.items():
    print(des , "->" , value)

print(cleaned_data.items())