#acronyms = ["LOL", "IDK", "TBH"]
#translation = ["laugh out loud","I don't know","to be honest"]

acronyms = {
    "LOL": "laugh out loud",
    "IDK": "I don't know",
    "TBH": "to be honest"
}
defintion = acronyms.get('BTW')
if defintion:
    print(defintion)
else:
    print("Not found")

sentence = 'IDK' +' what happened ' +'TBH'
translation = acronyms.get('IDK') + ' what happened ' + acronyms.get('TBH')
print('sentence:', sentence)
print('translation:', translation)