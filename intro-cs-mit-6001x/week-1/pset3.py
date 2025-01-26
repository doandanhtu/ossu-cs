s = 'gkzmyhjjvqzzsqdabfvav'

def get_longest_alpha_substr(s):
    substring = list()
    for j in range(0,len(s)):
        tmp_str = ''
        for char in s[j:len(s)]:
            if len(tmp_str) == 0:
                tmp_str += char
            elif char >= tmp_str[len(tmp_str)-1]:
                tmp_str += char
            elif char < tmp_str[len(tmp_str)-1]:
                break
        substring.append(tmp_str)

    longest_substring = substring[0]
    for string in substring:
        if len(string) > len(longest_substring):
            longest_substring = string
    
    return longest_substring

longest_substring = get_longest_alpha_substr(s)

print('Longest substring in alphabetical order is: ', longest_substring)

