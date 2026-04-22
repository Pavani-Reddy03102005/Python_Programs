a="Pavani"
vowels=0
count=0
for ch in a:
    if ch in "aeiouAEIOU":
        vowels+=1
    else:
        count+=1
print("vowels:",vowels)
print("constants:",count)
