from PIL import Image, ImageFilter, ImageEnhance
import numpy as np
import cv2 as cv


class ImageOps:
    def CropImage(self):
        """Crops an image based on user-provided coordinates and saves the cropped image to disk.

        Prompts the user to input the coordinates (x1, x2, y1, y2) for cropping the image. It then extracts the specified region from the image data, converts it to an image object, saves it to a predefined path, and returns the cropped image object.

        Returns:
            PIL.Image.Image: The cropped image object.

        Note:
            This method depends on the variable `imgdata` being accessible and containing image data as a NumPy array.
            The output path is hardcoded and should be adjusted for different environments."""
        print("Enter x1,x2,y1,y2")
        x1 = int(input("Enter x1: "))
        x2 = int(input("Enter x2: "))
        y1 = int(input("Enter y1: "))
        y2 = int(input("Enter y2: "))
        img_cropped_data = imgdata[x1:x2, y1:y2, :]
        data = Image.fromarray(img_cropped_data)
        data.save("D:\\Python major\\Output\\ImageCropped.png")
        img = data
        return img

    def Filters(self):
        """Displays a menu of image filter options for the user to select from.

        Prompts the user to enter a choice corresponding to an image filter operation. The method prints a numbered list of available filters, including grayscale, sepia, blur, sharpen, and others. Note that gamma correction is indicated as not working.

        This method is primarily used to guide users in selecting an image filter within the ImageEditor workflow. It does not apply any filters itself or return a value."""
        print("Enter an operation to perform")
        print("Choose a filter from the list:")
        print("1. Grayscale")
        print("2. Sepia")
        print("3. Blur")
        print("4. Sharpen")
        print("5. Threshold")
        print("6. Saturation")
        print("7. Contrast")
        print("8. Brightness")
        print("9. Gamma correction (Not Working)")
        print("10. Emboss")
        print("11. Glow")
        print("12. Noir")
        print("13. Monochrome")
        print("14. Film")
        print("15. Vivid")
        print("16. Cool")

    def FlipImageHorizontal(self, img):
        """Flip an image horizontally and save the result to a predefined file path.

        Args:
            img (PIL.Image.Image): The image to be flipped horizontally.

        Returns:
            PIL.Image.Image: The horizontally flipped image.

        The original image is closed after flipping. The flipped image is saved to
        'D:\\\\Python major\\\\Output\\\\ImageFlippedHorizontal.png' before being returned."""
        horizontal_flip = img.transpose(Image.FLIP_LEFT_RIGHT)
        horizontal_flip.save("D:\\Python major\\Output\\ImageFlippedHorizontal.png")
        img.close()
        img = horizontal_flip
        return img

    def FlipImageVertical(self, img):
        """Flip an image vertically and save the result to a predefined file path.

        Args:
            img (PIL.Image.Image): The input image to be flipped vertically.

        Returns:
            PIL.Image.Image: The vertically flipped image.

        Note:
            The flipped image is saved to 'D:\\\\Python major\\\\Output\\\\ImageFlippedVertical.png'.
            The original image is closed within the method before returning the flipped image."""
        vertical_flip = img.transpose(Image.FLIP_TOP_BOTTOM)
        vertical_flip.save("D:\\Python major\\Output\\ImageFlippedVertical.png")
        img.close()
        img = vertical_flip
        return img

    def RotateImage(self, img):
        """Rotates the given image by a user-specified angle and saves the result.

        Prompts the user to enter an integer angle for rotation, rotates the provided image accordingly,
        saves the rotated image to a fixed output path ('D:\\\\Python major\\\\Output\\\\ImageRotated.png'),
        and returns the rotated image object.

        Args:
            img (PIL.Image.Image): The image to be rotated.

        Returns:
            PIL.Image.Image: The rotated image."""
        angle = int(input("Enter angle for rotation"))
        rotated_image = img.rotate(angle)
        rotated_image.save("D:\\Python major\\Output\\ImageRotated.png")
        img.close
        img = rotated_image
        return img

    def Capture(self, img):
        """Captures an image from the default camera after a brief delay and saves it to a file.

        Args:
            img (PIL.Image.Image): An image object that will be replaced by the newly captured image.

        Returns:
            PIL.Image.Image: The newly captured and opened image, or None if the capture failed.

        Note:
            Prints a message indicating a 7-second wait before capturing, but does not implement an actual delay.
            The original `img` parameter is not modified in-place due to rebinding; the returned image should be used instead.
            The image is saved to a hardcoded path: "D:\\\\Python major\\\\Output\\\\ImageCapture.png"."""
        print("Taking image in 7 seconds")
        cam = cv.VideoCapture(0)
        result, image2 = cam.read()
        if result:
            img.close
            cv.imwrite("D:\\Python major\\Output\\ImageCapture.png", image2)
            img = Image.open("D:\\Python major\\Output\\ImageCapture.png")
            return img

    def GetChannel(self, img, channelchoice):
        """Extracts a single color channel from the given image and saves it as a new image file.

        Args:
            img (numpy.ndarray): The input image array from which to extract the channel.
            channelchoice (int): The index of the color channel to extract (e.g., 0 for Red, 1 for Green, 2 for Blue).

        Returns:
            None

        Saves the extracted channel image to 'D:\\\\Python major\\\\Output\\\\ImageChannel.png' as a PNG file."""
        channel = np.zeros(imgdata.shape, dtype="uint8")
        channel[:, :, channelchoice] = imgdata[:, :, channelchoice]
        image_channel = Image.fromarray(channel)
        image_channel.save("D:\\Python major\\Output\\ImageChannel.png")


choice1 = "y"
image1 = ImageOps()
img = Image.open("D:\\Python major\\CdvY2Q4_d.jpg")
imgdata = np.array(img)
dims = imgdata.shape
list1 = list(dims)
height = list1[0]
width = list1[1]
channels = list1[2]
print("The height of this image is " + str(height))
print("The width of this image is " + str(width))
print("This image has " + str(channels) + " channels")
while choice1 == "y":
    print("Enter an operation to perform")
    print("1. Cropping")
    print("2. Filters")
    print("3. Flipping")
    print("4. Rotation")
    print("5. Get Channel (Will not select image for further operations)")
    print("6. Capture Image for operations")
    opchoice = int(input("Enter your choice: "))
    if opchoice == 1:
        img = image1.CropImage()
    if opchoice == 2:
        image1.Filters()
        filter_choice = int(input("Enter the number of the filter you want to apply: "))
        if filter_choice == 1:
            filtered_img = img.convert("L")
        elif filter_choice == 2:
            filtered_img = ImageEnhance.Color(img).enhance(0.5)
            filtered_img = ImageEnhance.Contrast(filtered_img).enhance(1.3)
        elif filter_choice == 3:
            filtered_img = img.filter(ImageFilter.GaussianBlur(radius=5))
        elif filter_choice == 4:
            filtered_img = img.filter(ImageFilter.SHARPEN)
        elif filter_choice == 5:
            filtered_img = img.convert("L")
            filtered_img = filtered_img.point(lambda x: 0 if x < 128 else 255, "1")
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
            filtered_img = img.convert("L")
            filtered_img = filtered_img.filter(ImageFilter.CONTOUR)
        elif filter_choice == 13:
            filtered_img = img.convert("L")
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
        filtered_img.save("D:\\Python major\\Output\\ImageFiltered.png")
        img.close()
        img = filtered_img
    elif opchoice == 3:
        flipchoice = int(input("Horizontal or Vertical? 1 = H, 2 = V "))
        if flipchoice == 1:
            img = image1.FlipImageHorizontal(img)
        elif flipchoice == 2:
            img = image1.FlipImageVertical(img)
    elif opchoice == 4:
        img = image1.RotateImage(img)
    elif opchoice == 5:
        channelchoice = int(
            input("Enter channel to print \n0: Red\n1: Green\n2: Blue: ")
        )
        image1.GetChannel(img, channelchoice)
    elif opchoice == 6:
        img = image1.Capture(img)
    print("Operation Complete, Output has been saved to D:/Python Major/Output")
    choice1 = input("Continue operations?\n y = yes\n n = no: ")
print("Saving final output to D:\\Python major\\Final")
img.save("D:\\Python major\\Final\\FinalImage.png")
img.close()
