import os
import torch
from PIL import Image
import torchvision.transforms as transforms
import torch.nn.functional as F

from model import CurrencyCNN
from labels import CLASS_NAMES, CURRENCY_LABELS

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

MODEL_PATH = "currency_model.pth"

model = None


def load_model():
    global model

    if model is None:

        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(
                "currency_model.pth not found."
            )

        model = CurrencyCNN()

        model.load_state_dict(
            torch.load(
                MODEL_PATH,
                map_location=device
            )
        )

        model.to(device)
        model.eval()

    return model


transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor(),
    transforms.Normalize(
        [0.5, 0.5, 0.5],
        [0.5, 0.5, 0.5]
    )
])


def predict_image(image):

    model = load_model()

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