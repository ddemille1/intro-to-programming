from PIL import Image
beach_original = Image.open('beach.jpg')
beach_original.show()
width, height = beach_original.size
pixels_beach_original = beach_original.load()

for y in range(0, height):
    for x in range(0, width):
        (r, g, b) = pixels_beach_original[x, y]
        new_red = r + 100
        pixels_beach_original[x, y] = (new_red, g, b)
    
beach_original.show()
#beach_original.save('red_beach.jpg')


#to open the image in a new window
#image_original.show()

#find the size of image and store dimensions as variables width and height.
#width, height = image_original.size

#store the pixels of the image in a new vairable
#pixels_original = image_original.load()

#to access the rgb values at coordinate x, y, and store them as variables r, g, b.
#r, g, b = pixels_original[x, y]

#to see what the pixel value is:
#print(pixels_original[x, y])

#to see what the format of the image is
#print(image_beach.format)

#to set new rgb values for pixel at location x,y
#pixels_original[x, y] = (r, g, b)

#to save image to a new file
#image_original.save('the_file_goes_here.jpg')

