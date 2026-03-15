**📄 File Generator**

File Generator is an AI-powered tool that automatically creates and manages .txt files using web-searched content based on user input.
Instead of manually searching, copying, and organizing information, the system gathers relevant content and generates a ready-to-use file in just one click.
The application also allows users to create, update, and delete files easily, making information collection faster and more efficient.


**🚀 Features**

📂 Create Files – Generate a .txt file instantly based on user input
🌐 Web-Based Content Generation – Searches the web to gather relevant information
✏️ Update Files – Modify or append new content anytime
🗑 Delete Files – Remove files when no longer needed
⚡ One-Click Workflow – Automates the process of searching and writing content
🤖 LLM Powered – Uses AI to refine and structure the gathered content


**🛠 Tech Stack**

--Frontend
Streamlit
--Backend
FastAPI
--AI / Processing
LLM
LangGraph (for workflow orchestration)
--Other
Web search integration


**⚙️ How It Works**

User enters a topic or instruction.
The system searches the web for relevant information.
The LLM processes and structures the content.
A .txt file is generated automatically with the gathered information.

--Users can later:
Update the file
Delete the file
Create new files


**📦 Installation**

Clone the repository:
git clone https://github.com/yourusername/file-generator.git
cd file-generator

Install dependencies:
pip install -r requirements.txt

Run the backend:
uvicorn main:app --reload

Run the frontend:
streamlit run app.py


**🎯 Purpose of the Project**

This project aims to simplify the process of gathering information and organizing it into files.

--Instead of manually:
searching for content
copying information
creating files

organizing text

the system automates everything, allowing users to generate structured files instantly with minimal effort.
