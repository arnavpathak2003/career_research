# Project Documentation: Crew AI Career Research & Analysis

This project is designed to perform in-depth research on career landscapes in India for a specified field. By orchestrating a series of specialized agents, the project:

- **Researches** career trends, compensation, educational requirements, and future outlook.
- **Extracts** relevant data from curated, high-quality websites.
- **Analyzes & Writes** a comprehensive career guide.
- **Manages Files** by saving the final content with rigorous verification.

The configuration for each agent and task is defined in the `agent.yaml` and `task.yaml` files provided with the project.

---

## Table of Contents

1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Environment Setup](#environment-setup)
4. [Installation Instructions](#installation-instructions)
5. [API Keys and .env Setup](#api-keys-and-env-setup)
6. [Additional Information](#additional-information)

---

## Overview

The project uses **Crew AI** to coordinate multiple agents with distinct roles:

- **Researcher Agent:**
  Conducts comprehensive career research, analyzing job market trends, compensation, education requirements, and future career prospects for the specified field. It also curates a list of high-quality websites for deeper insights.

- **Web Scraper Agent:**
  Extracts detailed career data (job listings, salary information, educational details, etc.) from the websites identified by the researcher.

- **Analyst & Writer Agent:**
  Analyzes the research data and produces a well-structured, actionable career guide with the following seven sections:

  1. Executive Summary
  2. Current Market Analysis
  3. Compensation Overview
  4. Education & Skill Requirements
  5. Future Outlook & AI Impact
  6. Strategic Recommendations
  7. Conclusion

- **File Manager Agent:**
  Saves the final markdown content as `articles/{field}.md` with rigorous file verification to ensure content persistence.

The tasks and goals for these agents are detailed in the YAML files.

---

## Prerequisites

Before setting up the environment, ensure you have the following:

- **Python:** Version 3.8 or higher.
- **Virtual Environment:** It is recommended to use a virtual environment to manage dependencies.
- **Pip:** For installing Python packages.
- **API Keys:**

  - **SERPER_API_KEY** (required for search-related functionality)
  - Optionally, **OpenAI** and **Gemini API** keys if you plan to integrate with these services.

- **Optional Tool:**
  - **Ollama** (if you wish to run the project locally with Ollama support).

## Environment Setup

Choose your preferred method to set up the development environment:

### Option 1: Using venv (Python's built-in virtual environment)

**Linux/Mac:**

```bash
# Create and activate virtual environment (Linux/Mac)
python3.11 -m venv venv
source venv/bin/activate
```

**Windows Command Prompt:**

```bash
# Create and activate virtual environment (Windows CMD)
python3.11 -m venv venv
venv\Scripts\activate.bat
```

**Windows PowerShell:**

```bash
# Create and activate virtual environment (Windows PowerShell)
python3.11 -m venv venv
venv\Scripts\Activate.ps1
```

### Option 2: Using Conda

```bash
# Create and activate conda environment
conda create -n crewai-env python=3.11.9
conda activate crewai-env
```

### Installing Required Packages

After activating your chosen environment, install the required packages:

```bash
# Install Crew AI with tools
pip install crewai[tools]
pip install crewai-tools
```

3. **Optional: Install Ollama**

   If you want to run the project locally using Ollama, download and install it from the official website:

   - [Ollama Website](https://ollama.com/)

  - This implementation uses Ollama by default with the Qwen 2.5 model for local execution. Download and install from the above website:
  
  - After installing Ollama, run this command to pull the required model:
    ```bash
    ollama pull qwen2.5
    ```

---

## Installation Instructions

After setting up your virtual environment and installing the necessary packages, follow these steps:

1. **Clone or Download the Project Repository**

   Ensure you have the project files, including `agent.yaml` and `task.yaml`.

2. **Install Additional Dependencies (if any)**

   If there are other dependencies mentioned in the project requirements, install them using pip.

3. **Configure the API Keys**

   Create a `.env` file in the root directory of your project (see the section below for details).

---

## API Keys and .env Setup

If you plan to use OpenAI or Gemini API services, you must create a `.env` file to store your API keys. Additionally, you will need a `SERPER_API_KEY`.

Create a `.env` file in your project root with the following structure:

```env
# .env file

# API key for OpenAI
OPENAI_API_KEY=your_openai_api_key_here

# API key for Gemini
GEMINI_API_KEY=your_gemini_api_key_here

# API key for SERPER
SERPER_API_KEY=your_serper_api_key_here
```

### Useful Links for API Services

- **OpenAI:** [https://openai.com/](https://openai.com/)
- **Gemini:** [https://ai.google/](https://ai.google/)
  _(Note: Gemini is an evolving offering by Google AI. Check the site for the latest details.)_
- **Ollama:** [https://ollama.com/](https://ollama.com/)

---

## Additional Information

- **Model Information:**
  This project's agent and task configurations were created using the **Qwen2.5** model.

- **Usage:**
  Customize the `{field}` variable in your YAML files to specify the career field you wish to analyze. Then, use the Crew AI CLI or your preferred method to run the tasks defined in the configuration files.

- **Logging & Verification:**
  The File Manager Agent ensures that the final markdown is saved with rigorous verification. Check the logs to confirm that `articles/{field}.md` exists and contains the expected content.
