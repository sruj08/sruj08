import os
import sys
import urllib.request
from PIL import Image, ImageEnhance, ImageOps

def fetch_avatar(username="sruj08", output_path="data/source-photo.jpg"):
    url = f"https://avatars.githubusercontent.com/u/205763298?v=4"
    print(f"Downloading GitHub avatar for {username} from {url}...")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response, open(output_path, 'wb') as out_file:
        out_file.write(response.read())
    print(f"Saved avatar to {output_path}")
    return output_path

def remove_background(img_path):
    print("Attempting background removal...")
    try:
        from rembg import remove
        input_image = Image.open(img_path)
        output_image = remove(input_image)
        print("Background successfully removed using rembg.")
        return output_image
    except Exception as e:
        print(f"rembg unavailable or skipped ({e}), using Pillow image processing...")
        img = Image.open(img_path).convert("RGBA")
        return img

def apply_contrast_enhancement(pil_img):
    try:
        import cv2
        import numpy as np
        # Use OpenCV CLAHE if cv2 is installed
        cv_img = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2GRAY)
        clahe = cv2.createCLAHE(clipLimit=3.5, tileGridSize=(8, 8))
        clahe_img = clahe.apply(cv_img)
        return Image.fromarray(clahe_img)
    except Exception as e:
        print(f"cv2 unavailable ({e}), using PIL contrast enhancement...")
        gray_img = ImageOps.grayscale(pil_img)
        enhancer = ImageEnhance.Contrast(gray_img)
        enhanced = enhancer.enhance(2.2)
        # Apply auto-contrast
        return ImageOps.autocontrast(enhanced)

def prep_photo(input_path="data/source-photo.jpg", output_path="data/source-prepped.png"):
    if not os.path.exists(input_path):
        fetch_avatar("sruj08", input_path)
    
    rgba_img = remove_background(input_path)
    
    # Convert RGBA to white background composite
    bg = Image.new("RGBA", rgba_img.size, (255, 255, 255, 255))
    composited = Image.alpha_composite(bg, rgba_img).convert("RGB")
    
    prepped_img = apply_contrast_enhancement(composited)
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    prepped_img.save(output_path)
    print(f"Prepped photo successfully written to {output_path}")

if __name__ == "__main__":
    src_photo = sys.argv[1] if len(sys.argv) > 1 else "data/source-photo.jpg"
    prep_photo(src_photo, "data/source-prepped.png")
