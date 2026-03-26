from datetime import datetime, timedelta

print("________Welcome to AI Study Planner_________")

# Taking input from user
subjects = input("Enter subjects (comma separated): ").split(",")
difficulty = list(map(int, input("Enter difficulty (1-5)(comma seperated): ").split(",")))
marks = list(map(int, input("Enter your marks (out of 100)(comma seperated): ").split(",")))
total_hours = int(input("Enter total study hours: "))

# Calculate weight based on difficulty and weakness
weights = []

for i in range(len(subjects)):
    weak = 100 - marks[i]   # lower marks = more weak
    weight = difficulty[i] + (weak / 20)
    weights.append(weight)

# Total weight
total_weight = sum(weights)

# Calculate time for each subject
time_allocated = []

for w in weights:
    time = (w / total_weight) * total_hours
    time_allocated.append(time)

print("...Generating your timetable...")

# Start time
current_time = datetime.strptime("08:00", "%H:%M")

schedule = []

print("Your Study Timetable:")

for i in range(len(subjects)):
    hours = time_allocated[i]

    end_time = current_time + timedelta(hours=hours)

    line = current_time.strftime("%H:%M") + " - " + end_time.strftime("%H:%M") + " == " + subjects[i].strip()
    print(line)
    schedule.append(line)

    current_time = end_time

    # Add break
    break_end = current_time + timedelta(minutes=15)
    break_line = current_time.strftime("%H:%M") + " - " + break_end.strftime("%H:%M") + " == Break"
    print(break_line)
    schedule.append(break_line)

    current_time = break_end

# Save timetable in file
file = open("timetable.txt", "w")

for item in schedule:
    file.write(item + "\n")

file.close()

print("\nTimetable saved in 'timetable.txt'")

