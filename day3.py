  def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res =[]
        min_diff = abs(arr[0]-arr[1])
        for i in range(1,len(arr)):
            if abs(arr[i]-arr[i-1])<min_diff:
                min_diff=abs(arr[i]-arr[i-1])

        for i in range(1,len(arr)):
            if abs(arr[i]-arr[i-1])==min_diff:
                res.append([arr[i-1],arr[i]])
        return res
            
