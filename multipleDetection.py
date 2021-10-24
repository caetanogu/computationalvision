'''
This program purpose is to find templates on the given image and use it to draw rectangles, circles or marks
on the object wanted to find. The user must input the name and the extension of the image and the template desired
plus the threshold that match better and the mode (rectangles, markers or circles). Note that the image must be on the same directory as the program
'''
#Libraries imports
import cv2 as cv
import numpy as np

def findObjects(image, template, threshold, mode):

    #Load the base image and the template
    img = cv.imread(image, cv.IMREAD_UNCHANGED)
    templ = cv.imread(template, cv.IMREAD_UNCHANGED)

    #List all the methods possible
    methods = [cv.TM_CCOEFF, cv.TM_CCOEFF_NORMED, cv.TM_CCORR, 
                cv.TM_CCORR_NORMED, cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]

    #Matches the template in the image given
    result = cv.matchTemplate(img, templ, methods[1])

    #Set the threshold of the match
    thr = threshold

    #This takes the position where the template match and zip this positions into tuples
    locations = np.where(result >= thr)
    locations = list(zip(*locations[::-1]))

    if locations:
        print('Template found')

        #Takes the width and the height of the template given
        width = templ.shape[1]
        height = templ.shape[0]

        #Creates a list of rectangles with their (x, y, w, h) coordinates
        rectangles = []

        #This loops around all the rectangles that must be draw
        for loc in locations:
            
            #This create one rectangle with (x, y, w, h) for each loop
            rect = (int(loc[0]), int(loc[1]), width, height)

            #Then it adds the rectangle twice to always have more than 1 rectangle in the same location to group
            rectangles.append(rect)
            rectangles.append(rect)
        
        rectList, weights = cv.groupRectangles(rectangles, groupThreshold=1, eps=0.5)

        points = []

        #Loop to draw all the rectangles
        for (x, y, w, h) in rectList:

            # Determine the center position
            center_x = x + int(w/2)
            center_y = y + int(h/2)
            
            # Save the points
            points.append((center_x, center_y))

            if mode == 'Rectangles':

                #Determine the box position
                top_left = (x, y)
                bottom_right = (x + w, y + h)

                #Draw the rectangles
                cv.rectangle(img, top_left, bottom_right, color=(0, 0, 255))

            elif mode == 'Markers':
                
                #Draw the center point
                cv.drawMarker(img, (center_x, center_y), color=(0, 0, 255), markerType=cv.MARKER_CROSS)

            elif mode == 'Circles':

                #Draw the circle
                cv.circle(img, (center_x, center_y), radius=10, color=(0, 0, 255))

            else:
                #If the mode is not recognized pass
                pass

        #show the image with the markers in the detected objects
        cv.imshow('Display', img)
        cv.waitKey()

    else:
        print('Image not found')

#Principal routine
print('Welcome to the multiple detection program, this is my first project so sorry if you experience some problems along the way')
image = input("Insert the image and the extension name (ex: Mario.jpg): ")
template = input('Then, insert the template and the extension name (ex: Marioface.jpg): ')
mode = input('Then choose the marker mode (Rectangles, Circles or Markers): ')
findObjects(image, template, 0.715, mode)
