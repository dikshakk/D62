import cv2



def process(ch):
    
    img=cv2.imread("C:/Users/diksh/Downloads/sakshi.jpg")
    
    if ch=="show":
        #img read 
        cv2.imshow("original img",img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
   
    elif ch=="crop":
        #crop img 
        crop_img=img[100:300, 150:400]
        cv2.imshow("crop_img",crop_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif ch=="resize":
        #resize
        resize_img=cv2.resize(img,(200,200))
        cv2.imshow("resize img",resize_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif ch=="threshold":
        #thresholding
        grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        #binary
        _,threshold_img=cv2.threshold(grey_img,127,255,cv2.THRESH_BINARY)

        cv2.imshow("img",threshold_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        
    elif ch=="contours":   

        #controing 

        gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        _,threshold_img=cv2.threshold(gray_img,127,255,cv2.THRESH_BINARY)

        coutours, herarchy=cv2.findContours(threshold_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        coutour_img=img.copy()
        cv2.drawContours(coutour_img,coutours,-1,(0,255,0),2)

        cv2.imshow("contour_img",coutour_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows() 

    elif ch=="blob": 
        #blob img

        gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        _,threshould_img=cv2.threshold(gray_img,127,255,cv2.THRESH_BINARY)

        params = cv2.SimpleBlobDetector_Params()

        detector=cv2.SimpleBlobDetector_create(params)

        keypoints=detector.detect(threshould_img)

        blob_img= cv2.drawKeypoints(img,keypoints,None,(0,0,255),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

        cv2.imshow("contour_img",blob_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows() 
        
    else:
        print("wrong choice")
        
while True:
    print("\nAvailable operations: show, crop, resize, threshold, contours, blob")
    print("Enter 'exit' to quit the program.")
    cho = input("Enter your choice: ").strip().lower()
    
    if cho=="exit":
        print("you are exit succefully")
        break
    process(cho)    
    
        


