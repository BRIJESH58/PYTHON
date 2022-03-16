class PARROT:
    def FLY(self):
        print("PARROT CAN FLY")

    def SWIM(self):
        print("PARROT CAN'T SWIM")

class PENGUIN:
    def FLY(self):
        print("PENGUIN CAN'T FLY")

    def SWIM(self):
        print(("PENGUIN CAN SWIM"))

def FLYING_TEST(BIRD):
    BIRD.FLY()

BLU = PARROT()
PEGGY = PENGUIN()

FLYING_TEST(BLU)
FLYING_TEST(PEGGY)