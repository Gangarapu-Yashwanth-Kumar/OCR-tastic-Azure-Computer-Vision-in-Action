# OCR-tastic: Azure Computer Vision in Action 🚀

## Overview ✨
This repository provides a practical demonstration of Optical Character Recognition (OCR) using **Azure Computer Vision** integrated with a **Flask web application**. It's designed to showcase how to extract text accurately from image-based documents, such as Aadhar cards and Driving Licenses, offering a user-friendly interface for intelligent document processing.

## Tech Stack Used 🛠️
* **Programming Language:** Python 🐍
* **Web Framework:** Flask 💡
* **Azure Service:** Azure Computer Vision ☁️ (for robust OCR capabilities)
* **Python Libraries:**
    * `flask`
    * `azure-cognitiveservices-vision-computervision`
    * `msrest`
* **Development Environment:** Jupyter Notebooks 📓 (for initial demonstrations)

## Key Features & Responsibilities 🚀
* **Azure Computer Vision Integration:** Utilizes Azure's powerful Read API for high-accuracy text extraction from various document types. 🧠
* **Web-based OCR Tool:** Provides a simple yet effective Flask application allowing users to upload images and instantly view extracted text. 🌐
* **Document-Specific Examples:** Includes ready-to-run examples demonstrating OCR on common Indian ID documents like Aadhar cards and Driving Licenses. 🆔
* **Asynchronous API Handling:** Implements polling mechanisms to efficiently manage the asynchronous nature of Azure's OCR operations. ⏳
* **Practical Demonstrations:** Both a Flask app and a Jupyter Notebook offer clear, runnable code to understand the integration process.

## Learning Outcome 🎓
Upon exploring this repository, you will be able to:
* Confidently integrate Python applications with **Azure Computer Vision** for advanced OCR functionalities.
* Understand and implement a Flask web application to serve as a front-end for cloud AI services.
* Gain practical experience in handling asynchronous API responses and processing structured OCR results.
* Learn best practices for setting up and connecting to Azure Cognitive Services from a Python environment.
* Develop foundational skills for building intelligent document processing solutions.

## Getting Started ▶️
1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/your-username/OCR-tastic-Azure-Computer-Vision-in-Action.git](https://github.com/your-username/OCR-tastic-Azure-Computer-Vision-in-Action.git)
    cd OCR-tastic-Azure-Computer-Vision-in-Action
    ```
2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: `venv\Scripts\activate`
    ```
3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    * Create a `requirements.txt` file in your repository root with the following content:
        ```
        flask
        azure-cognitiveservices-vision-computervision
        msrest
        ```
4.  **Azure Setup:** Ensure you have an active Azure subscription and a **Computer Vision** resource configured with appropriate access keys/endpoints.

## Configuration 🔑
**Important:** To run these samples successfully, you must obtain the correct authentication keys and service URLs directly from your Azure account.
* **Azure Computer Vision:** Find your **Endpoint** and **Keys** from the Computer Vision service overview in the Azure portal.
    * Open `app.py` and `OCR Demo.ipynb`.
    * Replace placeholder values (`'GET YOUR KEY FROM AZURE '` and `'ENTER YOUR ENDPOINT FROM AZURE'`) with your actual Azure Computer Vision **Key** and **Endpoint**.
    * *Always keep your keys secure and never expose them publicly in your code or repositories. Consider using environment variables for production deployments.*

## Usage ▶️

### Running the Flask Application
1.  **Start the Flask development server:**
    ```bash
    export FLASK_APP=app.py # On Windows: `set FLASK_APP=app.py`
    flask run
    ```
2.  **Access the application**: Open your web browser and navigate to `http://127.0.0.1:5000/`.
3.  **Upload an Image**: Use the provided interface to upload an image file (e.g., a JPG of an Aadhar card or Driving License).
4.  **View Extracted Text**: The extracted text will be displayed on the page.

### Running the Jupyter Notebook (for demonstration)
1.  **Start Jupyter Notebook:**
    ```bash
    jupyter notebook
    ```
2.  **Open `OCR Demo.ipynb`**: Navigate to and open the `OCR Demo.ipynb` file in your browser.
3.  **Run Cells**: Execute the cells sequentially to see the OCR process in action for predefined images. (Ensure the image paths within the notebook are correct, or place the sample images in the expected path.)

## Contributing
Contributions are welcome! If you have suggestions for improvements, new features, or bug fixes, please feel free to open an issue or submit a pull request.

## Thank You 🙏
Thank you for checking out OCR-tastic! We appreciate your interest and hope this project is helpful in your Azure cloud development journey with Python.
