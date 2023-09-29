distance_km = int(input())
day_or_night = str(input())

transport_price = 0
transport_price_taxi_day = 0.7 + 0.79 * distance_km
transport_price_taxi_night = 0.7 + 0.9 * distance_km
transport_price_bus = 0.09 * distance_km
transport_price_train = 0.06 * distance_km

if day_or_night == "day":

    if distance_km < 20:
        transport_price = transport_price_taxi_day

    elif 20 <= distance_km < 100:
        transport_price = min(transport_price_taxi_day, transport_price_bus)

    elif distance_km >= 100:
        transport_price = min(transport_price_taxi_day, transport_price_bus, transport_price_train)

elif day_or_night == "night":

    if distance_km < 20:
        transport_price = transport_price_taxi_night

    elif 20 <= distance_km < 100:
        transport_price = min(transport_price_taxi_night, transport_price_bus)

    elif distance_km >= 100:
        transport_price = min(transport_price_taxi_night, transport_price_bus, transport_price_train)


print(f"{transport_price:.2f}")