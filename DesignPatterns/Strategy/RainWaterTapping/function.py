from abc import ABC, abstractmethod

class RainWaterTappingInterface(ABC):

    @abstractmethod
    def calculate_rain_water(self, arr) -> int:
        pass

    @abstractmethod
    def get_info(self) -> str:
        pass

class RainWaterTappingAlgorithm1(RainWaterTappingInterface):

    def calculate_rain_water(self, arr) -> int:
        result = 0
        n = len(arr)
        for i in range(1, n-1):
            left = arr[i]

            for j in range(i):
                left = max(left, arr[j])
            
            right = arr[i]

            for j in range(i+1, n):
                right = max(right, arr[j])

            #print(left, right, arr[i],result)
            result += max((min(left, right) - arr[i]),0)
        
        return result

    def get_info(self) -> str:
        return "This is the Algorithm 1. Time Conplexity : O(N2) and Space Conplexity : O(1)."

class RainWaterTappingAlgorithm2(RainWaterTappingInterface):

    def calculate_rain_water(self, arr) -> int:
        result = 0
        n = len(arr)
        left = [0] * n
        left[0] = arr[0]

        for i in range(1, n):
            left[i] = max(left[i-1], arr[i])
        

        right = arr[n-1]
        #print(left)
        for i in range(n-2,-1,-1):
            right = max(right, arr[i])

            result += max((min(right, left[i]) - arr[i]), 0)


        return result
    
    def get_info(self) -> str:
        return "This is the Algorithm 2. Time Conplexity : O(N) and Space Conplexity : O(N)."

class RainWaterTappingAlgorithm3(RainWaterTappingInterface):

    def calculate_rain_water(self, arr) -> int:
        n = len(arr)

        left = 0
        right = n-1

        l_max = 0
        r_max = 0

        result = 0

        while left <= right:

            if r_max <= l_max:

                result += max(0, r_max - arr[right])
                r_max = max(r_max, arr[right])
                right -= 1
            else:
                result += max(0, l_max - arr[left])
                l_max = max(l_max, arr[left])
                left += 1
        
        return result


    def get_info(self) -> str:
        return "This is the Algorithm 3. Time Conplexity : O(N) and Space Conplexity : O(1)."   