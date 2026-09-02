# Image Classification API

A REST API built with Django and Django REST Framework that classifies uploaded images using a pre-trained PyTorch ResNet18 model. Every request is persisted to a database, including the predicted class and confidence score.

Built as a learning project to practice three core backend skills: building a REST API from scratch, integrating a machine learning model into a web backend, and working with a relational database.

## Features

- Upload an image via a REST endpoint
- Image is classified using a pre-trained ResNet18 (ImageNet, 1000 classes)
- Returns predicted class + confidence score as JSON
- Every request (image, prediction, confidence, timestamp) is saved to the database
- Django admin interface for browsing past classifications

## Tech Stack

- **Backend:** Django, Django REST Framework
- **Machine Learning:** PyTorch, torchvision (ResNet18, pre-trained on ImageNet)
- **Database:** SQLite
- **Image processing:** Pillow

## Prerequisites

- Python 3.10+
- pip

## Installation

1. Clone the repository

   ```bash
   git clone https://github.com/your-username/image-classification-api.git
   cd image-classification-api/project
   ```

2. Create and activate a virtual environment

   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\Activate.ps1

   # macOS / Linux
   source venv/bin/activate
   ```

3. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations

   ```bash
   python manage.py migrate
   ```

5. (Optional) Create a superuser to access the Django admin

   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server

   ```bash
   python manage.py runserver
   ```

The API will be available at `http://127.0.0.1:8000/`.

## Usage

### Classify an image

**Endpoint:** `POST /api/classify/`

**Body:** `multipart/form-data`

| Key          | Type | Description             |
|--------------|------|--------------------------|
| `file_input` | File | The image to classify   |

**Example request (curl):**

```bash
curl -X POST http://127.0.0.1:8000/api/classify/ \
  -F "file_input=@/path/to/image.jpg"
```

**Example response:**

```json
{
    "id": 1,
    "file_input": "/media/uploads/golden_retriever.png",
    "predicted_class": "golden retriever",
    "confidence_score": 0.9556,
    "timestamp": "2026-09-02T15:12:31.240257Z"
}
```

## Project Structure

```
project/
├── manage.py
├── db.sqlite3
├── requirements.txt
├── project/                # Django configuration
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── classifier/              # Main app
    ├── models.py            # DB model: image, prediction, confidence, timestamp
    ├── serializers.py       # DRF serializer
    ├── views.py             # API view (upload + classify)
    ├── urls.py               # App-level routing
    ├── ml_model.py          # ResNet18 wrapper (preprocessing + inference)
    ├── admin.py
    └── migrations/
```

## How It Works

1. The client sends a `POST` request with an image file.
2. `FileSerializer` validates the upload and saves the file + a database record (`predicted_class` and `confidence_score` are read-only and left empty at this stage).
3. `ml_model.py` loads the image with Pillow, preprocesses it (resize, center crop, normalize using ImageNet stats), and runs it through a pre-trained ResNet18.
4. Softmax + argmax are applied to the raw model output to get the predicted class and its confidence score.
5. The database record is updated with the prediction results.
6. The API returns the full record as JSON.

## Roadmap

- [ ] Error handling for invalid/corrupted image uploads
- [ ] `GET` endpoint to list past classifications
- [ ] File size validation
- [ ] Automated tests
- [ ] Support for swapping in EfficientNet or other architectures

## License

See [LICENSE](LICENSE) for details.
