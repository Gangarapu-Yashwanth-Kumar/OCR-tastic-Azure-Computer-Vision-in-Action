import os
import time
from flask import Flask, request, render_template, redirect, url_for, flash
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from msrest.authentication import CognitiveServicesCredentials

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.secret_key = 'supersecretkey' # Replace with a strong secret key in production

# Ensure the upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Azure Computer Vision credentials
# IMPORTANT: In a production environment, store these securely (e.g., environment variables)
# The key and endpoint are taken directly from your provided Jupyter Notebook.
AZURE_VISION_KEY = 'GET YOUR KEY FROM AZURE '
AZURE_VISION_ENDPOINT = 'ENTER YOUR ENDPOINT FROM AZURE'
NUMBER_OF_CHARS_IN_OPERATION_ID = 36 # Standard length for Azure's operation ID

# Initialize Computer Vision client
try:
    credentials = CognitiveServicesCredentials(AZURE_VISION_KEY)
    computervision_client = ComputerVisionClient(
        endpoint=AZURE_VISION_ENDPOINT,
        credentials=credentials
    )
except Exception as e:
    print(f"Error initializing Azure Computer Vision client: {e}")
    computervision_client = None # Set to None if initialization fails

@app.route('/')
def index():
    """
    Renders the main page of the application.
    """
    return render_template('index.html', extracted_text=None)

@app.route('/upload', methods=['POST'])
def upload_file():
    """
    Handles file uploads, performs OCR using Azure Computer Vision,
    and displays the extracted text.
    """
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if file:
        # Save the uploaded file temporarily
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        extracted_text = "Error: Could not extract text."
        if computervision_client is None:
            flash("Azure Computer Vision client not initialized. Please check API key and endpoint.")
            # Clean up the uploaded file
            os.remove(filepath)
            return render_template('index.html', extracted_text=extracted_text)

        try:
            # Open the image file in binary read mode
            with open(filepath, "rb") as read_image:
                # Call the Azure Computer Vision Read API
                # This sends the image stream for text recognition
                raw_response = computervision_client.read_in_stream(read_image, language="en", raw=True)

            # Get the operation ID from the response headers
            operation_location = raw_response.headers["Operation-Location"]
            operation_id = operation_location[len(operation_location) - NUMBER_OF_CHARS_IN_OPERATION_ID:]

            # Poll for the result of the OCR operation
            while True:
                read_result = computervision_client.get_read_result(operation_id)
                if read_result.status not in ['notStarted', 'running']:
                    break
                time.sleep(1) # Wait 1 second before polling again

            # Process and extract text if the operation succeeded
            if read_result.status == OperationStatusCodes.succeeded:
                lines = []
                for text_result in read_result.analyze_result.read_results:
                    for line in text_result.lines:
                        lines.append(line.text)
                extracted_text = "\n".join(lines)
            else:
                extracted_text = f"OCR operation failed with status: {read_result.status}"
                flash(extracted_text)

        except Exception as e:
            extracted_text = f"An error occurred during OCR: {e}"
            flash(extracted_text)
        finally:
            # Clean up the uploaded file
            if os.path.exists(filepath):
                os.remove(filepath)

        return render_template('index.html', extracted_text=extracted_text)

    flash('Something went wrong with the file upload.')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True) # Set debug=False for production
