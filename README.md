<!-- #Dev - Bank Bot -->
<a name="readme-top"></a>
<h1 align="center">VIT-FAQAssist: AI-Powered FAQ Chatbot for VIT University</h1>
  <p align="center">
    VIT-FAQAssist is a custom-built **AI chatbot** designed to answer frequently asked questions about **VIT University**. It utilizes **CNN-based intent recognition** and integrates **TensorFlow & PyTorch** models for accurate classification and response generation. The chatbot enhances information accessibility for students and faculty by automating responses using **Natural Language Processing (NLP)** techniques.
    <br />
    <a href="https://github.com/mayank-cse1/VIT-FAQ-Assist/blob/main/project_report/1538_VIT-FAQAssist_CAPSTONE.pdf"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/mayank-cse1/VIT-FAQ-Assist/blob/main/Power%20Point/Capstone%20Reveiw%201%20-%20VIT-FAQAssist%20Presentation.pptx">View Presentation</a>
    ·
    <a href="https://github.com/mayank-cse1/VIT-FAQ-Assist/issues">Report Bug</a>
    ·
    <a href="https://github.com/mayank-cse1/VIT-FAQ-Assist/blob/main/Power%20Point/FlowChart%20Diagram%20Final.pdf">View Flow</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li><li><a href="#project-structure">Project Structure</a></li>
      </ul>
    </li>
    <li>
      <a href="#installation-setup">Getting Started</a>
      <ul>
        <li><a href="#installation-setup">Prerequisites</a></li>
      </ul>
    </li>
    <li><a href="#flow-chart">Flow Chart</a></li>
    <li><a href="#presentation">Presentation</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

<img width="960" alt="DEV Activity Chart" src="https://user-images.githubusercontent.com/72187020/200659507-6ab4b64f-197b-44e2-9d62-be26c4b8b101.png">


VIT-FAQAssist is a custom-built **AI chatbot** designed to answer frequently asked questions about **VIT University**. It utilizes **CNN-based intent recognition** and integrates **TensorFlow & PyTorch** models for accurate classification and response generation. The chatbot enhances information accessibility for students and faculty by automating responses using **Natural Language Processing (NLP)** techniques. 

Dev is designed for the customers to :
- **Dual-Model Approach:** Implements both **TensorFlow and PyTorch** for intent classification.
- **Convolutional Neural Networks (CNNs):** Used for enhanced accuracy in intent recognition.
- **Pattern Matching & Data Augmentation:** Improves chatbot learning and response accuracy.
- **AIML-Based Structured Responses:** Ensures better handling of queries.
- **Fast and Scalable:** Optimized for handling large volumes of student and faculty queries.

Key Features of the Product :
* Instant Response with automatic time-to-time pop-ups (alerts).
* Proactively reaches out if a bill is higher than normal.
* Suspects fraud and sends mail alert.
* Provides reward and account balances, spending summaries, refund confirmations and credit scores. 
<!-- * Automating Business Operations for visible efficiency gains due to fast communication. -->

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Built With

- **Python**
- **TensorFlow & PyTorch** (Neural Network Models)
- **Natural Language Processing (NLP)**
- **FastAPI** (API Framework)
- **MongoDB & MySQL** (Databases for logging queries & responses)
- **AIML (Artificial Intelligence Markup Language)**

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Project Structure
```
src/
│── models/              # TensorFlow & PyTorch models for intent classification
│── dataset/             # Training dataset for intent recognition
│── api/                 # FastAPI backend for chatbot interaction
│── database/            # MongoDB & MySQL integration for response logging
│── frontend/            # UI for user interaction (Optional: PHP/JS-based)
│── utils/               # Helper scripts for data processing and model training
│── config.py            # Configuration file for settings
│── main.py              # API entry point
│── requirements.txt     # Project dependencies
│── README.md            # Documentation
```
## Installation Setup
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/mayank-cse1/VIT-FAQAssist.git
cd VIT-FAQAssist
```

### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Set Up Databases
Ensure **MongoDB** and **MySQL** are running, and update `config.py` with connection details.

### 4️⃣ Run the API
```sh
python main.py
```

## Presentation
[VIT FAQ Assist Presentation.pptx](https://github.com/mayank-cse1/VIT-FAQ-Assist/blob/main/Power%20Point/Capstone%20Reveiw%201%20-%20VIT-FAQAssist%20Presentation.pptx)
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Flow Chart
<img width="960" alt="VITFAQ_FlowChart" src="https://github.com/mayank-cse1/VIT-FAQ-Assist/blob/main/Power%20Point/FlowChart%20Diagram%20Final.pdf">

<!-- CONTACT -->
## Contact

Mayank Gupta - [@MayankGuptaCse1](https://twitter.com/MayankGuptacse1) - mayank.guptacse1@gmail.com

Project Link: [https://github.com/mayank-cse/DEV-A-Virtual-Banking-Assistant](https://github.com/mayank-cse/DEV-A-Virtual-Banking-Assistant)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
