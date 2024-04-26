# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Input: strs = [""]
# Output: [[""]]

strs = ["eat","tea","tan","ate","nat","bat"]

#we take a hasmap where keys can be the letters in sorted string

#initialize an empty dictionary
groups = {}

#iterate through each string in strs

for i in strs:
    #sort every string 

    sorted_string = ''.join(sorted(i))
    #sorted_string = ate & i = eat
    if sorted_string in groups:
        groups[sorted_string].append(i)


    # If not, create a new entry with the sorted form as the key
    else:
        groups[sorted_string]=[i]

# Convert the dictionary values to a list
print(list(groups.values()))



