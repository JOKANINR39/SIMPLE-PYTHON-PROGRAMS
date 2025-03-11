# Tuple storing multiple flight details (Flight Number, Destination, Price)
flights = (
("AI202", "New York", 500),
("BA305", "London", 650),
("EK501", "Dubai", 400),
("SQ318", "Singapore", 550)
)
# Display available flights
print("Available Flights:")
for flight in flights:
print(f"Flight Number: {flight[0]}, Destination: {flight[1]}, Price: ${flight[2]}")
# Simulating a ticket booking (choosing the first flight)
selected_flight = flights[0]
# Booking confirmation
print("\nFlight Ticket Booked!")
print("Flight Number:", selected_flight[0])
print("Destination:", selected_flight[1])
print("Price: $", selected_flight[2])
=======================================