i = 0
while i < 5:
    i += 1
    print(i)

print("01: koniec")


i = 0
while True:
    print(i)
    i += 1
    if i>=5:
        break
print("02: koniec")

i = 0
while True:
    i += 1
    if i % 2 == 1:
        continue # jesli warunek jest spelniony to nie idzie dalej, tylko wraca do poczatku petli,
        # continue znaczy nie wykonuj dalej tylko kontynuuj od poczatku petli
    print(i) # idlatego drukuje parzyste,bo jak jest nieparzysta ma kontynuowac petle od poczatku a nie wykonywac kod dalej
    if (i > 10):
        break
print("03: koniec")


i = 0
while i < 9:
  i += 1
  print(i)
  if i == 3:
    continue
  print(i)


print('video 3 Python Tutorials ..................PyMoodra')

#pass do nothing go forward
for i in range(100):
    print(i)
    if i>5:
        pass # tznaczy nie rob nic i przejdzdo kolejnej linijkikodu, dlatego wysiwetla 'please come here'
            #continue mowi idz do poczatku
    else:
        print("Hello")
    print("please come here")
