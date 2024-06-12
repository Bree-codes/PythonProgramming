import re

pattern = "[A-Za-z]{1}[\d]{3}-[\d]{2}-[\d]{4}/[\d]{4}"

text1 = "brenda mukami C026-01-0921/2022 is a student in kimathi.Random reg C026-01-0931/2022"

ans = re.findall(pattern, text1)

print(ans)