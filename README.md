# FastAPI SEO Analyzer Documentation

**Specifications**:

1. Create an API layer in your framework of choice (python/php) that takes in a URL of a web-page as input and outputs issues that the meta tags of the page might face with SEO (Search engine optimization)
 - [Hard constraint] Use an SQL based database to store info about the page
 - Add a schema diagram to explain your decisions regarding the database
 - If info about a page already exists in database, it should be returned
 - Expected input and output must be in JSON
 - API should be RESTful

2. Set up a background job that re-checks all the web-page urls and updates info about page in database every 1 hour

3. Implement a preview route that returns a preview image of the webpage that is loaded by the URL
 - Should take a URL as input and return an image as output
 - [Optional] Store the generated preview image directly in database

4. [Optional] Host your API solution on some free solution to host an API ("render.com" is a good option for API, "supabase" is a good free option for database)
5. [Optional] Feel free to add any improvements as you see fit

6. Add your code to a private repository on github:
 - Give access to this repository to nfk
 - Create a PR and assign reviewer to nfk user


## Tasks

- [ ] Task 1: API Layer 
- [ ] Task 2: Backgroudn job
- [ ] Task 3: preview image
- [ ] Task 4: [Optional] Host API on render.com
- [ ] Task 5: [Optional] Add improvements 
- [ ] Task 6: Host code on Github and open PR


## Installation Instructions

### 1. Set Up Virtual Environment (Optional but Recommended)

### Create a virtual environment
`python -m venv venv`

### Activate the virtual environment

**On Windows**
`venv\Scripts\activate`

**On Unix or MacOS** 
`source venv/bin/activate`

### 2. Install Dependencies

#### Install required Python packages
`pip install -r requirements.txt`

### 3. Database Setup

Set up your SQL database and configure the connection in the FastAPI app.

### 4. Run FastAPI App

#### Run the FastAPI application
uvicorn your_app_name:app --reload

Replace your_app_name with the actual name of your FastAPI application file.
5. Set Up and Run Celery Worker (For Background Job)

#### Run the Celery worker
celery -A your_app_name.celery_worker worker --loglevel=info

Replace your_app_name with the actual name of your FastAPI application file.
6. Schedule the Background Job (Update every 1 hour)

Adjust the Celery task to update the web pages and schedule it to run periodically.
7. Test the API Endpoints

Use tools like curl or a REST client to test the /analyze and /preview endpoints.

Note:
Ensure your SQL database is running and accessible.
Update database connection details in your FastAPI application.
Customize the Celery task for your specific update logic.
For more detailed configurations and options, refer to the documentation of FastAPI, UVicorn, and Celery.

