### How LLMs Work

### Tokenization

- Tokens represent a chunk of text
- 0.75 on average 
- e.g. 'Artifical Intelligence' - 3 tokens = 'art', 'ifical' & 'intelligence'
- *context window* - each model (ChatGPT, Gemini, Claude, etc) have a limit on the amount of tokens being rendered on the model.

### Transformers

- Transformers help the model predict what the model should say based on understanding context from the entire query or prompt.
- The context-sensitivity is what makes LLMs better than RNNs
- *RNNs* - processes words strictly in sequential order & 'forgot' distant context.

### LLMs generating tokens

- prompt -> probablility distribution over entire vocabulary -> smaples next token.
- next token predictor is what a list of possible next tokens based on what the model sees.
- the list of probabilities add up to 100%. 

*Mathematical Concept*
1. the prompt turns to numbers.
2. model processes the numbers through layers.
3. scores are produced based on every token in the vocabulary. 
4. these scores are called *logits*.
5. logits are converted into probabilities using softmax.

`z_i = raw score for token i`
`V = total vocabulary size`
`P(t_i) = probability of token i being next`

### LLMs v RNNs

- Recurrent neural networks provide a different engineering layout, while large language models provides a transformer architecture, which  treats texts while every word is analyzed.
- RNNs struggle to analyze massive datasets because of the sequential training bottleneck.
- RNNs provide a *vanishing gradient problem* that's a mathematical signal fading away over long distances.
- LLMs provides self-attention, which is that every single token maintains a connection to every to every other token in the sequence. The signal never degrades. 

### Preventing highest-probabilty tokens

- *greedy decoding* - text generation strategy where the model selects the highest predicted probability at the current step.
- *sampling* - provides randomness rather than the greedy decoding. 
  1. sampling provides distribution to the selected tokens
  2. this can also lead to more 'hallucinations'

### Factors that dictate the next word/token

1. Temperature cooling
   a. low temperature - most likely word pushed near 100%. This is *greedy ecoding*
   b. high temperature (above 1.0) - the top choice will lose it's dominant lead. Most creative answer but can lead to more hallucinations.
2. Top-k / setting a fixed choice limit
   a. when a fixed number is selected, the model sorts all words from highest to lowest.
   b. keep the fixed number amount of choices.
   c. recalculates the percentages from the fixed number choices. Ensuring low-probability, and bizzare answers.
3. Top-k / setting a flexible choice limit
   a. a target cumulative percentage is selected rather than a fixed choice limit. 
   b. sorts the list from highest to lowest.
   c. there are options of decisions:
        >> if the model is certain then the model will hold the majority of the target cumulative percentages, and cuts off remaining choices.
        >> if the model is uncertain, the model will keep adding words until the desired target cumulative sum is calculated.

### Open-source tokenizer

- [visual of a LLM processing text as tokens](https://platform.openai.com/tokenizer)