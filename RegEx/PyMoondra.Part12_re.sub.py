import re

tekst = r'''After World War II, the United States entered the Cold War, where geopolitical tensions between the U.S. 
and the Soviet Union led the two countries to dominate world affairs.[134] The US engaged in regime change against 
governments perceived to be aligned with the Soviet Union, and competed in the Space Race, culminating in the first 
crewed Moon landing in 1969.[135][136][137][138] Domestically, the U.S. experienced economic growth, urbanization, and 
population growth following World War II.[139] The civil rights movement emerged, with Martin Luther King Jr. becoming 
a prominent leader in the early 1960s.[140] The counterculture movement in the U.S. brought significant social changes,
including the liberalization of attitudes towards recreational drug use and sexuality[141][142] as well as open 
defiance of the military draft and opposition to intervention in Vietnam.[143] The late 1980s and early 1990s saw 
the collapse of the Warsaw Pact and the dissolution of the Soviet Union, which marked the end of the Cold War and 
solidified the USA as the world's sole superpower.[144][145][146][147] In the early 21st century, the September 11 
attacks in 2001 led to the war on terror and military interventions in Afghanistan and Iraq.[148][149] The U.S. 
housing bubble in 2006 culminated in the 2007–2008 financial crisis and the Great Recession, the largest economic 
contraction since the Great Depression.[150] Starting in the 2010s, political polarization increased as sociopolitical 
debates on cultural issues dominated political discussion'''


tekst2 = re.sub(r'\[\d+\]','',tekst)
print(tekst2)
print(' ')
print("UStekst: ",re.sub('U.S.|US|USA', 'United States',tekst2))
print(' ')
print("..............................................................lambda..........functions with re.sub............")

string = "Dan has 3 snails. Mike has 4 cats. Alias has 9 monkeys."
print("string: ",(re.search(r'(\d+)',string).group()))

print("string2: ",re.findall(r'(\d+)',string))
import math
print("Substring3: ",re.sub(r'(\d+)','1', string))
print("Lambdastring5: ",re.sub(r'(\d+)', lambda x: str(x), string))
print("Lambdastring6: ",(re.sub('(\d+)', lambda x: (x.group(0)), string)))
print("Lambdastring4: ",(re.sub('(\d+)', lambda x: str(int(x.group(0))*int(x.group(0))), string)))

print('')

inpot = 'eat laugh sleep study'
verbs = re.findall(r'\w+',inpot)
print(verbs)

result = re.sub(r'\w+',lambda x: x.group() + "ing",inpot)
print(result)

print('')

print(".................................................backreferencing with re.sub............")

string3 = 'Merry Merry Christmas'
print(re.search(r'(\w+ )(\1)',string3).groups())
print(re.search(r'(\w+ )(\1)',string3).group(1,2))

print(re.sub(r'(\w+ )(\1)', r'Happy \1', string3))

print(re.sub(r'(\w+ )(\1)', r'\1 Happy ', string3))

print(re.sub(r'(\w+ )(\1)', r'Happy \2', string3))