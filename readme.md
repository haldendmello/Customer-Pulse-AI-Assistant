# Personalized Financial Assistant

This project is a personalized financial assistant that leverages customer segmentation, anomaly detection, and churn prediction to offer tailored financial insights, product recommendations, and spending advice. The assistant helps improve customer retention, engagement, and satisfaction by providing relevant information and proactive suggestions.

## Project Structure
```
code.md
embed_data_from_pickle.py
embed_data.py
embed_jsonl_data.py
llama_inference.py
main.py
package.json
pinecone_setup.py
query_bot.py
readme.md
static/
    css/
        style.css
    index.html
testdata.jsonl
user_interface.py
```


## How to Run the Project

### Prerequisites

- Python 3.x
- Flask
- Requests
- Pinecone
- Joblib
- Pandas
- Scikit-learn

### Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/financial-assistant.git
    cd financial-assistant
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Set up the Pinecone index:
    ```python
    from pinecone_setup import initialize_pinecone
    initialize_pinecone()
    ```

4. Run the Flask server:
    ```sh
    python main.py
    ```

5. Open `static/index.html` in a web browser to interact with the chatbot interface.

### Usage

- **Chatbot Interface**: Interact with the chatbot through the web interface. Type a message and receive responses from the personalized financial assistant.
- **Embedding Data**: Use the scripts `embed_data_from_pickle.py`, `embed_data.py`, and `embed_jsonl_data.py` to generate embeddings and store them in Pinecone.


### For More Detail about Project Achitecture [click here](project.md)
