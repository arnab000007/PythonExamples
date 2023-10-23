from AlgoFactory import AlgoFactory
from function import RainWaterTappingInterface
from enums import TimeComplexity, SpaceComplexity

def main():

    arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

    algo:RainWaterTappingInterface = AlgoFactory.get_Algorithm(TimeComplexity.O_N, SpaceComplexity.O_N)
    print(algo.get_info())
    ans = algo.calculate_rain_water(arr)
    print('The rain water tapped with the array is : {}'.format(ans))

if __name__ == '__main__':
    main()