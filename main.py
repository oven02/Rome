from venice import Motor, Gearset, Direction

def main():
    my_motor = Motor(
        1,
        Direction.FORWARD,
        Gearset.GREEN
    )
    my_motor.set_voltage(10.0)


if __name__ == "__main__":
    main()
