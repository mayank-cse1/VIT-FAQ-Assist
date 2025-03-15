<!-- #Dev - Bank Bot -->
<a name="readme-top"></a>
<h1 align="center">VIT-FAQAssist: AI-Powered FAQ Chatbot for VIT University</h1>
  <p align="center">
    VIT-FAQAssist is a custom-built **AI chatbot** designed to answer frequently asked questions about **VIT University**. It utilizes **CNN-based intent recognition** and integrates **TensorFlow & PyTorch** models for accurate classification and response generation. The chatbot enhances information accessibility for students and faculty by automating responses using **Natural Language Processing (NLP)** techniques.
    <br />
    <a href="https://github.com/mayank-cse/DEV-A-Virtual-Banking-Assistant"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="#demo-video">View Demo</a>
    ·
    <a href="https://github.com/mayank-cse/DEV-A-Virtual-Banking-Assistant/issues">Report Bug</a>
    ·
    <a href="https://1drv.ms/p/s!AqPutyaMMDPchxk-rgpzvvOp-avH?e=39UbKT">View Presentation</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#prerequisites">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#overview">Overview</a></li>
        <li><a href="#install-net-core-cli">Installation</a></li>
        <li><a href="#create-a-luis-application-to-enable-language-understanding">Enable LUIS</a></li>
      </ul>
    </li>
    <li><a href="#to-try-this-sample">Try This Sample</a></li>
    <li><a href="#testing-the-bot-using-bot-framework-emulator">Emulator Testing</a></li>
    <li><a href="#deploy-the-bot-to-azure">Deploying</a></li>
    <li><a href="#flow-chart">Flow Chart</a></li>
    <li><a href="#presentation">Presentation</a></li>
    <li><a href="#implementation-video">Implementation</a></li>
    <li><a href="#demo-video">Demo Video</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#further-reading">Further Reading</a></li>
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

## 📂 Project Structure
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
## ⚙️ Installation & Setup
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
[DEV BankingBot Presentation.pptx](https://github.com/mayank-cse/DEV-A-Virtual-Banking-Assistant/blob/main/Resources/Dev%20PPT%202.0.pptx)
<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Flow Chart
<img width="960" alt="Dev_FlowChart" src="https://user-images.githubusercontent.com/72187020/205635169-2e3b0719-bc92-42e0-8d4e-46fc9b8d7a59.png">


<!-- CONTACT -->
## Contact

Mayank Gupta - [@MayankGuptaCse1](https://twitter.com/MayankGuptacse1) - mayank.guptacse1@gmail.com

Project Link: [https://github.com/mayank-cse/DEV-A-Virtual-Banking-Assistant](https://github.com/mayank-cse/DEV-A-Virtual-Banking-Assistant)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Further reading

- [Bot Framework Documentation](https://docs.botframework.com)
- [Bot Basics](https://docs.microsoft.com/azure/bot-service/bot-builder-basics?view=azure-bot-service-4.0)
- [Dialogs](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-concept-dialog?view=azure-bot-service-4.0)
- [Gathering Input Using Prompts](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-prompts?view=azure-bot-service-4.0&tabs=csharp)
- [Activity processing](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-concept-activity-processing?view=azure-bot-service-4.0)
- [Azure Bot Service Introduction](https://docs.microsoft.com/azure/bot-service/bot-service-overview-introduction?view=azure-bot-service-4.0)
- [Azure Bot Service Documentation](https://docs.microsoft.com/azure/bot-service/?view=azure-bot-service-4.0)
- [.NET Core CLI tools](https://docs.microsoft.com/en-us/dotnet/core/tools/?tabs=netcore2x)
- [Azure CLI](https://docs.microsoft.com/cli/azure/?view=azure-cli-latest)
- [Azure Portal](https://portal.azure.com)
- [Language Understanding using LUIS](https://docs.microsoft.com/en-us/azure/cognitive-services/luis/)
- [Channels and Bot Connector Service](https://docs.microsoft.com/en-us/azure/bot-service/bot-concepts?view=azure-bot-service-4.0)
