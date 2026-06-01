# Brief History

### AI v ML v Deep Learning

- AI - making machines *smart*
- ML - machines learning from data (with no rules)
- Deep Learning - layered neural networks that find patterns 

### Learning Methods

- Supervised learning - teaching with examples (e.g. spam/no spam)
- Unsupervised learning - finding hidden patterns with no label (e.g. customer segmentation)
- Reinforcement learning - learning by trial & error, and reward signals. (e.g. alphago & chatgpt)

### Neural Networks 

[TensorFlow Playground](https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=circle&regDataset=reg-plane&learningRate=0.03&regularizationRate=0&noise=0&networkShape=4,2&seed=0.21838&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false)

*A intutitive and visual representation of what, how, and why neural network work.*

- Neural network have:
  1. neurons that are connected and created together, which are a collection of software neurons. 
  2. the network is asked to solve a problem.
  3. attempts to solve the problem multiple times.
  4. this strengthens the connection and leads to less failure & more success.

### Neural Network use cases

- Used in image, & speech recognition, and natural language processing.

![alt text](<Screenshot 2026-05-19 at 6.47.37 PM.png>)

*A visual representation of how output layer are displayed through multiple hidden layers to make predictions from the input layer*

- input layers are features or information that the model uses.
- the lines represent the amount of connection to the many neurons in the next layer. *the lines represent weights, which represent the significance of the input layer*
- hidden layers provide a way for the model to perform pattern recognition behind the scenes.
- output layer represents the models final predictions based on the information that was given as input layers, the connections, and the hidden layers peforming pattern recognition.

### Real Use Case

- Supervised ML system - netflix's recommendation system which helps using trained data from watch events, ratings, and dwell times. 
- It saved netflix $1B /Year in potential churn prevention
- *churn - customer usage stopped*
- e.g. Active Netflix user → cancels subscription → churned user
