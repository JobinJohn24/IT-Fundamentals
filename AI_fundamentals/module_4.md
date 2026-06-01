# Neural Networks & Data

### Neural network learning

- a chain of mathematical transformations. 
- data -> numbers -> weighted connections across layers -> output.
- the networks predictions are compared to the correct answers (*loss function*)
- *backpropagation* - propagates the error backward through the network, and gradient descent applying to each weight to be pushed in the direction that would reduces errors.
- once this it done millions, and billions of times = a trained model

### Training v Inference

- Training is *expensive*, while the inference is *inexpensive*
- training are done once or periodically.
- running ChatGPT for 100M daily users is an inference problem.
- inference is *real-time calculation*

### Role of data quality

- The biggest bottleneck in production ML is almost never the algorithm, rather tha data quality, labeling consistency & distribution shift. (e.g. world changes but your training data doesn't)
- *distribution shift* - gap between training data & real-world data AT deployment.

### Learning Machine Learning

[Machine Learning Course - *Kaggle*](https://www.kaggle.com/learn/intro-to-machine-learning)

*Machine Learning Course Notes*

- Objective: training a decision tree on housing data - tangible, tactile way to feel backpropagation's output.

![alt text](<Screenshot 2026-05-20 at 12.35.29 PM.png>)

- Building a model
  1. define - the type of model, parameters of the model types are specifed.
  2. fit - capturing patterns from the data
  3. predicting - predicting based on the patterns.
  4. validating - determining how accurate the model's predictions.

## Under & over fitting

- Fine-tuning the model for better performance.

*Overfitting:*

  1. the model matches the training data, fails the validation.
  2. high training and testing error.
  3. poor performance because the learning of the underlying trend hasn't been done.
  4. e.g. making strong assumptions about the distribution of data.

*Fixing Underfitting:*

1. increasing the model complexity - more flexible algorithm.
2. feature engineering - more relevant input features for the model to have more contextual signals.
3. reduce regularization - strong regularization forces parameters toward zero, and it oversimplies the model

*Underfitting:*

  1. model's performance is too complex & flexible.
  2. since the model has too many parameters, it's decision boundary is twisted.
  3. low training error & high testing/validation errors
  4. e.g. memorization rather than comprehension/ conceptual understanding.

*Fixing Overfitting:*

1. adding regularization - provide penalties to shrink large weights or add dropout layers, which disables random neurons during training.
   a. shrinking large weights = `$$\text{Total Loss} = \text{Prediction Error} + \lambda \sum (w^2)$$`
   b. adding dropout layers disables some neurons, which forces the network to learn independent, robust features without memorizing noisy details.
2. increasing training data - providing the model more examples, and more data that dilutes the impact of outliers & random noise.
3. simplify the model - reduce features, simpilier algorithm architecture.
4. early stopping - immediately stopping the moment the validation error starts rising.

### CNNs - Convolutional Neural Networks

- an algorithm that recognizes patterns in data.

- the building blocks of a CNN:

  1. Tensor - n-dimensional matrix 
  2. Neuron - function that takes multiple inputs & yields a single response. Visual representation = *activation maps*
  3. Layer - collection of neurons with the same operations and hyperparamaeters
  4. Kernal Weighted & Biases:
   a. Kernel weights = what pattern the filter looks for
   b. Bias = how easily the filter fires
   c. Activation function = whether/how strongly the signal passes forward 
  5. Differentiable score function - any mathematical operation that takes a input tensor, calculates a scalar score & allows a gradient to flow backward.

- e.g. for image recognition
- a image converts to a meatrix of numbers.
- converting it into a single vector rather than a matrix. *This will compress the localized visual features into unified format by three factors:*
  1. reshaping 2D feature maps into 1D format.
  2. strips away spatial boundaries (good for cross referencing)
  3. shrinks every grid of single pixel scores into a tight summary.


### Case Study

- tesla auto-pilot is trained on 'fleet learning.'
- The is billions of miles of driving data collected across customer vehicles.
  1. edge cases are flagged, labeled, and used to train the model.
  2. The closed loop between inference [driving] & training [learning] with weekly improvements.