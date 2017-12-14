from SimpleCV import Camera 
from time import sleep 
print("setting GPIO") 
sw=21 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(sw,GPIO.IN) 
print("setting twitter interface") 
c_key="***************************" c_secret="*********************************" A_Token="********************************************" A_secret="**********************************************" api=Twython(c_key,c_secret,A_Token,A_secret) 
print("setting camera property") myCamera=Camera(prop_set={'Width':320,'height':240}) #frame=myCamera.getImage() 
#frame.save("img1.jpg") 
#sleep(3) 
#count=0 
while True:  
print("Checking Human")  
inputValue=GPIO.input(sw)  
if(inputValue==True):   
print("setting camera for image capture")     frame=myCamera.getImage()   
print("setting camera for image save")   
frame.save("img1.jpg")   
sleep(3)   
photo=open('img1.jpg', 'rb')   response=api.upload_media(media=photo)   
print("setting for twitter status")   
api.update_status(status='live pic',media_ids=[response['media_id']])  
sleep(1)  
