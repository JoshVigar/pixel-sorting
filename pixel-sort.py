import matplotlib.pyplot as plt
import numpy as np 

# setup
plt.axis('off')
img = plt.imread('foggy-trees.jpg')

# functions
def set_pixel(img_array, x, y, c):
    img_array[x,y,0]=c 
    img_array[x,y,1]=c
    img_array[x,y,2]=c

def set_pixels(img_array, x, y, c0, c1, c2):
    img_array[x,y,0]=c0
    img_array[x,y,1]=c1
    img_array[x,y,2]=c2

def pixel_brightness(img_array, x, y):
    return (int(img_array[x,y,0]) + int(img_array[x,y,1]) + int(img_array[x,y,2]))/3

def pixel_sort(img):
    img_array = np.asarray(img).copy()
    img_size = img_array.shape

    for y in range(img_size[1]):
        colour_stack = []
        positon_stack = []
        for x in range(img_size[0]):
            if pixel_brightness(img_array, x, y) > 200 or pixel_brightness(img_array, x, y) < 50:
                # set_pixel(img_array, x, y, 0)
                next
            else:
                #push position to stack
                positon_stack.append(x)
                #push pixel colour to array
                colour_stack.append(img_array[x, y, :])
        #when finished sort colour array and set pixel from the stack 
        sorted_colours = sorted(colour_stack, key=lambda x:int(x[0])+int(x[1])+int(x[2]))
        for s in range(len(positon_stack)):
            colours = sorted_colours.pop()
            position = positon_stack.pop()
            set_pixels(img_array, position, y, colours[0], colours[1], colours[2])
        

    return img_array

# processing
processed = pixel_sort(img)

# display
plt.imshow(processed)
plt.show()
