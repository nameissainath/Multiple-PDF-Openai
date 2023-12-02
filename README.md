# 📄 PDF Uploader & Analyzer: GPT Powered 🤖🔍

This Streamlit application allows users to upload PDF documents and ask questions about the content. It uses GPT (Generative Pre-trained Transformer) powered by OpenAI for analyzing and responding to queries based on the uploaded PDFs.

## Features

- **PDF Upload:** Users can upload multiple PDF files for analysis.
- **Text Extraction:** Extracts text from uploaded PDFs.
- **GPT-4 Integration:** Leverages GPT-4 to understand and respond to user queries about the PDF content.
- **Conversational Interface:** Provides an interactive chat interface for users to ask questions.


# How It Works

## Overview of the MultiPDF Chat App Process

The MultiPDF Chat App operates through a series of steps to deliver accurate responses to user queries:

### 1. **PDF Loading**
   - The app begins by loading multiple PDF documents.
   - It then extracts the text content from these documents for further processing.

### 2. **Text Chunking**
   - The extracted text undergoes a chunking process.
   - This involves breaking down the text into smaller, manageable chunks, optimizing them for efficient processing.

### 3. **Language Model Integration**
   - The application leverages an advanced language model.
   - This model is used to create vector representations, also known as embeddings, of the text chunks. These embeddings capture the semantic essence of the text.

### 4. **Similarity Matching**
   - Upon receiving a user query, the app employs similarity matching techniques.
   - It compares the query against the embeddings of the text chunks to find the ones with the highest semantic similarity.

### 5. **Response Generation**
   - The most relevant text chunks are selected based on the similarity match.
   - These chunks are fed back into the language model.
   - The model then generates a comprehensive response, drawing on the pertinent information from the PDFs.



## Installation

To set up and run this application, follow these steps:

### Prerequisites

- Python 3.7 or higher
- An OpenAI API key (for GPT-4 access)

### Setup

 **Clone the Repository**
   ```bash
   git clone https://github.com/your-github-username/your-repo-name.git
   cd your-repo-name


# MultiPDF Chat App

## Installation

Before using the MultiPDF Chat App, ensure you have completed the following steps:

1. **Install Dependencies**: Make sure all required dependencies are installed on your system.
2. **API Key Configuration**: Enter your OpenAI API key in the UI.

## Running the App

To run the MultiPDF Chat App, follow these steps:

1. **Start the App**: Open your terminal and run the app using Streamlit. Use the following command:
2. **Accessing the App**: The app will automatically launch in your default web browser, displaying the user interface.

## Usage

Once the app is running:

1. **Load PDFs**: Follow the instructions in the app to load multiple PDF documents.
2. **Chat Interface**: Use the chat interface to ask questions in natural language about the content of the loaded PDFs.


