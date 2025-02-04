# DeepSeek Code Companion 🧠🚀

## Your AI Pair Programmer with Debugging Superpowers

This Streamlit application is your personal AI coding assistant, powered by the DeepSeek language model. It leverages [Ollama](https://ollama.ai/) to run the model locally and [LangChain](https://python.langchain.com/) to orchestrate the interactions.  Think of it as having an expert AI pair programmer right beside you, ready to help with your coding challenges!

![DeepSeek Code Companion Screenshot](placeholder-screenshot.png) <!-- Replace with actual screenshot if you have one -->

### ✨ Key Features

*   **🐍 Python Expert:**  Get assistance with Python code, from basic syntax to complex algorithms.
*   **🐞 Debugging Assistant:**  Stuck on a bug? DeepSeek can help you identify and fix errors with strategic debugging advice.
*   **📝 Code Documentation:**  Need to document your code?  Let DeepSeek generate clear and concise documentation.
*   **💡 Solution Design:**  Brainstorming a new feature or project? DeepSeek can assist with solution design and architectural ideas.
*   **Concise and Correct Solutions:**  Designed to provide accurate and to-the-point code suggestions.
*   **Debugging Focus:**  Emphasizes the importance of strategic `print` statements for effective debugging.
*   **Local and Private:** Runs locally using Ollama, ensuring your code and queries remain private.
*   **Model Selection:** Choose between different DeepSeek models (like `deepseek-r1:1.5b` and `deepseek-r1:7b`) to balance performance and resource usage.

### 🛠️ Technology Stack

*   **[Streamlit](https://streamlit.io/):**  For building the interactive web application interface.
*   **[Ollama](https://ollama.ai/):**  To locally run and manage the DeepSeek language models.
*   **[LangChain](https://python.langchain.com/):**  A framework for developing applications powered by language models, used here for prompt management and model interaction.
*   **[DeepSeek Models](https://deepseek.com/):**  Powerful language models known for their coding capabilities.

### 🚀 Getting Started

Follow these steps to get your DeepSeek Code Companion up and running:

**1. Prerequisites:**

*   **[Ollama Installed](https://ollama.ai/download):** You need to have Ollama installed and running on your system. Ollama is what allows you to run language models locally.
*   **DeepSeek Models Pulled:**  Before running the application, you need to pull the DeepSeek models you want to use with Ollama. Open your terminal and run the following commands for the models available in the application (you can choose one or both):
    ```bash
    ollama pull deepseek-r1:1.5b
    ollama pull deepseek-r1:7b
    ```
    (This will download the models if you don't have them already.)
*   **Python 3.7+:** Ensure you have Python 3.7 or a later version installed on your system.
*   **Python Libraries:** Install the required Python libraries using pip:
    ```bash
    pip install streamlit langchain-ollama langchain-core
    ```

**2. Run the Application:**

1.  **Save the Code:** Save the provided Python code as a file named `app.py` (or any name you prefer with the `.py` extension).
2.  **Open your Terminal:** Navigate to the directory where you saved `app.py` in your terminal.
3.  **Run Streamlit:** Execute the following command in your terminal:
    ```bash
    streamlit run app.py
    ```
4.  **Access in Browser:** Streamlit will automatically open your web browser and load the DeepSeek Code Companion application. If it doesn't open automatically, it will provide a URL in the terminal (usually `http://localhost:8501`) that you can manually open in your browser.

**3. Using the Application:**

1.  **Model Selection:** In the sidebar on the left, you can choose the DeepSeek model you want to use from the "Choose Model" dropdown. `deepseek-r1:7b` is generally more powerful but may require more resources, while `deepseek-r1:1.5b` is lighter and faster.
2.  **Ask Your Coding Question:** In the chat input box at the bottom of the application, type your coding question or request.
3.  **Get AI Assistance:** Press Enter or click the send button. The application will process your query using the selected DeepSeek model and display the AI's response in the chat window.
4.  **Iterate and Refine:**  Continue the conversation, asking follow-up questions or providing more context to refine the AI's responses and get the best coding assistance.

### ⚙️ Configuration Options (Sidebar)

*   **Choose Model:**  Select the DeepSeek model you want to use for code generation and assistance. The available options are:
    *   `deepseek-r1:1.5b`: A smaller, faster model, suitable for less resource-intensive tasks.
    *   `deepseek-r1:7b`: A larger, more capable model, providing potentially better results but requiring more resources.

### 🎨 Customization

*   **Model Temperature:** You can adjust the `temperature` parameter in the `llm_engine` initialization in the code to control the randomness of the model's output. A lower temperature (e.g., 0.1) makes the output more focused and deterministic, while a higher temperature (e.g., 0.7) makes it more creative and potentially less predictable.
*   **System Prompt:**  Modify the `system_prompt` template to change the persona and instructions given to the AI. You can tailor it to specific coding domains or preferences.
*   **Styling:**  The `st.markdown` block with `<style>` tags at the beginning of the code defines the custom CSS for the application. You can modify this CSS to change the look and feel of the interface.

### 📝 Example Use Cases

*   **"How can I write a Python function to reverse a string?"** - Get a Python function with debugging print statements to reverse a string.
*   **"Debug this Python code: ```python ... ```"** - Paste your code snippet and ask DeepSeek to help you find and fix errors.
*   **"Write documentation for this Python class: ```python ... ```"** - Generate clear documentation for your Python classes or functions.
*   **"Suggest a Python library for data visualization."** - Get recommendations for relevant Python libraries based on your needs.
*   **"Explain the concept of decorators in Python with a simple example."** - Learn about Python concepts with clear explanations and examples.

### 🤝 Contributions

Contributions to improve this DeepSeek Code Companion are welcome! Feel free to fork the repository, make your changes, and submit a pull request.

 

---

**Enjoy coding with your DeepSeek AI Companion! 🚀**