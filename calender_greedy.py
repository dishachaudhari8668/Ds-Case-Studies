
def time_to_minutes(time):
    hours, minutes = map(int, time.split(":"))
    return hours * 60 + minutes


events = []

n = int(input("Enter number of events: "))

for i in range(n):
    name = input("Enter event name: ")
    start = input("Enter start time (HH:MM): ")
    end = input("Enter end time (HH:MM): ")

    start_minutes = time_to_minutes(start)
    end_minutes = time_to_minutes(end)

    if start_minutes >= end_minutes:
        print("Invalid time. End time must be later.")
        continue

    events.append((name, start_minutes, end_minutes))

events.sort(key=lambda event: event[2])

selected = []
last_end = -1

for event in events:
    name, start, end = event

    if start >= last_end:
        selected.append(event)
        last_end = end

print("\nSelected events:")

for name, start, end in selected:
    print(name, "-", 
          f"{start // 60:02d}:{start % 60:02d}",
          "to",
          f"{end // 60:02d}:{end % 60:02d}")

print("Total selected events:", len(selected))
