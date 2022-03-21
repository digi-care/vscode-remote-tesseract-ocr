import cv2
from PIL import Image
import pyocr

# tesseract
tools = pyocr.get_available_tools()
tool = tools[0]

# jpg
img_cv = cv2.imread(r'data/sample/sample.jpg')

# ocr
img_pil = Image.fromarray(img_cv)
builder = pyocr.builders.WordBoxBuilder(tesseract_layout=6)
wordboxies = tool.image_to_string(img_pil, 'eng', builder)

# result
i=0
for wordbox in wordboxies:
    i += 1
    print('#:', i)
    cv2.putText(img_cv, str(i), wordbox.position[1], cv2.FONT_HERSHEY_SIMPLEX, 3.0, (0,0,255))
    print('content:', wordbox.content)
    print('position:',wordbox.position)
    cv2.rectangle(img_cv, wordbox.position[0], wordbox.position[1], (0, 0, 255), 2)

# write, png
cv2.imwrite('data/sample/sample_result.png', img_cv)
