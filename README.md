# Week 9: GenAI Domain Assistant (Project 3 - Part 1)

## Project Overview

This project was completed as part of **Week 9 Lab: GenAI Domain Assistant**.

The objective of this lab was to build an AI-powered chatbot using a Generative AI API, understand conversational AI development, and create domain-specific assistants using prompt engineering.

Originally, the lab required OpenAI API integration. Due to API credit limitations, this project was successfully implemented using **Google Gemini API** in **Kaggle Notebook**, while fulfilling all required chatbot functionalities.

---

# Lab Objectives

The main goals of this project were:

- Create and configure an AI API account
- Make the first successful API call
- Build a conversational chatbot
- Handle multi-turn conversation history
- Customize chatbot behavior using system prompts
- Create domain-specific assistants
- Understand prompt engineering techniques

---

# Technologies Used

- **Python**
- **Kaggle Notebook**
- **Google Gemini API**
- **google-generativeai library**
- **GitHub**

---

# Project Tasks

---

## Part 1: First API Call

In this step, the Gemini API was configured and tested successfully.

### Installation

```bash
pip install google-generativeai
```

### API Configuration

```python
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel("gemini-2.5-flash")
```

### First API Request

```python
response = model.generate_content(
    "Say hello and introduce yourself!"
)

print(response.text)
```

### Outcome

- API connection established successfully
- AI-generated response received
- Environment configured properly

---

## Part 2: Basic Chatbot Development

A conversational chatbot was created that can interact with users continuously.

### Features Implemented

- Accept user input
- Send prompts to Gemini API
- Generate chatbot responses
- Maintain conversation memory
- Exit chatbot using `quit`

### Chatbot Code

```python
chat_session = model.start_chat(history=[])

print("Chatbot ready! Type 'quit' to exit.")

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        print("Goodbye!")
        break

    response = chat_session.send_message(user_input)

    print("Assistant:", response.text)
```

### Example Interaction

```text
You: Hello
Assistant: Hello! How can I assist you today?

You: What can you do?
Assistant: I can answer questions, provide information, and help solve problems.
```

---

## Part 2.2: System Prompt Customization

System prompts were used to define chatbot personality and behavior.

### Example Prompt

```python
system_prompt = """
You are a helpful assistant.
Be friendly, concise, and professional.
If you don't know something, say so.
"""
```

### Benefits

- Controlled chatbot tone
- Improved response consistency
- Customized assistant behavior

---

# Part 3: Domain-Specific Assistants

Two specialized assistants were developed.

---

## 1. HR Assistant

An HR chatbot was created for a technology company.

### Company Policies

- Vacation: **15 days per year**
- Sick leave: **Unlimited (manager approval)**
- Remote work: **3 days per week**
- Health insurance: **Fully covered**
- 401(k) matching: **Up to 5%**

### HR Assistant Code

```python
hr_prompt = """
You are an HR assistant for a technology company.

Company policies:
- Vacation: 15 days per year
- Sick leave: Unlimited
- Remote work: 3 days per week
- Health insurance: Fully covered
- 401(k) matching: Up to 5%

Answer employee questions clearly and briefly.
"""
```

### Example Questions

- How many vacation days do I get?
- Can I work remotely?
- What is the health insurance policy?
- How does 401(k) matching work?

---

## 2. Customer Support Bot

A customer support chatbot was created for an electronics retailer.

### Store Policies

- Returns: **30-day return policy**
- Shipping: **Free over $50**
- Warranty: **1 year manufacturer warranty**
- Support hours: **9 AM – 6 PM EST**

### Support Bot Code

```python
support_prompt = """
You are a customer support agent for TechShop.

Policies:
- Returns: 30-day return policy
- Shipping: Free over $50
- Warranty: 1 year manufacturer warranty

Be empathetic and solution-focused.
"""
```

### Example Questions

- I want to return a product.
- How much is shipping?
- My laptop stopped working.

---

# Project Deliverables Completed

✅ API setup completed  
✅ First successful API call  
✅ Basic chatbot implemented  
✅ Multi-turn conversation maintained  
✅ System prompt customization completed  
✅ HR assistant developed  
✅ Customer support bot developed  
✅ Tested with multiple questions  
✅ Code uploaded to GitHub  

---

# How to Run the Project

## Step 1: Open Kaggle Notebook

Create a new notebook in Kaggle.

---

## Step 2: Install dependencies

```bash
pip install google-generativeai
```

---

## Step 3: Add API key

```python
genai.configure(api_key="YOUR_API_KEY")
```

---

## Step 4: Run notebook cells

Execute all cells in order.

---

## Step 5: Interact with chatbot

Type questions and receive AI responses.

---

# Learning Outcomes

This lab helped build practical experience in:

- Generative AI API integration
- Prompt engineering
- Chatbot development
- Conversation memory handling
- Domain-specific assistant design
- Real-world AI application development

---

# Challenges Faced

During the project:

- OpenAI API quota limitations were encountered.
- Gemini API was used as an alternative.
- Model compatibility issues were resolved.
- Kaggle internet settings were configured.

These challenges helped improve debugging and problem-solving skills.

---

# Future Improvements

Possible enhancements include:

- Web-based chatbot interface
- Document-based Q&A using RAG
- Voice interaction
- Database integration
- Deployment as a web app

---

# Author

**Anderis Nisar**

Course Lab – Week 9  
GenAI Domain Assistant Project  
