import numpy as np
from patchify import patchify, unpatchify
from PIL import Image

img = Image.open( "ball.jpg" )
img.load()
# conviert image into a array numpy
tmp = np.asarray(img)
print ("shape of original image: ", tmp.shape)
# the shape of 'ball.jpg' is 428x800 pixels, each represented by 3 bytes (RGB code)
# it is convenient for this example that the each dimension is a multiple of 10
# I crop the image to get a 400x800 section
image = tmp [:400,:,:]
print ('Size of the croped image', image.shape)

#  CASO 1: TROCEO TODA LA IMAGEN SIN SOLAPAMIENTOS Y LUEGO LA RECUPERO ENTERA
# CASE 1: I split all the image without overlap and then reconstruct the whole image
# I want patches of 100x100 pixels without overlap
patches = patchify(image, (100,100,3), step=100)

# patches is a numpy array of shape (4,8,1,100,100,3)
# 4 rows of 8 patches each
# There is a third dimension that is not used here
# Each patch has 100x100 pixels and each pixel is represented by 3 bytes

print ('patches: ', patches.shape)

# I get the shape
(a,b,c,d,e,f) = patches.shape

# Now I save each patch in a jpg file

for i in range (a):
    for j in range (b):
        imagenTrozo = Image.fromarray( patches[i][j][0])
        # save image in file 'patch_i_j.jpg'
        imagenTrozo.save  ('patch_'+str(i)+'_'+str(j)+'.jpg')

# Now I will reconstruct the image from all the stored patches
# I need a numpy array with the adequate dimensions
recoveredPatches = np.zeros((a,b,c,d,e,f))

# I recover each patch, convert it in a numpy array and store it in the right place
for i in range (a):
    for j in range (b):
        img = Image.open('patch_'+str(i)+'_'+str(j)+'.jpg')
        img.load()
        np_img = np.asarray(img)
        recoveredPatches[i][j][0] =np.copy (np.asarray(img))
# Now I can reconstruct the original image from the patches.
# I must tell the function what is the shape of the image to be reconstructed
reconstructedImage = unpatchify(recoveredPatches, image.shape)
# Convert numpy array into a image
originalImage =Image.fromarray(reconstructedImage.astype(np.uint8))
originalImage.show()

# CASE 2: build a new image using only some of the patches
# I will build a image with 2x3 patches
onlySomePatches = np.zeros((2,3,1,d,e,f))

# I choose 6 (arbitrary) patches, convert each in a numpy array and put it
# in numpy array for the new image
img = Image.open('patch_1_4.jpg')
img.load()
np_img = np.asarray(img)
onlySomePatches[0][0][0] = np.copy(np.asarray(img))

img = Image.open('patch_1_0.jpg')
img.load()
np_img = np.asarray(img)
onlySomePatches[0][1][0] = np.copy(np.asarray(img))

img = Image.open('patch_2_2.jpg')
img.load()
np_img = np.asarray(img)
onlySomePatches[0][2][0] = np.copy(np.asarray(img))

img = Image.open('patch_0_1.jpg')
img.load()
np_img = np.asarray(img)
onlySomePatches[1][0][0] = np.copy(np.asarray(img))

img = Image.open('patch_0_1.jpg')
img.load()
np_img = np.asarray(img)
onlySomePatches[1][1][0] = np.copy(np.asarray(img))

img = Image.open('patch_3_3.jpg')
img.load()
np_img = np.asarray(img)
onlySomePatches[1][2][0] = np.copy(np.asarray(img))

# the new image will have 200 x 300 pixels
reconstructedImage = unpatchify(onlySomePatches, (200,300,3))
newImage =Image.fromarray(reconstructedImage.astype(np.uint8))
newImage.show()
