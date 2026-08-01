from PIL import Image
from predict import predict_image

image = Image.open("sample_images/test.jpg")

prediction, confidence = predict_image(image)

print("Prediction :", prediction)
print(f"Confidence : {confidence:.2f}%")