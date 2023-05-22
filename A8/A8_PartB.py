'''
Do some simple image processing
# Assignment written by: Sejin Yoon
'''

# This brings in functions from the graphics.py file
from graphics import *
# We will need some random numbers
from random import randrange

# This function makes a new image that has the red values of the original image but sets the
# green and blue parts to zero. A pure green or blue color in the original will look black
# in the new image since those colors get set to 0.
#
# Study the pattern of the loop inside a loop (called nested loops). Each time the first loop
# does a single repeat, the entire inner loop does all its repetitions.
#
# Look how to get the color at a pixel, change the color, and set the pixel to the new color.
# The assignment problems below will use these steps.
def red_part_of_an_image(image):
    red_image = image.clone()  # copy the image
    # go across the image with the for x loop and then move down a row
    for y in range(0, image.getHeight()):
        for x in range(0, image.getWidth()):
            color = image.getPixel(x, y)  # get the pixel color
            red_color = color[0]  # pull out the red component
            new_color = [red_color, 0, 0]  # Zero out the green and blue
            red_image.setPixel(x, y, new_color)  # Set the pixel to the new color
    return red_image  # return the finished new image

# Question 1, Make a function that sets every pixel of a new image to the average
# of the red, green, and blue parts of the pixel at the same location in the
# original. The average is summing them up and dividing by 3. This is one way
# to convert a color image to a grey (black-and-white) image.
# // means integer division, which produces an int for a result, like 5 // 2 is 2.
# Look at the above function for the basic structure you should follow.
def color_image_to_grey_scale(image):
    grey_image = image.clone()  # copy the image
    # go across the image with the for x loop and then move down a row
    for y in range(0, image.getHeight()):
        for x in range(0, image.getWidth()):
            color = image.getPixel(x, y)  # get the pixel color
            red_color = color[0]  # red component
            green_color = color[1]  # green component
            blue_color = color[2]  # blue component
            average_color = (red_color + green_color + blue_color) // 3  # calculate average
            new_color = [average_color, average_color, average_color]  # create new color
            grey_image.setPixel(x, y, new_color)  # set pixel to new color
    return grey_image  # return the finished new image

# Question 2, Make a function that makes a photonegative of the original.
# The red value should be set to 255 - original red, green to 255 - original green
# and the same for the blue value.
def photonegative_of_an_image(image):
    negative_image = image.clone()  # copy the image
    # go across the image with the for x loop and then move down a row
    for y in range(0, image.getHeight()):
        for x in range(0, image.getWidth()):
            color = image.getPixel(x, y)  # get the pixel color
            red_color = 255 - color[0]  # calculate negative red value
            green_color = 255 - color[1]  # calculate negative green value
            blue_color = 255 - color[2]  # calculate negative blue value
            new_color = [red_color, green_color, blue_color]  # create new color
            negative_image.setPixel(x, y, new_color)  # set pixel to new color
    return negative_image  # return the finished new image

# Question 3, Make a function that brightens the original. To do this, multiply each color
# value by 2. Some values * 2 will be larger than the allowed 0-255 range for a color.
# The graphics module sets all values bigger than 255 to 255.
def brighten_image(image):
    brightened_image = image.clone()  # copy the image
    # go across the image with the for x loop and then move down a row
    for y in range(0, image.getHeight()):
        for x in range(0, image.getWidth()):
            color = image.getPixel(x, y)  # get the pixel color
            red_color = min(color[0] * 2, 255)  # calculate brightened red value
            green_color = min(color[1] * 2, 255)  # calculate brightened green value
            blue_color = min(color[2] * 2, 255)  # calculate brightened blue value
            new_color = [red_color, green_color, blue_color]  # create new color
            brightened_image.setPixel(x, y, new_color)  # set pixel to new color
    return brightened_image  # return the finished new image

# Question 4, Make a function that randomly picks a pixel location, finds the color
# at that location, and draws a circle at that location filled with that color onto the
# window. The function should do this finding and drawing process 50000 times.
# This will cover the old image with an artistic style.
# You need to pick an x location from 0 to one less than the image width.
# You need a y location from 0 to one less than the image height.
# Research, using Google, the randrange function in Python and imported at the top of
# this file and use it to pick a random x and a random y location.
# Ask yourself, if you want to repeat the action 50000 times, what kind of loop structure do you need?
#
# An example of drawing a circle to image is
#
#         circle = Circle(Point(x, y), 5) # 5 makes a 5 pixel radius circle
#         circle.setFill(color)
#         circle.setWidth(0) # This gets rid of the circle border
#         circle.draw(win)
#
def color_image_to_pointillist(image, win):
    for _ in range(50000):  # repeat the process 50000 times
        x = randrange(image.getWidth())  # pick a random x location
        y = randrange(image.getHeight())  # pick a random y location
        color = image.getPixel(x, y)  # get the color at that location
        circle = Circle(Point(x, y), 5)  # create a circle
        circle.setFill(color)  # fill the circle with the color
        circle.setWidth(0)  # remove the circle border
        circle.draw(win)  # draw the circle on the window

# This function loads the image file and centers it in the window. The image is returned so
# it can be drawn.
def load_image(filename):
    # Load the image
    image = Image(Point(0,0), filename)
    # Center it
    image.move(int(image.getWidth()/2), int(image.getHeight()/2))
    return image

# This is where the program starts
def main():
    # Load the image first so we know how big to make the window.
    image = load_image("pepper.png")
    # Setup the window using the image size
    win = GraphWin('Image Art', image.getWidth(), image.getHeight(), autoflush=False)
    win.setBackground('yellow') # This is here to help see if the image is centered.

    # Draw the original image and wait for a mouse click to move to the next step
    image.draw(win)
    win.getMouse()

    # Compute the red portion of the image
    red_image = red_part_of_an_image(image)
    red_image.draw(win)
    win.getMouse()

    # Test Question1, by removing the comments from the next 3 lines
    grey = color_image_to_grey_scale(image)
    grey.draw(win)
    win.getMouse()

    # Test Question 2,  by removing the comments from the next 3 lines
    photonegative = photonegative_of_an_image(image)
    photonegative.draw(win)
    win.getMouse()

    # Test Question 3,  by removing the comments from the next 3 lines
    brightened_image = brighten_image(image)
    brightened_image.draw(win)
    win.getMouse()

    # Test Question 4, by removing the next 2 comments
    color_image_to_pointillist(image, win)
    win.getMouse()

    win.close()

# This is the only code that is not indented, so this is the first line executed.
main()