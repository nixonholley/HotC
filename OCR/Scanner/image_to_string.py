import cv2
import pytesseract
from utils import select_roi, Card, valTrackbars, init_trackbars

def get_selected_regions(im):
    card_id = select_roi(im, 'id')
    card_name = select_roi(im, 'name')
    card_text = select_roi(im, 'text')

    return [card_id, card_name, card_text]

def get_custom_regions(im):
    card_id = im[435:435+25, 310:310+100]
    # card_name = im[11:11+51, 16:16+359]
    # card_text = im[467:467+116, 26:26+390]

    #return [card_id, card_name, card_text]
    return [card_id]

def image_to_string(im):
    regions = get_custom_regions(im)
    region_types = ['Card_ID', 'Card_Name', 'Card_Text']

    card = Card()
    for i, region in enumerate(regions):
        resized_im = cv2.resize(region, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

        #blur_im = cv2.GaussianBlur(resized_im,(5,5),0)
        gray_im = cv2.cvtColor(resized_im, cv2.COLOR_BGR2GRAY)
        
        init_trackbars()
        while True:
            # get track bar values
            thresh = valTrackbars()
            cutoff, threshold_im = cv2.threshold(gray_im, thresh[0],thresh[1], cv2.THRESH_BINARY+cv2.THRESH_OTSU)
            
            cv2.imshow('Image', threshold_im)
            # press q to break loop
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
        cv2.imwrite(f'./temp/{region_types[i]}.jpg', threshold_im)

        region_text = pytesseract.image_to_string(threshold_im)
        if i == 0:
            card.id = region_text
        elif i == 1:
            card.name = region_text
        elif i == 2:
            card.text = region_text

    return card
    