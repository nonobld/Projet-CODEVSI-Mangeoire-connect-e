import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions

# Charger le modèle ResNet50 pré-entraîné
model = ResNet50(weights='imagenet')

def predict_bird_species(image_path):
    # Charger et prétraiter l'image
    img = image.load_img(image_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    # Faire une prédiction
    preds = model.predict(x)

    # Décoder les prédictions
    decoded_preds = decode_predictions(preds, top=3)[0]

    # Renvoyer les trois prédictions les plus probables
    for i, (imagenet_id, label, score) in enumerate(decoded_preds):
        print("Prediction {}: {} (Confidence: {:.2f}%)".format(i+1, label, score*100))

# Utilisation de la fonction pour prédire l'espèce d'oiseau dans une image
predict_bird_species('bird_image.jpg')
