import random

def get_random_image_file():    
    num = random.randint(1, 11)
    im_file = f'./OCR/CardImages/index{num}.jpg'
    return im_file
