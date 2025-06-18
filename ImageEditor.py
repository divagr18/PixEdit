from PIL import Image, ImageFilter, ImageEnhance
import numpy as np
import cv2 as cv


class ImageOps:

    def CropImage(self):
        print('Enter x1,x2,y1,y2')
        x1 = int(input('Enter x1: '))
        x2 = int(input('Enter x2: '))
        y1 = int(input('Enter y1: '))
        y2 = int(input('Enter y2: '))
        img_cropped_data = imgdata[x1:x2, y1:y2, :]
        data = Image.fromarray(img_cropped_data)
        data.save('D:\\Python major\\Output\\ImageCropped.png')
        img = data
        return img

    def Filters(self):
        print('Enter an operation to perform')
        print('Choose a filter from the list:')
        print('1. Grayscale')
        print('2. Sepia')
        print('3. Blur')
        print('4. Sharpen')
        print('5. Threshold')
        print('6. Saturation')
        print('7. Contrast')
        print('8. Brightness')
        print('9. Gamma correction (Not Working)')
        print('10. Emboss')
        print('11. Glow')
        print('12. Noir')
        print('13. Monochrome')
        print('14. Film')
        print('15. Vivid')
        print('16. Cool')

    def FlipImageHorizontal(self, img):
        horizontal_flip = img.transpose(Image.FLIP_LEFT_RIGHT)
        horizontal_flip.save(
            'D:\\Python major\\Output\\ImageFlippedHorizontal.png')
        img.close()
        img = horizontal_flip
        return img

    def FlipImageVertical(self, img):
        """Flip an image vertically, save the flipped image to a specified path, and return the flipped image.

Args:
    img (PIL.Image.Image): The input image to be flipped.

Returns:
    PIL.Image.Image: The vertically flipped image."""
        vertical_flip = img.transpose(Image.FLIP_TOP_BOTTOM)
        vertical_flip.save('D:\\Python major\\Output\\ImageFlippedVertical.png'
            )
        img.close()
        img = vertical_flip
        return img

    def RotateImage(self, img):
        angle = int(input('Enter angle for rotation'))
        rotated_image = img.rotate(angle)
        rotated_image.save('D:\\Python major\\Output\\ImageRotated.png')
        img.close
        img = rotated_image
        return img

    def Capture(self, img):
        print('Taking image in 7 seconds')
        cam = cv.VideoCapture(0)
        result, image2 = cam.read()
        if result:
            img.close
            cv.imwrite('D:\\Python major\\Output\\ImageCapture.png', image2)
            img = Image.open('D:\\Python major\\Output\\ImageCapture.png')
            return img

    def GetChannel(self, img, channelchoice):
        channel = np.zeros(imgdata.shape, dtype='uint8')
        channel[:, :, channelchoice] = imgdata[:, :, channelchoice]
        image_channel = Image.fromarray(channel)
        image_channel.save('D:\\Python major\\Output\\ImageChannel.png')


choice1 = 'y'
image1 = ImageOps()
img = Image.open('D:\\Python major\\CdvY2Q4_d.jpg')
imgdata = np.array(img)
dims = imgdata.shape
list1 = list(dims)
height = list1[0]
width = list1[1]
channels = list1[2]
print('The height of this image is ' + str(height))
print('The width of this image is ' + str(width))
print('This image has ' + str(channels) + ' channels')
while choice1 == 'y':
    print('Enter an operation to perform')
    print('1. Cropping')
    print('2. Filters')
    print('3. Flipping')
    print('4. Rotation')
    print('5. Get Channel (Will not select image for further operations)')
    print('6. Capture Image for operations')
    opchoice = int(input('Enter your choice: '))
    if opchoice == 1:
        img = image1.CropImage()
    if opchoice == 2:
        image1.Filters()
        filter_choice = int(input(
            'Enter the number of the filter you want to apply: '))
        if filter_choice == 1:
            filtered_img = img.convert('L')
        elif filter_choice == 2:
            filtered_img = ImageEnhance.Color(img).enhance(0.5)
            filtered_img = ImageEnhance.Contrast(filtered_img).enhance(1.3)
        elif filter_choice == 3:
            filtered_img = img.filter(ImageFilter.GaussianBlur(radius=5))
        elif filter_choice == 4:
            filtered_img = img.filter(ImageFilter.SHARPEN)
        elif filter_choice == 5:
            filtered_img = img.convert('L')
            filtered_img = filtered_img.point(lambda x: 0 if x < 128 else 
                255, '1')
        elif filter_choice == 6:
            filtered_img = ImageEnhance.Color(img).enhance(2.0)
        elif filter_choice == 7:
            filtered_img = ImageEnhance.Contrast(img).enhance(2.0)
        elif filter_choice == 8:
            filtered_img = ImageEnhance.Brightness(img).enhance(1.5)
        elif filter_choice == 9:
            filtered_img = ImageEnhance.Contrast(img).enhance(2.0)
            filtered_img = ImageEnhance.Brightness(filtered_img).enhance(1.5)
            filtered_img = ImageEnhance.Gamma(filtered_img).enhance(1.2)
        elif filter_choice == 10:
            filtered_img = img.filter(ImageFilter.EMBOSS)
        elif filter_choice == 11:
            filtered_img = ImageEnhance.Sharpness(img).enhance(2.0)
            filtered_img = ImageEnhance.Contrast(filtered_img).enhance(1.3)
            filtered_img = ImageEnhance.Brightness(filtered_img).enhance(1.1)
        elif filter_choice == 12:
            filtered_img = img.convert('L')
            filtered_img = filtered_img.filter(ImageFilter.CONTOUR)
        elif filter_choice == 13:
            filtered_img = img.convert('L')
        elif filter_choice == 14:
            filtered_img = ImageEnhance.Color(img).enhance(0.5)
            filtered_img = ImageEnhance.Contrast(filtered_img).enhance(1.5)
            filtered_img = ImageEnhance.Brightness(filtered_img).enhance(1.2)
        elif filter_choice == 15:
            filtered_img = ImageEnhance.Color(img).enhance(1.5)
            filtered_img = ImageEnhance.Contrast(filtered_img).enhance(1.2)
        elif filter_choice == 16:
            filtered_img = ImageEnhance.Color(img).enhance(0.5)
            filtered_img = ImageEnhance.Contrast(filtered_img).enhance(1.5)
        filtered_img.save('D:\\Python major\\Output\\ImageFiltered.png')
        img.close()
        img = filtered_img
    elif opchoice == 3:
        flipchoice = int(input('Horizontal or Vertical? 1 = H, 2 = V '))
        if flipchoice == 1:
            img = image1.FlipImageHorizontal(img)
        elif flipchoice == 2:
            img = image1.FlipImageVertical(img)
    elif opchoice == 4:
        img = image1.RotateImage(img)
    elif opchoice == 5:
        channelchoice = int(input(
            'Enter channel to print \n0: Red\n1: Green\n2: Blue: '))
        image1.GetChannel(img, channelchoice)
    elif opchoice == 6:
        img = image1.Capture(img)
    print('Operation Complete, Output has been saved to D:/Python Major/Output'
        )
    choice1 = input('Continue operations?\n y = yes\n n = no: ')
print('Saving final output to D:\\Python major\\Final')
img.save('D:\\Python major\\Final\\FinalImage.png')
img.close()
