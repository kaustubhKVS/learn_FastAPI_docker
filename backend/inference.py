import io
import torch
from torchvision import transforms
from PIL import Image

import resnet12_ml_model

import config_ml

IMAGE_SIZE = 224

img_size : int = IMAGE_SIZE

# Labels for classification
labelclass = ["Normal", "Infiltration", "Atelectasis",
              "Effusion", "Nodule", "Pneumothorax", "Mass"]

# Creating dictionery for associating labels from output
op_to_labels = {i: j for i, j in zip(range(7), labelclass)}

# Setting up Inference Mode of EXECUTION

device = ("cuda:0" if torch.cuda.is_available() else 'cpu')
print("INFERENCE DEVICE :", device)

# Loading Model
num_classes = 7
model = resnet12_ml_model.resnet12(num_classes).to(device)
state_dict = torch.load(config_ml.TRAINED_MODEL_FILE_PATH, map_location=torch.device('cpu'))      
model.load_state_dict(state_dict)           # Load state dictonary
model.to(device)
model.eval()
print("MODEL LOAD SUCCESSFUL")

# Input Image and preprocess
def filenameToPILImage(x): return Image.open(x).convert('RGB')

infer_transform = transforms.Compose([filenameToPILImage, transforms.Resize(
    (img_size, img_size)), transforms.ToTensor(), transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])


async def get_fsm_prediction(file_content: bytes):
    
    file_content = io.BytesIO(file_content)
    
    image = infer_transform(file_content)
    image = image.reshape(1, *image.shape)
    preds = model(image.to(device))
    predicted_image_label = op_to_labels[preds.max(1)[1].cpu().numpy().tolist()[0]]
    
    return predicted_image_label

# Labels in the Model are:

"""
No Finding            60361
Infiltration           9547
Atelectasis            4215
Effusion               3955
Nodule                 2705
Pneumothorax           2194
Mass                   2139

"""