def decode_ways(digits: str) -> int:
    # WRITE YOUR BRILLIANT CODE HERE

    sum = [0]
    def dfs(digits: str, start_idx: int):
        if start_idx == len(digits):
            sum[0] += 1
            return
        
        if start_idx > len(digits):
            return
        
        for i in range (len(digits)):
            
            x = digits[start_idx:(start_idx + i + 1)]

            if int(x) > 26:
                continue

            dfs(digits, (start_idx + i + 1))
                
        return
        
    dfs(digits, 0)
    return sum[0]

res = decode_ways("1234")
print(res)