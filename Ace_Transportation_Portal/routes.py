# routes.py

route_1_stops = [
    "College Gate",
    "RTC Cross",
    "Miyapur",
    "KPHB",
    "Kukatpally"
]

stop_coordinates = (
    (17.4939, 78.3996),
    (17.4850, 78.3910),
    (17.4965, 78.3559),
    (17.4947, 78.3916),
    (17.4836, 78.4081)
)

registered_pass_ids = {
    "ACE001",
    "ACE002",
    "ACE003"
}

bus_fleet = {
    "bus_no": "TG09Z1234",
    "capacity": 50,
    "driver": "Mr. Kumar",
    "route": "Route 1"
}


def display_route_stops(route_stops):

    print("\nRoute Stops")
    print("-" * 30)

    for index, stop in enumerate(route_stops, start=1):
        print(f"{index}. {stop}")


def add_stop(route_stops, new_stop):

    if new_stop in route_stops:
        print("Stop already exists.")
    else:
        route_stops.append(new_stop)
        print("Stop added successfully.")


def register_student_pass(pass_set, student_id):

    if student_id in pass_set:
        print("Student Pass already registered.")
    else:
        pass_set.add(student_id)
        print("Student Pass registered successfully.")


def display_bus_details(bus_dict):

    print("\nBus Details")
    print("-" * 30)

    for key, value in bus_dict.items():
        print(f"{key} : {value}")