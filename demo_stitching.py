import cv2

def recorta (img, ancho, solapamiento):
    height, width, _ = img.shape
    p = 0
    n = 1
    while p < width:
        cropped_image = img[0:height, p:p+ancho]
        cv2.imwrite("imagen_"+str(n)+".jpg", cropped_image)
        n = n+1
        p = p + ancho - solapamiento
    return n-1


def stitching(n):
    images = []
    for i in range (1,n+1):
        image= cv2.imread('imagen_'+str(i)+'.jpg')
        if image is not None:
            images.append(image)
    stitcher = cv2.Stitcher_create()
    result = stitcher.stitch((tuple(images)))
    cv2.imwrite('res.jpg', result[1])

img = cv2.imread('original.jpg')
n = recorta (img, 400, 200)
print ('numero de fotos ',n)
stitching(n)
print ('listo')
