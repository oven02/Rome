from venice import V5Motor, Gearset, Direction
#import rome.odom

def main():
    vert_mL = V5Motor(
        1,
        Direction.FORWARD,
        Gearset.GREEN
    )
    vert_mR = V5Motor(
        2,
        Direction.FORWARD,
        Gearset.GREEN
    )
    #tracking = rome.odom.Tracking(0, 0, 0, 0)

    while True:
        pass
        #tracking.Update(vert_mL, vert_mR, 4.0, 1.0)
        #print(tracking)


if __name__ == "__main__":
    main()
