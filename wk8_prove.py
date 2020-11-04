from PIL import Image
#open, import info, name variables from cactus picture
cactus_original = Image.open('cactus.jpg')
width_cactus, height_cactus = cactus_original.size
pixels_cactus_original = cactus_original.load()

#open, import info, name variables from beach picture 
beach_original = Image.open('beach.jpg')
width_beach, height_beach = beach_original.size
pixels_beach_original = beach_original.load()

#creating new image same size as beach and cactus pictures which are both 800w x 600h
image_new = Image.new("RGB", cactus_original.size)
pixels_new = image_new.load()

#going through pixels of images, deciding which go into the new picture
#green pixels get set to pixels from beach bicture
#if not green, then they are pixels from the cactus picture
for y in range(0, height_cactus):
    for x in range (0, width_cactus):
      (rc, gc, bc) = pixels_cactus_original[x, y]
      (rb, gb, bb) = pixels_beach_original[x, y]
      if rc >= 0 and rc <=156 and gc >= 164 and gc <= 255  and bc >= 0 and bc <=104:
        pixels_new[x, y] = (rb, gb, bb)
      else:
        pixels_new[x, y] = (rc, gc, bc)

image_new.show()
image_new.save("the_new_image.jpg")

#color to block out (76, 244, 24)
#range of (0, 164, 0) and (156, 255, 104) works really well


#make it my own:

#open, import info, name variables from desert picture
desert_original = Image.open('desert.jpg')
width, height = desert_original.size
pixels_desert_original = desert_original.load()

#open, import info, name variables from sunset picture 
sunset_original = Image.open('sunset.jpg')
width, height = sunset_original.size
pixels_sunset_original = sunset_original.load()

#creating new image same size as sunset and desert pictures which are both 800w x 600h
image_blend = Image.new("RGB", desert_original.size)
pixels_blend = image_blend.load()

#combining the desert and sunset images
for y in range(0, height):
    for x in range (0, width):
      (rc, gc, bc) = pixels_desert_original[x, y]
      (rb, gb, bb) = pixels_sunset_original[x, y]
      r = int((rc + rb) / 2)
      g = int((gc + gb) / 2)
      b = int((bc + bb) / 2)
      pixels_blend[x, y] = (r, g, b)

#showing and saving the new blended picture
image_blend.show()
image_blend.save("the_blend_image.jpg")

