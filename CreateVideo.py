import os
import cv2

path = "/Users/aakashnarne/Downloads/Images"

images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext.lower() in [".jpg", ".jpeg", ".png"]:
        file_name = os.path.join(path, file)
        print(file_name)
        images.append(file_name)

count = len(images)

if count == 0:
    print("No images found in the specified directory.")
    exit()

frame = cv2.imread(images[0])
if frame is None:
    print("Error reading the first image.")
    exit()

height, width, channels = frame.shape

size = (width, height)
print(size)

out = cv2.VideoWriter("Project.avi", cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

for i in range(count):
    img = cv2.imread(images[i])
    if img is None:
        print(f"Error reading image {images[i]}. Skipping.")
        continue
    out.write(img)

out.release()

print("Done")

cv2.waitKey(0)
