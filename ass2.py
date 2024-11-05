import cv2

def process(ch):
    
    img=cv2.imread("C:/Users/diksh/Downloads/sakshi.jpg")

    if ch=="line":
        Start_point=(50,50)
        end_point=(300,300)
        color=(255,0,0)
        thickness=2
        cv2.line(img,Start_point,end_point,color,thickness)
        cv2.imshow("line",img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    if ch=="rectangle":
        top_left=(100,100)
        bottom_right=(400,300)
        color=(227,0,0)
        thickness=2
        cv2.rectangle(img,top_left,bottom_right,color,thickness)
        cv2.imshow("line",img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    if ch=="circle":
        center=(50,50)
        radius=50
        color=(217,0,0)
        thickness=-1
        cv2.circle(img,center,radius,color,thickness)
        cv2.imshow("circle",img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    if ch=="ellipse":
        center=(300,300)
        axes=(100,50)
        angle=30
        start_angle=0
        end_angle=360
        color=(255,255,0)
        thickness=2
        cv2.ellipse(img,center,axes,angle,start_angle,end_angle,color,thickness)
        cv2.imshow("ellipse",img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        
while True:
    print("enter choce `line, circle,rectangle,ellipse")
    print("Enter 'exit' to quit the program.")
    ch = input("Enter your choice: ").strip().lower()
    
    if ch=="exit":
        print("exit code successfully")
        break
    
    process(ch)       

