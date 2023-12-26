# Codebasics Q&A: Empowering Learner Inquiry with AI

This project seeks to develop a revolutionary question-and-answer system for Codebasics, a leading e-learning platform specializing in data science and programming. With a large and active community of learners, Codebasics faces a constant stream of questions posed through various channels like Discord and email.

To streamline this process and offer an enhanced learning experience, I propose a cutting-edge Q&A system powered by Google's PaLM Language Model and Langchain's semantic search technology. The system will be hosted on a user-friendly Streamlit interface, providing learners with a convenient platform to pose their questions and access relevant answers.

## Key benefits:

Seamless knowledge search: Leverage the combined power of PaLM and Langchain to deliver accurate and insightful answers, even for complex or open-ended inquiries.
Improved accessibility: Offer a centralized Q&A hub accessible directly within the learning platform, eliminating the need for scattered communication channels.
Enhanced community engagement: Foster a collaborative learning environment where students can share knowledge, learn from each other, and contribute to a growing pool of valuable resources.
 
## This project, in essence, aims to:

Revolutionize Codebasics' learning experience by facilitating efficient knowledge acquisition and fostering a stronger, more engaged community.
Showcase the potential of cutting-edge AI and semantic search technologies in the context of e-learning, paving the way for innovative educational solutions.

## Project Overview

 This project develops a Q&A system for Codebasics, leveraging Google's PaLM Language Model and Langchain's semantic search. It aims to:

- Streamline learner support
- Enhance the learning experience
- Showcase cutting-edge AI in e-learning
 
 ## Key Features

- Real-world FAQ data: Utilizes a CSV file of actual Codebasics FAQs
- LLM-powered answers: Provides fast and accurate responses to diverse questions
- Streamlit UI: Offers a user-friendly interface for learners
- Semantic search: Employs Langchain for deep understanding of inquiries
- Text embeddings: Huggingface Instructor for efficient text representation
- Vector database: FAISS for fast retrieval of relevant answers
 
 ## Technical Highlights

- Langchain + Google PaLM: LLM-based Q&A
- Streamlit: UI framework
- Huggingface instructor embeddings: Text embeddings
- FAISS: Vector database
 
 ## Installation

1. Clone the repository:

```
git clone https://github.com/LokeshReddy09/CodeBasics-QA-LLM.git
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Get a Google API key and add it to .env:

```
GOOGLE_API_KEY="your_api_key_here"
```

 ## Usage

- Run the Streamlit app:

```
streamlit run main.py
```

- Create the knowledge base in the app (wait for completion).
- Ask questions in the provided box!

 ## Sample Questions

- Do you offer internships or EMI payments?
- Do you have a JavaScript course?
- Should I learn Power BI or Tableau?

 ## Project Structure

- main.py: Streamlit application script
- langchain_helper.py: Langchain code
- requirements.txt: Required Python packages
- env: Configuration file for Google API key
