import unittest

Right = 'Right'
Left = 'Left'


def calculate_direction(angles):
    return Right if sum(angles) > 0 else Left

    # total = 0
    #
    #
    # # for angle in angles:
    # #     total += angle
    #
    # while angles:
    #     total += angles[0]
    #     angles = angles[1:]
    #
    # if total > 0:
    #     return Right
    # else:
    #     return Left


class BoatTestCase(unittest.TestCase):

    def test_givenOnePositiveAngle_retunrnsRight(self):
        givenAngles= [1]
        direction = calculate_direction(givenAngles)
        self.assertEquals(direction, Right)

    def test_givenNothing_returnLeft(self):
        givenAngles = []
        direction = calculate_direction(givenAngles)
        self.assertEquals(direction, Left)


    def test_givenOneNegativeAngle_returnLeft(self):
        givenAngles = [-1]
        direction = calculate_direction(givenAngles)
        self.assertEquals(direction, Left)


    def test_givenTwoAnglesWithTotalPositive_returnRight(self):
        givenAngles = [-1, 2]
        direction = calculate_direction(givenAngles)
        self.assertEquals(direction, Right)


    def test_givenTwoAnglesWithTotalNegative_returnLeft(self):
        givenAngles = [-2, 1]
        direction = calculate_direction(givenAngles)
        self.assertEquals(direction, Left)

if __name__ == '__main__':
        unittest.main()
