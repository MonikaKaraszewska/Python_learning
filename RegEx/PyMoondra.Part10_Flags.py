import re
string = '''In earlier examples, we used the search method. It will return only the first match for each group. But what if a string contains the multiple occurrences of a regex group and you want to extract all matches.

In this section, we will search Method learn how to capture all matches to a regex group. \nmethod To capture all Search Method matches to a regex group we need to use the finditer() method.

The finditer() method finds all matches and returns an iterator yielding match objects matching the regex pattern. Next, we can iterate each Match object and extract its value.

Note: Don’t use the findall() method because it returns a list, Search method the group() method cannot be applied. If you try to apply it to the findall method, you will get AttributeError: ‘list’ object has no attribute ‘groups.’

So always use finditer if you wanted to capture all matches to the group.'''

print(re.search(r'^method\.?',string)) #^to działa jak match, czyli jak poczatek sie zgadza to bedzie ok
print(re.search(r'group\.?$',string))

print('')
print(".......................flaga1.......re.MULTILINE / re.M......search")
#re.MULTILINE dziala tylko z re.search
#re.MULTILINE spradza poczatki kazdejlini i wysiwetla pierwsza znaleziona
print("flagaRe.M: ",re.search(r'^method\.?',string, flags=re.MULTILINE))

print('')
print(".......................flaga2.......re.IGNORECASE / re.I......findall..")
#szuka i z malai wielka litera
print("flaga2Re.I: ",re.findall(r'search method',string, flags=re.IGNORECASE))

print('')
print(".......................flaga3.......re.DOTALL/re.S........match.")
#re.DOTALL
print("flaga3: ",re.match('.*',string).group()) # normalnie wyswietli do momentu az zaczyna sie nowa linia
print("flaga3Re.S: ",re.match('.*',string, flags=re.DOTALL).group()) # wyswietla wszytsko




