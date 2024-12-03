# ThesisMate: An AI Chatbot for Supervisor and Topic Recommendations

ThesisMate is an AI-powered chatbot designed to streamline the process of finding thesis supervisors and topics for students. The system leverages web scraping, data processing, natural language processing, and a user-friendly interface to deliver fast and accurate recommendations.

## Features

- **Supervisor and Topic Matching**: Provides tailored recommendations based on user queries and preferences.
- **Web Scraping**: Extracts data from university faculty websites for up-to-date supervisor profiles.
- **Efficient NLP Integration**: Uses Google's Gemma LLM and Groq's inference API for fast and contextual responses.
- **Interactive User Interface**: Built using Streamlit with custom CSS for an intuitive and visually appealing experience.
- **Accessible Deployment**: Deployed on Streamlit Community Cloud for free and easy access.

## Table of Contents

1. [Introduction](#introduction)
2. [Technologies Used](#technologies-used)
3. [Installation](#installation)
4. [Usage](#usage)
5. [How It Works](#how-it-works)
6. [Limitations and Future Work](#limitations-and-future-work)
7. [License](#license)

## Introduction

ThesisMate simplifies the complex task of finding the right thesis supervisor by providing quick, accurate recommendations. It ensures students can focus on their research rather than administrative challenges.

## Technologies Used

- **Programming Language**: Python
- **Frontend Framework**: Streamlit
- **Web Scraping**: Selenium
- **LLM**: Google Gemma integrated with Groq API
- **Embedding and Retrieval**: LangChain with FAISS
- **Deployment**: Streamlit Community Cloud, GitHub

## Installation

1. Clone this repository:
   git clone https://github.com/your-username/ThesisMate.git

2. Navigate to the project directory:
   cd ThesisMate
   
3. Install the required dependencies:
   pip install -r requirements.txt

4. Set up environment variables:
   - Create a `.env` file and include the following keys:
     GROQ_API_KEY=your_groq_api_key
     GOOGLE_API_KEY=your_google_api_key

## Usage

1. Place the faculty data file (PDF format) in the `data/` directory.
2. Run the Streamlit app: streamlit run app.py
3. Open the application in your browser and start querying the chatbot.

## How It Works

1. **Web Scraping**: Data is collected from faculty websites using Selenium and stored in a structured CSV format.
2. **Data Preparation**: The raw data is cleaned, refined, and converted into embeddings for efficient retrieval.
3. **LLM Integration**: User queries are processed through Google's Gemma LLM for personalized responses.
4. **UI Design**: The Streamlit-based interface allows users to interact with the chatbot seamlessly.
5. **Deployment**: The application is hosted on Streamlit Community Cloud for easy and free access.

## Limitations and Future Work

### Current Limitations:
- Limited dataset for supervisor profiles.
- Might struggle with ambiguous queries.
- Basic user interface with room for enhancement.

### Future Improvements:
- Scalability for larger datasets.
- Enhanced NLP capabilities for handling ambiguous queries.
- Additional functionalities such as direct thesis document uploads.

## License

This project is licensed under the [MIT License](LICENSE).
