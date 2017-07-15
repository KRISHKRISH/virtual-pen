# this function takes the average of the background which can be further used to subtract out the background
def background(cam):
  bck_gnd = np.zeros((480,640,3), np.float32)*0
  for i in range(0,100):
    ret_val, img = cam.read()
    #print np.amax(img)
    bck_gnd=bck_gnd+img;
  bck_gnd=bck_gnd/100;
  bck_gnd=bck_gnd.astype(np.uint8) 
  return(bck_gnd)

# this function is used for caliberation
# Note : 4 points are required for caliberation 
# place the pen at the 4 corner of your screen (in clockwise order) and the press backspace 
# the function saves the pixel locations of these points and use it to calicate the homographic transformation
def caliberate(cam,bck_gnd):
  src=[];
  dst=[[0,0],[640,0],[640,480],[0,480]];
  while True :
    ret_val, img = cam.read()
    img=cv2.absdiff(img,bck_gnd)
    mask = cv2.inRange(img, lower, upper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    cv2.imshow('my webcam', mask)
    if cv2.waitKey(1) == 8:
      M = cv2.moments(mask)
      if(M["m10"]>0):
        print len(src)+1
        center = [int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"])]
        src.append(center)
        if(len(src)==4):
          break;
    if cv2.waitKey(1) == 27:
    		break;
  src=np.float32(src);
  dst=np.float32(dst);
  m = cv2.getPerspectiveTransform(src, dst)
  cv2.destroyAllWindows()   
  return(m)
def track(p1,p2,image,cam,bck_gnd):
  ret_val, img = cam.read()
  img=cv2.absdiff(img,bck_gnd)
  mask = cv2.inRange(img, lower, upper)
  mask = cv2.erode(mask, None, iterations=2)
  mask = cv2.dilate(mask, None, iterations=2)
  cv2.imshow('tracking', mask)
  cv2.imshow('display',image)
  if cv2.waitKey(1) == 27: 
     print "exiting......"
     exit();
  M = cv2.moments(mask)
  if M["m00"]>0 :
     center = [int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"])]
     p2=p1;
     p1 = np.array([center], dtype=np.float32)
     result = cv2.perspectiveTransform(p1[None,:], m)
     p1=result[0][0]
     if not all(tuple(p2)):
      return(p1,p2,image)
     print tuple(p1)
     print tuple(p2)
     cv2.line(image,tuple(p2), tuple(p1), (0, 0, 255),2)
  else :
     p1=np.array([None,None,None]);
     p2=np.array([None,None,None]);
  return(p1,p2,image)



# main
import cv2
import numpy as np
cam = cv2.VideoCapture(0)
lower = np.array([2,2,2])
upper = np.array([255,255,255])
image = np.ones((480,640,3), np.uint8)
image = image*255
p1=np.array([None,None,None]);
p2=np.array([None,None,None]);
#background 
print "background"
bck_gnd=background(cam);
#claiberation
print "caliberating"
m=caliberate(cam,bck_gnd);
print "tarcking"
while True :
  p1,p2,image=track(p1,p2,image,cam,bck_gnd);
cv2.destroyAllWindows()
