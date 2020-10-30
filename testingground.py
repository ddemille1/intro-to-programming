from PIL import Image
#open, import info, name variables from cactus picture
cactus_original = Image.open('cactus.jpg')
width_cactus, height_cactus = cactus_original.size
pixels_cactus_original = cactus_original.load()

#open, import infor, name variables from beach picture 
beach_original = Image.open('beach.jpg')
width_beach, height_beach = beach_original.size
pixels_beach_original = beach_original.load()

#r, g, b = pixels_cactus_original[x, y]
for y in range(0, height_cactus):
    for x in range (0, width_cactus):
      (rc, gc, bc) = pixels_cactus_original[x, y]
      (rb, gb, bb) = pixels_beach_original[x, y]
      if rc >= 0 and rc <=156 and gc >= 154 and gc <= 255  and bc >= 0 and bc <=104:
        pixels_cactus_original[x, y] = (rb, gb, bb)
      else:
        pixels_cactus_original[x, y] = (rc, gc, bc)

cactus_original.show()


#color to block out (76, 244, 24)
#range of (0, 154, 0) and (156, 255, 104) works really well
size  = int(input('How many columns and rows do you want in your multiplication table? '))
#range = range(1, size + 1)
#for x in range:
#    print (x, end=' ')
biggest_number = (size ** 2)
print(biggest_number)
import math
digit_count = int(math.log10(biggest_number)) + 1
print(digit_count)

for row in range(1, size +1):
    for column in range(1, size +1):
        number = row * column
        print(f'{number:{digit_count}}', end=' ')
    print()
