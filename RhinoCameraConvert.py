import Rhino
import math


yUp = True  # convert current Z-up space to Y-up space
digit = 3  # how many digits to round to

vp = Rhino.RhinoDoc.ActiveDoc.Views.ActiveView.ActiveViewport

print vp.Name
rhLensLength = vp.Camera35mmLensLength
rhCamDir = -vp.CameraZ
rhCamLocation = vp.CameraLocation

if yUp:
    newCamLocation = [rhCamLocation[0], rhCamLocation[2], -rhCamLocation[1]]
    newCamDir = [rhCamDir[0], rhCamDir[2], -rhCamDir[1]]
else:
    newCamLocation = rhCamLocation
    newCamDir = rhCamDir


# calculate rotation
newCamRotation = [0,0,0]
## find rotation Y
if newCamDir[2] != 0:
    newCamRotation[1] = math.degrees(math.atan(newCamDir[0]/newCamDir[2]))
## find rotation Z
# find length of projection on XZ plane
projectXZ = (newCamDir[0]**2 + newCamDir[2]**2)**(1/2)  
newCamRotation[2] = math.degrees(math.atan(newCamDir[1]/projectXZ))


# output
print 'newCamLocation = ',
print round(newCamLocation[0],digit),
print ',',
print round(newCamLocation[1],digit),
print ',',
print round(newCamLocation[2],digit)

print 'newCamRotation = ',
print round(newCamRotation[0],digit),
print ',',
print round(newCamRotation[1],digit),
print ',',
print round(newCamRotation[2],digit)

print ('newCamLensLength = ' + str(rhLensLength) )
print ('newCamFOV = 35 mm')