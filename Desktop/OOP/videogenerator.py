# importing libraries
import os
import cv2
from PIL import Image

# Checking the current directory path
print(os.getcwd())

# Folder which contains all the images
# from which video is to be generated
os.chdir("/home/likitha/Desktop/images")
print(os.getcwd())
path = "/home/likitha/Desktop/images"

mean_height = 0
mean_width = 0

# print(num_of_images)
num_of_images = len(os.listdir('.'))
# os.listdir() prints the contents of image directory in form of list

for file in os.listdir('.'):
    im = Image.open(os.path.join(path, file))
    width, height = im.size
    mean_width += width
    mean_height += height
    #im.show()
    print("good till here")

# Finding the mean height and width of all images.
mean_width = int(mean_width / num_of_images)
mean_height = int(mean_height / num_of_images)

#Resizing of the images to give them same width and height

for file in os.listdir('.'):
    if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith("png"):
        # opening image using PIL Image
        im = Image.open(os.path.join(path, file))

        # im.size includes the height and width of image
        width, height = im.size
        print(width, height)

        # resizing
        imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS)
        imResize.save( file, 'JPEG', quality = 95) # setting quality

        # printing each resized image name
        print(im.filename.split('\\')[-1], " is resized")

# Video Generating function
def generate_video():
    image_folder = '.'
    video_name = 'mygeneratedvideo.avi'
    os.chdir("/home/likitha/Desktop/images")
    #Array images should only consider the image files ignoring others if any
    images = [img for img in os.listdir(image_folder)
              if img.endswith(".jpg") or
                 img.endswith(".jpeg") or
                 img.endswith("png")]
    print(images)

    frame = cv2.imread(os.path.join(image_folder, images[0]))

     # setting the frame width, height
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, 0, 1, (width, height))
    # Appending the images to the video one by one

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    # Deallocating memories taken for window creation
    cv2.destroyAllWindows()
    video.release()  # releasing the video generated

# Calling the generate_video function
generate_video()

