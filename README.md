# Norse FinCrime AI 🛡️

Norse FinCrime AI is a specialized research tool designed to navigate and analyze complex financial crime regulations and fraud typologies using **Retrieval-Augmented Generation (RAG)**.

## 🚀 Overview
This project was developed to streamline the study and research process for Anti-Money Laundering (AML) and Fraud certifications (like CAMS and CFE). By indexing thousands of pages of global regulatory standards, the AI provides high-accuracy, source-backed answers to complex compliance queries.

## 🛠️ Tech Stack
* **Language:** Python
* **Framework:** LlamaIndex (RAG Pipeline)
* **AI Model:** OpenAI GPT-4o
* **Interface:** Command Line Interface (CLI)

## 📚 Global Standards Indexed
This assistant is trained on the "Gold Standards" of financial crime prevention, including:
* **FATF 40 Recommendations:** The global standard for AML/CTF.
* **Wolfsberg Group Principles:** Focus on Correspondent Banking and Private Banking.
* **Basel Committee Standards:** Guidance on Customer Due Diligence (CDD) for banks.
* **FFIEC Manual:** U.S. regulatory red flags and exam procedures.
* **Egmont Group Cases:** Real-world financial intelligence unit (FIU) case studies.

## 💡 Key Features
* **Zero Hallucination Policy:** By using RAG, the AI only answers based on the provided regulatory PDFs.
* **Scenario Simulation:** Generates practice scenarios for AML officers to identify red flags.
* **Complex Mapping:** Connects "Placement, Layering, and Integration" stages to specific transaction types.

## 🔧 How to Use
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Add your regulatory PDFs to the `/data` folder.
4. Add your OpenAI API Key to the environment variables.
5. Run `python app.py` to start the research terminal.
