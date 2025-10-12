from typing import List, Optional

# ===== Flight class =====
class Flight:
    def __init__(self, flight_no: str, origin: str, destination: str, departure_time: str, seats: int):
        self.flight_no = flight_no
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.seats = seats

    def __str__(self):
        return f"Flight {self.flight_no} | {self.origin} → {self.destination} | Seats Available: {self.seats}"

# ===== QuickSort & Binary Search =====
def quicksort(flights: List['Flight'], low: int, high: int, key=lambda x: x.flight_no):
    if low < high:
        p = partition(flights, low, high, key)
        quicksort(flights, low, p - 1, key)
        quicksort(flights, p + 1, high, key)

def partition(flights: List['Flight'], low: int, high: int, key):
    pivot = flights[high]
    pivot_key = key(pivot)
    i = low - 1
    for j in range(low, high):
        if key(flights[j]) <= pivot_key:
            i += 1
            flights[i], flights[j] = flights[j], flights[i]
    flights[i + 1], flights[high] = flights[high], flights[i + 1]
    return i + 1

def binary_search(flights: List['Flight'], target: str, key=lambda x: x.flight_no) -> Optional[int]:
    low, high = 0, len(flights) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_val = key(flights[mid])
        if mid_val == target:
            return mid
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1
    return None

# ===== Flight Reservation System =====
class FlightReservationSystem:
    def __init__(self):
        self.flights: List[Flight] = []

    def add_flight(self, flight: Flight):
        self.flights.append(flight)

    def sort_by_departure_time(self):
        def time_key(f: Flight):
            hh, mm = map(int, f.departure_time.split(":"))
            return hh * 60 + mm
        quicksort(self.flights, 0, len(self.flights) - 1, key=time_key)

    def sort_by_flight_no(self):
        quicksort(self.flights, 0, len(self.flights) - 1, key=lambda f: f.flight_no)

    def list_flights(self):
        if not self.flights:
            print("No flights available.")
            return
        self.sort_by_departure_time()
        print("\n📋 Available Flights:")
        for f in self.flights:
            print(f"Flight {f.flight_no} | {f.origin} → {f.destination}")

    def find_flight(self, flight_no: str) -> Optional[Flight]:
        self.sort_by_flight_no()
        index = binary_search(self.flights, flight_no, key=lambda f: f.flight_no)
        if index is not None:
            return self.flights[index]
        return None

    def book_seat(self, flight_no: str):
        flight = self.find_flight(flight_no)
        if flight:
            if flight.seats > 0:
                flight.seats -= 1
                return [f"✅ Seat booked on {flight_no}. Remaining seats: {flight.seats}"]
            else:
                return ["❌ No seats available on this flight."]
        else:
            return ["❌ Flight not found."]

    def cancel_booking(self, flight_no: str):
        flight = self.find_flight(flight_no)
        if flight:
            flight.seats += 1
            return [f"✅ Booking cancelled on {flight_no}. Seats now: {flight.seats}"]
        else:
            return ["❌ Flight not found."]

    def search_by_route(self, origin: str, destination: str):
        found = False
        result = [f"🔍 Searching flights from {origin} → {destination}"]
        for f in self.flights:
            if f.origin.lower() == origin.lower() and f.destination.lower() == destination.lower():
                result.append(f"Flight {f.flight_no} | {f.origin} → {f.destination}")
                found = True
        if not found:
            result.append("❌ No flights found for this route.")
        return result

# ===== Main Function with Output History =====
def main():
    frs = FlightReservationSystem()
    output_history: List[str] = []

    # Predefined Flights
    predefined_flights = [
        Flight("AI101", "Mumbai", "Delhi", "08:30", 10),
        Flight("6E202", "Delhi", "Bangalore", "09:45", 5),
        Flight("SG303", "Hyderabad", "Chennai", "11:15", 8),
        Flight("UK404", "Kolkata", "Mumbai", "14:00", 2),
        Flight("IX505", "Bangalore", "Pune", "16:30", 0)
    ]
    for flight in predefined_flights:
        frs.add_flight(flight)

    while True:
        print("\n===== ✈️ Flight Reservation System =====")
        print("1. Display Available Flights")
        print("2. Search Flights by Route")
        print("3. Search Flight by Flight No")
        print("4. Book Seat")
        print("5. Cancel Booking")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            # Directly display flights, not stored in history
            frs.list_flights()

        elif choice == "2":
            origin = input("Enter origin city: ").strip()
            destination = input("Enter destination city: ").strip()
            new_output = frs.search_by_route(origin, destination)
            output_history.extend(new_output)
            print("\n".join(output_history))

        elif choice == "3":
            flight_no = input("Enter flight number to search: ").strip().upper()
            flight = frs.find_flight(flight_no)
            if flight:
                new_output = [f"✅ Flight found: Flight {flight.flight_no} | {flight.origin} → {flight.destination}"]
            else:
                new_output = ["❌ Flight not found."]
            output_history.extend(new_output)
            print("\n".join(output_history))

        elif choice == "4":
            flight_no = input("Enter flight number to book: ").strip().upper()
            new_output = frs.book_seat(flight_no)
            output_history.extend(new_output)
            print("\n".join(output_history))

        elif choice == "5":
            flight_no = input("Enter flight number to cancel: ").strip().upper()
            new_output = frs.cancel_booking(flight_no)
            output_history.extend(new_output)
            print("\n".join(output_history))

        elif choice == "0":
            print("👋 Exiting. Thank you for using the system!")
            break

        else:
            new_output = ["⚠️ Invalid choice. Please try again."]
            output_history.extend(new_output)
            print("\n".join(output_history))

        input("\n🔁 Press Enter to continue...")

if __name__ == "__main__":
    main()
