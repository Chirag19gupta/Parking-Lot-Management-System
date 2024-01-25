from datetime import datetime

class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.spaces = [None] * capacity
        self.fee_per_hour = 10  # fee in dollars
        self.occupied_count = 0

    def check_in(self, vehicle_number, entry_time):
        if self.occupied_count < self.capacity:
            for i in range(self.capacity):
                if self.spaces[i] is None:
                    # Convert string time to datetime object
                    entry_time_obj = datetime.strptime(entry_time, "%Y-%m-%d %H:%M:%S")
                    self.spaces[i] = {'vehicle_number': vehicle_number, 'entry_time': entry_time_obj}
                    self.occupied_count += 1
                    return f"Vehicle {vehicle_number} parked in slot {i+1}."
            return "No available slots."
        else:
            return "Parking lot is full."

    def check_out(self, vehicle_number, exit_time):
        for i, space in enumerate(self.spaces):
            if space and space['vehicle_number'] == vehicle_number:
                entry_time = space['entry_time']
                # Convert string time to datetime object
                exit_time_obj = datetime.strptime(exit_time, "%Y-%m-%d %H:%M:%S")
                parked_hours = (exit_time_obj - entry_time).total_seconds() / 3600
                fee = round(parked_hours * self.fee_per_hour, 2)
                self.spaces[i] = None
                self.occupied_count -= 1
                return f"Vehicle {vehicle_number} checked out. Entry Time: {entry_time}, Exit Time: {exit_time_obj}, Parking fee: ${fee}."
        return "Vehicle not found."

    def available_spaces(self):
        return self.capacity - self.occupied_count

# Create a parking lot with 5 spaces
parking_lot = ParkingLot(5)

# Check-in a vehicle with a specified entry time
vehicle_number = input("Enter the vehical number")
entry_time = input("Enter the year and time of entry")
print(parking_lot.check_in(vehicle_number, entry_time))

# Simulate a short parking duration
# In actual use, this time would elapse naturally

# Check-out the vehicle with a specified exit time
exit_time = input("Enter the year and time of exit")
print(parking_lot.check_out(vehicle_number, exit_time))

# Check available spaces
print(f"Available spaces: {parking_lot.available_spaces()}")
