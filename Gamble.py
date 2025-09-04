import random 

reels = [[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9]]

def spin():
 spinResult = ''
 for reel in reels:
  spinResult += str(random.choice(reel))
 return spinResult
print (spin())

counter = 0
for i in range (1000):
 currSpin = spin()
 if currSpin == '777':
   counter += 1 

   print(f"det var en total av {counter} jackpots truffet")

   #enkel guide lærte av Not a Software Engineer link:https://youtu.be/hnTrectlTxM?si=IAhNvk5-a1IsWj4b