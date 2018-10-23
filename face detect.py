import cv2
import PIL.Image, PIL.ImageDraw
import matplotlib.pyplot
import matplotlib.image


def detectByClf(image_name, clf):

    #openCV read
    img = cv2.imread(image_name)

    #openCV
    smiles_cascade = cv2.CascadeClassifier(clf)

    #decrease dimension
    if img.ndim == 3:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        gray = img

    print("start detecting...")
    zones = smiles_cascade.detectMultiScale(gray, 1.3, 5)
    result = []
    for (x, y, width, height) in zones:
        result.append((x, y, x + width, y + height))
    print("end detecting.")
    return result


def main():
    clf_face = "haarcascades/haarcascade_frontalface_default.xml" #Open CV haarcascades, trained by OpenCV, can using self-trained data
    picture = "group.jpg" #Picture input

    #open picture
    Image_object = PIL.Image.open(picture)

    #run detection
    result = detectByClf(picture, clf_face)

    #draw picture
    if(result):
        print("starting drawing the result")

        draw_instance = PIL.ImageDraw.Draw(Image_object,'RGBA')
        for (x1,y1,x2,y2) in result:
            draw_instance.ellipse((x1, y1, x2, y2), outline=(0, 255, 0), fill=(200,0,0,80))
            print(x1,y1,x2,y2)



    #plot
    matplotlib.pyplot.imshow(Image_object)
    matplotlib.pyplot.show()





if __name__ == '__main__':
    main()
