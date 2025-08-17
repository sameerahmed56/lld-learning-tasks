from abc import ABC, abstractmethod
import time

#  ------ VEHICLE ------


class Vehicle(ABC):

    @abstractmethod
    def hourly_price(self):
        pass

    @abstractmethod
    def daily_price(self):
        pass


class CarVehicle(Vehicle):

    def hourly_price(self):
        return 5

    def daily_price(self):
        return 100


class TruckVehicle(Vehicle):

    def hourly_price(self):
        return 10

    def daily_price(self):
        return 200


# -------- PARKING SPOT --------

class ParkingSpot(ABC):

    def __init__(self, spot_id: int):
        self.spot_id = spot_id
        self.is_occupied = False
        self.vehicle = None

    @abstractmethod
    def can_park(self, vehicle: Vehicle) -> bool:
        pass

    def park(self, vehicle: Vehicle):
        self.vehicle = vehicle
        self.is_occupied = True

    def vacate(self):
        self.vehicle = None
        self.is_occupied = False


class CarParkingSpot(ParkingSpot):

    def can_park(self, vehicle: Vehicle) -> bool:
        return isinstance(vehicle, CarVehicle)


class TruckParkingSpot(ParkingSpot):

    def can_park(self, vehicle: Vehicle) -> bool:
        return isinstance(vehicle, TruckVehicle)

# ---------- Ticket -----------


class Ticket:
    def __init__(self, ticket_id: int, vehicle: Vehicle, spot: ParkingSpot):
        self.ticket_id = ticket_id
        self.vehicle = vehicle
        self.spot = spot
        self.entry_time = time.time()

# ---------- ParkingPricingStrategy -------------


class ParkingPricingStrategy(ABC):

    @abstractmethod
    def calculate_cost(self, ticket: Ticket):
        pass


class HourlyParkingPricingStrategy(ParkingPricingStrategy):

    def calculate_cost(self, ticket: Ticket):
        duration_seconds = time.time() - ticket.entry_time
        duration_hours = (duration_seconds / 3600) + 1
        print(
            f'Pricing calculated as {duration_hours * ticket.vehicle.hourly_price():.2f} for {duration_hours:.2f} hours')
        return duration_hours * ticket.vehicle.hourly_price()


class DailyParkingPricingStrategy(ParkingPricingStrategy):

    def calculate_cost(self, ticket: Ticket):
        duration_seconds = time.time() - ticket.entry_time
        duration_days = (duration_seconds / (60*60*24)) + 1
        print(f'Pricing calculated as {duration_days * ticket.vehicle.daily_price():.2f} for {duration_days:.2f} days')
        return duration_days * ticket.vehicle.daily_price()


# ------------ Parking Lot ------------

class ParkingLot:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ParkingLot, cls).__new__(cls)
        return cls._instance

    def __init__(self, pricing_strategy: ParkingPricingStrategy):
        self.spots = [CarParkingSpot(i) for i in range(1, 8)] + [TruckParkingSpot(i) for i in range(8, 11)]
        self.tickets = {}
        self.ticket_counter = 0
        self.pricing_strategy = pricing_strategy

    def find_spot(self, vehicle: Vehicle) -> ParkingSpot | None:
        for spot in self.spots:
            if not spot.is_occupied and spot.can_park(vehicle):
                return spot
        return None

    def park_vehicle(self, vehicle: Vehicle) -> Ticket | None:
        spot = self.find_spot(vehicle)
        if not spot:
            print("Sorry, no spots available for this vehicle type.")
            return None

        spot.park(vehicle)
        self.ticket_counter += 1
        ticket = Ticket(self.ticket_counter, vehicle, spot)
        self.tickets[ticket.ticket_id] = ticket
        print(f"Vehicle parked in spot {spot.spot_id}. Ticket ID: {ticket.ticket_id}")
        return ticket

    def exit_vehicle(self, ticket_id: int) -> float:
        if ticket_id not in self.tickets:
            raise ValueError("Invalid ticket ID.")

        ticket = self.tickets[ticket_id]
        cost = self.pricing_strategy.calculate_cost(ticket)

        ticket.spot.vacate()
        del self.tickets[ticket_id]

        print(f"Vehicle from spot {ticket.spot.spot_id} exited. Cost: ${cost:.2f}")
        return cost


hourly_strategy = HourlyParkingPricingStrategy()
parking_lot = ParkingLot(pricing_strategy=hourly_strategy)
my_car = CarVehicle()
my_truck = TruckVehicle()
car_ticket = parking_lot.park_vehicle(my_car)
truck_ticket = parking_lot.park_vehicle(my_truck)
print("\n... vehicles parked for a while ...\n")
time.sleep(2)
if car_ticket:
    parking_lot.exit_vehicle(car_ticket.ticket_id)
if truck_ticket:
    parking_lot.exit_vehicle(truck_ticket.ticket_id)
