from PIL import Image, ImageFilter
import os
from concurrent.futures import wait, as_completed
from concurrent.futures import ProcessPoolExecutor

def process_image(image_path):
  img = Image.open(image_path)
  img = img.filter(ImageFilter.BLUR)
  img = img.save(os.path.join(output_dir, os.path.basename(image_path)))
  return os.path.basename(image_path)
 
input_dir = "/home/admin/Imagens"
output_dir = "/home/admin/Imagens/processado"
os.makedirs(output_dir, exist_ok=True)
imagens = [os.path.join(input_dir, img) for img in os.listdir(input_dir) if img.endswith(".jpg")]

executor = ProcessPoolExecutor(max_workers=4)
result = executor.map(process_image, imagens)
print(list(result))

