s = 'azcbobobegghakl'
substring = list()
count = 0
while count < len(s) - 2:
    for i in range(count, len(s) - 1):
        if s[i + 1] < s[i]:
            substring.append(s[count:i+1])
            break
    count += 1

longest_substring = substring[0]
for string in substring:
    if len(string) > len(longest_substring):
        longest_substring = string

print('Longest substring in alphabetical order is: ', longest_substring)
