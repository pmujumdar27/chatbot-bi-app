# chatbot-customer-touchpoint-app

**Note:** This project was done as a part of ```MS 491-III``` course at IITGN. The deployment is only for demonstration purpose. This deployment might be vulnerable to cyber attacks.

This Repository is for the **BI Server** mentioned in the Architecture.

---

## Problem Statement

<p align="center">
  <img width="600" src="https://github.com/pmujumdar27/chatbot-bi-app/blob/main/static/question.PNG">
</p>

---

## Proposed Solution

The ChatBot for FAQ is built using [DialogFlow](https://dialogflow.cloud.google.com). The [KnowledgeBase](https://cloud.google.com/dialogflow/es/docs/how/knowledge-bases) API is used to pass the ChatBot model with a library of FAQ's, based on which it generates the responses.

---

## Architecture

<p align="center">
  <img width="600" src="https://github.com/pmujumdar27/chatbot-bi-app/blob/main/static/architecture.PNG">
</p>

- The customer interacts with the Chatbot through the Customer-touchpoint website.
- The request received at the Customer-touchpoint website is then sent to our DialogFlow model, which generates a response
- The DialogFlow deployment has a webhook which calls back the address of our BI server, and the question asked to the chatbot is logged there in the database.
- The data can then be used by the **Sales and Service** team to get insights of what questions are asked by the cuesomers frequently and update the FAQ's in the chatbot deployment.

---
