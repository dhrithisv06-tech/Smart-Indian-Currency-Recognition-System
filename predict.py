import torch
from PIL import Image
import torchvision.transforms as transforms
import torch.nn.functional as F

from model import CurrencyCNN
from labels import CLASS_NAMES, CURRENCY_LABELS


# Device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


# Load Model
model = CurrencyCNN()

model.load_state_dict(
    torch.load(
        "currency_model.pth",
        map_location=device
    )
)

model.to(device)
model.eval()


# Image Transform
transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor(),
    transforms.Normalize(
        [0.5, 0.5, 0.5],
        [0.5, 0.5, 0.5]
    )
])


def predict_image(image):

    image = image.convert("RGB")
    image = transform(image)
    image = image.unsqueeze(0)
    image = image.to(device)

    with torch.no_grad():

        output = model(image)

        probabilities = F.softmax(output, dim=1)

        confidence, prediction = torch.max(probabilities, 1)

    predicted_class = CLASS_NAMES[prediction.item()]

    return (
        CURRENCY_LABELS[predicted_class],
        confidence.item() * 100
    )