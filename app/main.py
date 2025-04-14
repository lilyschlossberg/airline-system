# app/main.py

from datetime import datetime, timedelta

DEFAULT_SEAT_COUNT = 150


class Flight:
    def __init__(self, number, origin, destination, departure_time, duration_minutes, aircraft_type):
        self.flight_number = number
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = departure_time + timedelta(minutes=duration_minutes)
        self.aircraft_type = aircraft_type
        self.seats_available = DEFAULT_SEAT_COUNT
        self.crew = []
        self.passengers = []

    def assign_crew(self, crew_member):
        self.crew.append(crew_member)

    def book_seat(self, passenger):
        if self.seats_available <= 0:
            raise Exception("No seats available on this flight.")
        self.seats_available -= 1
        self.passengers.append({
            "passenger": passenger,
            "seat_number": DEFAULT_SEAT_COUNT - self.seats_available
        })


class Passenger:
    def __init__(self, name, passport_number):
        self.name = name
        self.passport_number = passport_number
        self.registered_on = datetime.now()


class CrewMember:
    def __init__(self, name, role):
        self.name = name
        self.role = role


class AirlineSystem:
    def __init__(self):
        self.flights = {}
        self.passengers = {}
        self.crew_members = []

    def add_flight(self, *args, **kwargs):
        flight = Flight(*args, **kwargs)
        self.flights[flight.flight_number] = flight
        print(f"[INFO] Flight {flight.flight_number} added.")

    def register_passenger(self, name, passport_number):
        passenger = Passenger(name, passport_number)
        self.passengers[passport_number] = passenger
        print(f"[INFO] Passenger {name} registered.")

    def assign_crew_member(self, name, role, flight_number):
        crew_member = CrewMember(name, role)
        if flight_number in self.flights:
            self.flights[flight_number].assign_crew(crew_member)
            self.crew_members.append(crew_member)
            print(f"[INFO] Crew member {name} assigned to flight {flight_number}.")
        else:
            print(f"[ERROR] Flight {flight_number} not found.")

    def book_flight(self, passport_number, flight_number):
        if passport_number not in self.passengers:
            print("[ERROR] Passenger not found.")
            return
        if flight_number not in self.flights:
            print("[ERROR] Flight not found.")
            return

        try:
            flight = self.flights[flight_number]
            passenger = self.passengers[passport_number]
            flight.book_seat(passenger)
            print(f"[INFO] Booking successful for {passenger.name} on flight {flight.flight_number}.")
        except Exception as e:
            print(f"[ERROR] {str(e)}")

    def flight_summary(self, flight_number):
        if flight_number not in self.flights:
            print("[ERROR] Flight not found.")
            return

        flight = self.flights[flight_number]
        print(f"\n[SUMMARY] Flight {flight.flight_number} from {flight.origin} to {flight.destination}")
        print(f"Departure: {flight.departure_time} | Arrival: {flight.arrival_time}")
        print("Crew Members:")
        for c in flight.crew:
            print(f" - {c.name} ({c.role})")
        print("Booked Passengers:")
        for entry in flight.passengers:
            print(f" - {entry['passenger'].name} (Seat {entry['seat_number']})")


if __name__ == "__main__":
    manager = AirlineSystem()
    manager.add_flight("AI101", "New York", "London", datetime(2025, 5, 1, 18, 0), 420, "Boeing 777")
    manager.register_passenger("Alice Johnson", "P1234567")
    manager.register_passenger("Bob Lee", "P2345678")
    manager.assign_crew_member("Captain Morgan", "Pilot", "AI101")
    manager.assign_crew_member("Dana Scott", "Flight Attendant", "AI101")
    manager.book_flight("P1234567", "AI101")
    manager.book_flight("P2345678", "AI101")
    manager.flight_summary("AI101")
