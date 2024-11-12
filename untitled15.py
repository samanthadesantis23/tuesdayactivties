class Clock:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def tick(self):
        # Increment seconds by 1
        self.seconds += 1
        
        # If seconds reach 60, reset seconds and increment minutes
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
            
            # If minutes reach 60, reset minutes and increment hours
            if self.minutes == 60:
                self.minutes = 0
                self.hours += 1
                
                # If hours reach 24, reset to 0 (24-hour clock format)
                if self.hours == 24:
                    self.hours = 0

    def set(self, hours, minutes):
        # Set the clock to a specific hour and minute, seconds are set to 0
        self.hours = hours
        self.minutes = minutes
        self.seconds = 0

    def __str__(self):
        # Format the time as "hh:mm:ss", with leading zeros if needed
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

# Example usage
clock = Clock(23, 59, 55)
print(clock)  # 23:59:55
clock.tick()
print(clock)  # 23:59:56
clock.tick()
print(clock)  # 23:59:57
clock.tick()
print(clock)  # 23:59:58
clock.tick()
print(clock)  # 23:59:59
clock.tick()
print(clock)  # 00:00:00 (reset to 00:00:00)
clock.tick()
print(clock)  # 00:00:01
clock.set(12, 5)
print(clock)  # 12:05:00
