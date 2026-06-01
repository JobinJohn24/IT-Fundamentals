# AI Agents

### AI Agents

- a LLM given tools and autonomy to use in sequential order to complete a goal.
- Agents: search the web -> running scripts -> read files -> write code -> check output -> and iterate.
- Components of an AI Agent:
  1. LLM with a backbone
  2. set of tools
  3. memory mechanism 
  4. planning loop

### Custom GPTs for Personal Workflows

- GPT builder lets you create specialized assistant with custom instructions, knowledge base and connected tools.
- e.g. a custom GPT for conducting bioinformatics research.
    • deep context domain
    • preferred formats
    • institutions citation-style
- this can reduce research queries from multi-step prompt to a single setence.

### Local Models with Ollama

- Ollama allows users to run open-source LLMs entirely on your own machine.
    *no internet needed, no API costs, full data privacy.*

- Running `ollama run llama3` in the terminal and you're chatting with a locally-hosted 8B parameter model + `AnythingLLM` for a local RAG pipeline over your own documents.
    *critical for working with sensitive clinical or research data that don't leave your machine*

### Use Cases of Personal AI Agents

- `Devin` demonstrated agent completing end-to-end software engineering task:
  1. reading github isses
  2. exploring codebases
  3. writing a fix
  4. running unit tests
  5. openning pull requests

### Building custom GPT for academic or research domains

- using `AnythingLLM` for creating local RAG pipelines over multiple documents.
- documenting purpose of the local model, where does it fall short versus claude.

