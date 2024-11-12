class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def tick(self):
        # Increment the time by 1 second
        self.seconds += 1
        
        # If seconds reach 60, reset seconds and increment minutes
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1

    def __str__(self):
        # Format time as "minutes:seconds"
        return f"{self.minutes}:{self.seconds:02d}"

# Test the Stopwatch
watch = Stopwatch()
for i in range(3600):
    print(watch)
    watch.tick()
