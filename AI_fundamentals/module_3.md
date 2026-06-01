# Prompt Engineering

### zero-shot v few-shot processing

- zero-shot: a modle with no examples.
  1. relies primarily on training.
  2. e.g. classifying a review as positive or negative.
- few-shot: model with examples, then the model performs the real task.
  1. improves accuracy
  2. dependent on text pattern continuation.
  3. high edge case resilience
  4. large KV cache footprint, which limits parallel request batching limits.
  5. helps serve as a visual boundary that prevents the model from straying into a creative text generation.


### Use cases

- Zero-shot processing: high-volume customer support ticket triage.
  1. to handle high-volume support tickets, a automated routing layer reads incoming text from the widget and categorizes it into a specialized department tag. 
- few-shot processing: standardizing client-ready executive summaries.
  1. a consulting company would convert internal analyst notes, financial models, and interview transcripts into client-facing summaries.
  2. the summary will adhere to the firm's proprietry communication style, tone, headers and phrasing guidelines.

### Chain-of-Thought(CoT) prompting

- instructions for the model on how to generate its' own reasoning steps before displaying an answer.
- adding a reasoning chain or logic helps the model with externalize it's thinking.
- improves performance on math, logic, and multi-step reasoning.
- you're providing the model with a *thinking style* with examples.

### Use case

- automated B2B credit risk underwriting
  1. uses LLM agent to review business' growth data, multi-layered chargeback ratios, cash-reserve trajectories, and macro-economic industry risk signals
  2. provides computational tokens required processing the next variable, which would help prevent a financial miscalculation.

### System prompts & role definition

- a set of rules/instructions for the model to abide by in order to get a definitive answer.
- The prompts dictate the model's persona, scope, and behavioral constraints.

### Use case

- secure wealth management database interface
  1. e.g. a financial advisor at Morgan Stanley uses the company's internal AI tool to look up data.
  2. the system prompt acts a internal compliance office which is forced to abide by the company security policies, and safety guardrails.

*KV Caching*

- technique that reduces costs & latency.
- the computer's GPU calcualtes the mathematical representation of the system prompt *ONCE*, and locks them into memory (caches them), and appends a new user messages to it. 
- changing the system prompt would break the cache, and initiate the GPU to re-compute the sequence from scratch & increases the API latency & computational costs.


### Case study for constriants for an model

- *Stripe* uses engineered prompt in the API documentation AI assistant. 
- The system constriants the model to only answer Stripe-related questions.
- the production-grade prompt engineering prevents the hallucinated API response. Breaking the devs codebase.

### Anthropic Prompt Engineering Guide (API Documentation)

- the effort parameter allows for Claude's intelligence v token spend, trade off for faster speeds and lower costs.

* `max`: Max effort can deliver performance gains in some use cases, but may show diminishing returns from increased token usage. This setting can also sometimes be prone to overthinking. We recommend testing max effort for intelligence-demanding tasks.
* `xhigh` (new): Extra high effort is the best setting for most coding and agentic use cases.
* `high`: This setting balances token usage and intelligence. For most intelligence-sensitive use cases, we recommend a minimum of high effort.
* `medium`: Good for cost-sensitive use cases that need to reduce token usage while trading off intelligence.
* `low`: Reserve for short, scoped tasks and latency-sensitive workloads that are not intelligence-sensitive.

- adding context to improve performance
  1. providing context beyond instructions (e.g. why a certain behavior is important.)
  2. good for providing a more targeted response.

- less tool use to enhance the use of reasoning more.
  1. adjustments to tool use can be made through explicitly instructing the model when and how to properly use its tools. 
  2. when claude is rushed (low effort), then the model will spew a answer from memory rather than reasoning, and *higher mistakes*