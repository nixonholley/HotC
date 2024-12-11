import cv2
import pytesseract
from utils import select_roi

def get_selected_regions(im):
    card_id = select_roi(im, 'id')
    card_name = select_roi(im, 'name')
    card_text = select_roi(im, 'text')

    return [card_id, card_name, card_text]

def get_custom_regions(im):
    card_id = im[440:440+18, 314:314+91]
    # card_name = im[11:11+51, 16:16+359]
    # card_text = im[467:467+116, 26:26+390]

    #return [card_id, card_name, card_text]
    return [card_id]

def image_to_string(im):
    regions = get_custom_regions(im)
    region_types = ['Card_ID', 'Card_Name', 'Card_Text']

    text = ''
    for i, region in enumerate(regions):
        resized_im = cv2.resize(region, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
        enhanced_im = cv2.convertScaleAbs(resized_im, alpha=1.5, beta=20)  # Adjust alpha and beta
        gray_im = cv2.cvtColor(enhanced_im, cv2.COLOR_BGR2GRAY)
        binary_im = cv2.adaptiveThreshold(gray_im, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
        denoised_im = cv2.medianBlur(binary_im, 3)
        cv2.imwrite(f'./temp/{region_types[i]}.jpg', denoised_im)

        region_text = pytesseract.image_to_string(denoised_im)
        text += f'{region_types[i]}: {region_text}\n'

    return text
    