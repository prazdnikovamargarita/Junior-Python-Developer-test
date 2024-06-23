Setup
Create a virtual environment:
python -m venv env
use `env\Scripts\activate`

Install dependencies:
pip install -r requirements.txt

Write your_api_key in main.py


Run the application:
uvicorn main:app --reload

Test the endpoint:
Send a POST request to http://127.0.0.1:8000/summarize with a JSON body containing the text to be summarized.
