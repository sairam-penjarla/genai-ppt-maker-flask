# [![Website](https://img.shields.io/badge/Website-Visit-brightgreen)](https://psairam9301.wixsite.com/website) [![YouTube](https://img.shields.io/badge/YouTube-Subscribe-red)](https://www.youtube.com/@sairampenjarla) [![GitHub](https://img.shields.io/badge/GitHub-Explore-black)](https://github.com/sairam-penjarla) [![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/sairam-penjarla-b5041b121/) [![Instagram](https://img.shields.io/badge/Instagram-Follow-ff69b4)](https://www.instagram.com/sairam.ipynb/)

# Gen AI PPT Maker

## Project Overview
Gen AI PPT Maker is a powerful AI-driven tool that enables users to create professional presentations effortlessly. Users can specify their requirements, such as the number of slides, the desired content for each slide, and even select slide designs. The AI generates customized slides as per the inputs, allowing users to preview and download individual slides with chosen designs. The project leverages OpenAI's GPT technology, Flask, HTML, CSS, JS, and SQLite for seamless functionality.

---

## Getting Started

Follow the instructions below to set up and run the project on your local machine.

### Step 1: Clone the Repository
```bash
git clone https://github.com/sairam-penjarla/genai-ppt-maker-flask
```

### Step 2: Navigate to the Project Directory
```bash
cd genAI-ppt-maker-flask-
```

### Step 3: Set Up the Environment
To learn how to create a virtual environment, check out this [blog post](https://psairam9301.wixsite.com/website/post/learn-virtualenv-basics).

#### Using `virtualenv` (Recommended)
```bash
python3 -m venv env
source env/bin/activate  # For Linux/Mac
env\Scripts\activate    # For Windows
```

#### Using Anaconda
```bash
conda create -n genai-ppt-maker python=3.9
conda activate genai-ppt-maker
```

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 5: Add Your OpenAI API Token
1. Create a `.env` file in the root directory.
2. Add the following line to the file:
   ```env
   OPENAI_API_TOKEN=your_openai_api_key_here
   ```

### Step 6: Run the Project
```bash
python app.py
```

### Step 7: Access the Application
Open your browser and navigate to:
```text
http://127.0.0.1:5000/
```

---

## Features and Functionality

- **AI-Powered Slide Creation:** Specify the number of slides and detailed content for each slide, and let the AI generate them for you.
- **Slide Design Options:** Choose from a catalog of designs, and download individual slides as PPT files with the selected design and text.
- **Session Management:** View past sessions in the sidebar for quick access and reference.
- **Logging:** Logs are stored in the `app.log` file for troubleshooting and monitoring purposes.
- **OpenAI Integration:** Utilize OpenAI's GPT model for generating content dynamically.
- **Tech Stack:** Flask for backend, HTML/CSS/JS for frontend, and SQLite for database management.

---

## Additional Resources

- [Project Blog Post](https://psairam9301.wixsite.com/website/post/project-blog-gen-ai-ppt-maker)
- [YouTube Video](https://www.youtube.com/@sairampenjarla)
