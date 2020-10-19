from PIL import Image, ImageOps  
      
# creating a image1 object  
orginal = Image.open(r"C:\Users\Belgin\Desktop\github.png")  
      
# applying expand method 
# using border value = 20 
# using fill = 50 which is brown type color 

expanded_image = ImageOps.expand(orginal, border = 20, fill = 50)  
  
expanded_image.show() 
