class Beacon:
    def __init__(self, position: tuple[int, int]) -> None:
        self.position = position

    def __repr__(self) -> str:
        return f'{self.position}'

class Sensor:
    def __init__(self, position: tuple[int, int], beacon: Beacon) -> None:
        self.position = position
        self.beacon = beacon
        self.distance_to_beacon = 0

    def calculate_manhattan_distance(self, coords: tuple[int,int]):
        return abs(self.position[0] - coords[0]) + abs(self.position[1] - coords[1])

    def __repr__(self) -> str:
        return f'Sensor {self.position} looking at Beacon {self.beacon} distance: {self.distance_to_beacon}'

def map_sensors(puzzle_input_file) -> list[Sensor]:
    sensors = []
    with open(puzzle_input_file) as file:
        lines = file.read().splitlines()
    for line in lines:
        things = line.split()
        sensor_position = (int(things[2][2: -1]), int(things[3][2: -1]))
        beacon_position = (int(things[8][2: -1]), int(things[9][2:]))
        sensor = Sensor(position=sensor_position, beacon=Beacon(position=beacon_position))
        sensor.distance_to_beacon = sensor.calculate_manhattan_distance(beacon_position)
        sensors.append(sensor)
    return sensors

def check_point(sensors: list[Sensor], point: tuple[int, int]):
    for sensor in sensors:
        difference = sensor.calculate_manhattan_distance(point) - sensor.distance_to_beacon
        if difference > 0: continue
        else:
            return point, abs(difference)
    return 0, abs(difference)

def loop_over_points(shape: tuple[int, int]):
    y_count = -1
    while y_count < shape[1] + 1:
        y_count += 1
        x_count = 0
        while x_count < shape[0] + 1:
            x_count += 1
            point = (x_count, y_count)
            cant_have_beacon_point, margin = check_point(sensors, point)
            if not cant_have_beacon_point: 
                print(f'beacon must be at {x_count, y_count}')
                return (x_count * 4_000_000) + y_count
            if margin > 0: x_count += margin -1
            # print(margin, found_point)

sensors = map_sensors('input15.txt')
for sensor in sensors: print(sensor)
frequency = loop_over_points(shape= (4_000_000, 4_000_000))
print(frequency)