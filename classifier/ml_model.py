from torchvision import models, transforms
from torchvision.models import ResNet18_Weights
from PIL import Image
import torch
model = models.resnet18(weights=ResNet18_Weights.DEFAULT)
model.eval()

preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    ),
])

softmax = torch.nn.Softmax(dim=1)


def classify_image(image_path):
    img = Image.open(image_path).convert("RGB")
    img_tensor = preprocess(img).unsqueeze(0)

    with torch.no_grad():
        output = model(img_tensor)
        probabilities = softmax(output)
        confidence, predicted_index = torch.max(probabilities, dim=1)

    categories = ResNet18_Weights.DEFAULT.meta["categories"]
    class_name = categories[predicted_index.item()]

    return class_name, confidence.item()