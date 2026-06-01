# Enteprise AI

### AI in Healthcare, Finance, & Marketing

- AI is changing *diagnostic*, *drug discovery*, *clinical operations*
    1. diagnostics - pathology AI, which has the ability to read slides that match fellowship-trained pathologists.
    2. drug discovery - identifies specific drugs becomes easier.
    3. clinical operations - e.g. ambient AI listens to patient encounters and auto-generates SOAP notes, which saves physicians 2+ hours daily.

- AI in finance
    1. the use of quantitative ML models have been made for decades.
    2. e.g. JPMorgan's LOXM executes equity trades using RL. 
    3. Fraud detection ML models flag anomalous transactions in miliseconds
    4. LLM's are used to summarize earnings call transcripts.
    5. Extracting covenant violations from legal documents
    6. Automating regulatory reporting
    7. AI in finance spends roughly $20B+ annually

### Calculating AI ROI

- `(time saved * hourly rate + revenue gained - AI cost) / AI cost`
- e.g. a 10-person team that spend 2 hr/day on manual reporting, at $75/hr average = $109/year in labor
*VS*
- e.g. Automating 80% at $12/year  = ROI of 727%

- Calculates actual time displacement *NOT productivity gains*
- USEFUL: when building this calculation before an AI implementation.

### Case Study - Documentation

1. The role of AI in hospitals & clinics: Transforming healthcare in the 21st century

- challenges face:
  a. rising costs
  b. limited access
  c. growing demand
- objectives: 
  • reviewing how AI transformed healthcare domains
  • challenges
  • possible solutions
- AI changes `clinical decision-making`, `hospital operations`, `medical diagnostics`, `patient care`, `ethical considerations`
- changes in clinical settings: assists in diagnosing diseases, predicting patient outcomes, & personalizing treatment plans. 
- hospital management operations: optimizing operational efficiency, streamlining admin tasks, improving patient flow & scheduling.
- 

![alt text](<Screenshot 2026-05-21 at 9.25.16 PM.png>)
*overview of AI's role in healthcare across sections*

- AI in clincial decision-making
  1. AI algorithms for diagnosis & prognosis
  2. case studies of AI in diasease detection
  3. AI's role in personalized medicine

1. AI Algorithms:
- for managing chronic and complex diseases, predictive accuracy & diagnostic precision can be *crucial*
- AI in prognosis:
  a. AI forecasts potential complications, use healthcare professional to devise preemptive strategies.
  b. e.g. for diabetes; AI can predict potential risks through analyzing blood sugar levels, lifestyle factors, and treatment responses.
  
    1. Applied Algorithms:
        a. `machine learning` - learning from data to make predictions or decisions. Supervised ML are used for patient outcomes based on historical data. While unsupervised learning are used for identifing patterns or clusters within data. Reinforcement learning is learning to make sequences of decisions through trial & error, which is useful for personalised treatment optimization.
        b. `deep learning` - CNNs are used for intepreting and processing imaging data for diagnosing diseases through X-ray / MRIs. ResNet, VGG, & GCNs are used for image analysis, classification, & graph data processing (modeling relationships between patients, symptoms, genes, diseases, medications, hospitals, or outcomes.) RNN's are known for handling sequential data (time-series data = physiological signals during patient monitoring, predicting health deteriorations or outcomes over time.) Transformer models help power GPT, or BERT which helps enable more accurate patient information, and processing NL in clinical notes. GNNs used for prediction protein interactions to understand disease pathways. GNNs are used for creating synthetic medical images for training *without* have privacy concerns.
        c. `NLP` - extracting meaningful information from clinical notes and/or research literature.
