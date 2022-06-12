from typing import List

def letter_combinations_of_phone_number(digits: str) -> List[str]:
    # WRITE YOUR BRILLIANT CODE HERE
    possible_characters = mapper(digits)

    res = []

    def dfs(characters: List[str], path: List[str], 
    used: List[List[bool]], res: List[str], level: int):
        
        if len(path) == len(digits):
            res.append("".join(path))
            return
        
        for i, c in enumerate(characters[level]):
            
            if used[level][i]:
                continue

            used[level][i] = True
            path.append(c.lower())
            dfs(characters, path, used, res, level + 1)
            used[level][i] = False
            path.pop()
    
    used = []

    #initate used element
    # 2d array, where row is level
    # col is chars
    for i in range (len(digits)):
        used.append([False] * len(possible_characters[i]))
    
    dfs(possible_characters, [], used, res, 0)

    return res


def mapper(digits: str) -> List[str]:
    
    data = {}
    data['1'] = []
    data['2'] = ['A', 'B', 'C']
    data['3'] = ['D', 'E', 'F']
    data['4'] = ['G', 'H', 'I']
    data['5'] = ['J', 'K', 'L']
    data['6'] = ['M', 'N', 'O']
    data['7'] = ['P', 'Q', 'R', 'S']
    data['8'] = ['T', 'U', 'V']
    data['9'] = ['W', 'X', 'Y', 'Z']
    
    results = []
    for _, c in enumerate(digits):
        if len(data[c]) > 0:
            results.append(data[c])
    
    return results

# print(mapper("56"))

answers = letter_combinations_of_phone_number("56")
print(answers)