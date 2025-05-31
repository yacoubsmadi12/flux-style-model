from PIL import Image
import torch
from torchvision import transforms
import io

def load_model():
    # نموذج بسيط تجريبي - عدله بنموذج حقيقي لاحقًا
    def dummy_style(image):
        return image.transpose(Image.FLIP_LEFT_RIGHT)
    return dummy_style

def predict(image, prompt):
    model = load_model()
    styled = model(image)
    output = io.BytesIO()
    styled.save(output, format="PNG")
    output.seek(0)
    return output
