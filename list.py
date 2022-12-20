acronyms = ["LOL", "IDK", "SMH", "TBH"]
word = 'BFN'
if word in acronyms:
    print('Found')
else:
    print(word + ' not found')

acronyms.append(word)
acronyms.append("IMHO")

print(acronyms)
acronyms.remove("IMHO")
print(acronyms)

if word in acronyms:
    print('Found')
else:
    print(word + ' not found')

for acronym in acronyms:
    print(acronym)
