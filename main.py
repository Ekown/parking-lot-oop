import math

class Vehicle:
    def __init__(self, license_plate_number, vehicle_type):
        self.license_plate_number = license_plate_number
        self.vehicle_type = vehicle_type


class ParkingSlot:
    def __init__(self, slot_number, slot_type):
        self.slot_number = slot_number
        self.slot_type = slot_type
        self.is_occupied = False
        self.vehicle = None

    def allocate(self, vehicle):
        self.is_occupied = True
        self.vehicle = vehicle

    def free(self):
        self.is_occupied = False
        self.vehicle = None


class ParkingLot:
    def __init__(self, entry_points, parking_slots, vehicle_map):
        self.entry_points = entry_points
        self.parking_slots = parking_slots
        self.vehicle_map = vehicle_map

    def park_vehicle(self, vehicle):
        for slot in self.parking_slots:
            if not slot.is_occupied and vehicle.vehicle_type in slot.slot_type:
                slot.allocate(vehicle)
                print(f"Vehicle with license plate number {vehicle.license_plate_number} parked at slot {slot.slot_number}")
                return
        print("No available slot for the vehicle type.")

    def unpark_vehicle(self, vehicle):
        for slot in self.parking_slots:
            if slot.is_occupied and slot.vehicle.license_plate_number == vehicle.license_plate_number:
                slot.free()
                print(f"Vehicle with license plate number {vehicle.license_plate_number} has been unparked.")
                return
        print("Vehicle not found in the parking lot.")

    def calculate_fee(self, entry_time, exit_time, vehicle_type, slot_type):
        hourly_rate = 0
        if slot_type == "SP":
            hourly_rate = 20
        elif slot_type == "MP":
            hourly_rate = 60
        elif slot_type == "LP":
            hourly_rate = 100

        total_hours = math.ceil((exit_time - entry_time).total_seconds() / 3600)
        fee = 40 + max(0, total_hours - 3) * hourly_rate

        if total_hours > 24:
            fee = ((total_hours // 24) * 5000) + fee

        return fee


def create_parking_lot():
    # Get user input for number of entry points, rows, and columns
    num_entry_points = int(input("Enter the number of entry points: "))
    num_rows = int(input("Enter the number of rows: "))
    num_columns = int(input("Enter the number of columns: "))

    # Initialize an empty parking lot map
    parking_map = [["" for _ in range(num_columns)] for _ in range(num_rows)]

    # Get user input for entry point coordinates
    entry_points = []
    for i in range(num_entry_points):
        row = int(input(f"Enter the row coordinate for entry point {i+1}: "))
        column = int(input(f"Enter the column coordinate for entry point {i+1}: "))
        
        # Check if the entry point is on the edge or side of the table
        if row == 0 or row == num_rows - 1 or column == 0 or column == num_columns - 1:
            entry_points.append((row, column))
            parking_map[row][column] = 'E'
        else:
            print("Entry points are only allowed on the edges and sides of the table. Please enter valid coordinates.")
            return create_parking_lot()  # Restart the creation process if invalid coordinates are provided

    # Get user input for parking slot sizes
    parking_slots = []
    for row in range(num_rows):
        for column in range(num_columns):
            slot_number = f"{chr(row+65)}{column+1}"
            if (row, column) not in entry_points:
                slot_type = input(f"Enter the parking slot size for slot {slot_number}: ")
                parking_map[row][column] = slot_type
                parking_slots.append(ParkingSlot(slot_number, slot_type))

    # Create the ParkingLot instance
    vehicle_map = {
        "S": 0,  # Small vehicle
        "M": 1,  # Medium vehicle
        "L": 2,  # Large vehicle
    }
    parking_lot = ParkingLot(entry_points, parking_slots, vehicle_map)

    return parking_map, parking_lot


def display_parking_lot(parking_map):
    num_rows = len(parking_map)
    num_columns = len(parking_map[0])

    print("\nParking Lot Map:")
    for row in range(num_rows):
        for column in range(num_columns):
            print(parking_map[row][column], end=" ")
        print()
    print()


def park_vehicle(parking_lot):
    license_plate_number = input("Enter the license plate number of the vehicle: ")
    vehicle_type = input("Enter the vehicle type (S/M/L): ")
    vehicle = Vehicle(license_plate_number, vehicle_type)
    parking_lot.park_vehicle(vehicle)


def unpark_vehicle(parking_lot):
    license_plate_number = input("Enter the license plate number of the vehicle to unpark: ")
    vehicle = Vehicle(license_plate_number, None)
    parking_lot.unpark_vehicle(vehicle)


def calculate_fee(parking_lot):
    license_plate_number = input("Enter the license plate number of the vehicle: ")
    entry_time = input("Enter the entry time (YYYY-MM-DD HH:MM): ")
    exit_time = input("Enter the exit time (YYYY-MM-DD HH:MM): ")
    vehicle_type = input("Enter the vehicle type (S/M/L): ")
    slot_type = input("Enter the slot type (SP/MP/LP): ")

    # Convert entry and exit times to datetime objects
    entry_time = datetime.strptime(entry_time, "%Y-%m-%d %H:%M")
    exit_time = datetime.strptime(exit_time, "%Y-%m-%d %H:%M")

    fee = parking_lot.calculate_fee(entry_time, exit_time, vehicle_type, slot_type)
    print(f"Total fee for vehicle {license_plate_number}: {fee}")


def main():
    parking_map, parking_lot = create_parking_lot()

    # display_parking_lot(parking_map)

    while True:
        display_parking_lot(parking_map)
        
        print("1. Park Vehicle")
        print("2. Unpark Vehicle")
        print("3. Calculate Fee")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            park_vehicle(parking_lot)
        elif choice == "2":
            unpark_vehicle(parking_lot)
        elif choice == "3":
            calculate_fee(parking_lot)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
