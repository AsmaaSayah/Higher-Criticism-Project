# ArXiv Data Acquisition & Preprocessing Pipeline

This repository contains a pipeline for fetching arXiv paper metadata and PDF content, focused on papers submitted in March of each year.

## Structure

- `arxiv_data.py`: Module containing functions to fetch and preprocess arXiv data.
- `data_acquisition.ipynb`: Notebook for running the data acquisition and exploring results.
- `requirements.txt`: List of dependencies.
- `README.md`: This documentation.

## Setup

1. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
