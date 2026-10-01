---
key: machine_learning
title: "Machine Learning"
program: data_science
course_level: 3
dna16: "0701201872457019"
l4_address: "S6:P999505942"
chain256_anchor: "1706310553031512152732450248374901719952698437490493408533537708044976796739545904380085767537491499861558693749178818194367488718232991380908081046574425103749065570657869374902364442128057000363280649565153075053470618374908644939812737491528911143404423"
updated_at: "2026-10-01T20:00:00.000Z"
license: All-Rights-Reserved (Sales King Academy LLC)
source: Sales King Academy knowledge base (ska_knowledge)
---

# Machine Learning

> The course assumes foundational knowledge and teaches applied practice of machine learning concepts and techniques.

## Supervised

Classification (logistic regression, SVM, decision trees, random forest, k-NN) and regression (linear, polynomial, ridge/lasso). Train/validation/test split. Cross-validation. Bias-variance tradeoff. UNSUPERVISED: Clustering (k-means, hierarchical, DBSCAN), dimensionality reduction (PCA, t-SNE, UMAP), anomaly detection. NEURAL NETWORKS: Perceptron, multilayer feedforward. Activation functions: sigmoid, tanh, ReLU, softmax. Backpropagation via chain rule. Optimizers: SGD, Adam, RMSProp. Batch normalization, dropout. DEEP LEARNING: CNNs (convolution, pooling, feature maps — image recognition). RNNs, LSTMs, GRUs (sequential data). Transformers (attention mechanism — self-attention, multi-head). BERT, GPT architecture. EVALUATION: Accuracy, precision, recall, F1. ROC/AUC. Confusion matrix. Loss functions: MSE, cross-entropy, hinge. REINFORCEMENT LEARNING: Agent, environment, state, action, reward. Q-learning, policy gradient, actor-critic. Markov decision processes.

## Foundations

In computer science, Machine Learning (ML) refers to a subset of Artificial Intelligence (AI) that involves the development of algorithms and statistical models to enable machines to perform tasks without explicit instruction. A **model** is a mathematical representation of a system, process, or relationship, learned from **data**, which is a collection of observations, measurements, or examples. **Learning** is the process of improving the model's performance on a task through experience, where **experience** is the process of receiving and processing data. 
**Supervised Learning** involves training a model on labeled data, where each example is associated with a target output, to predict outputs for new, unseen data. **Unsupervised Learning** involves training a model on unlabeled data to discover patterns, relationships, or groupings. **Features** are individual characteristics or attributes of the data used to train a model, while **targets** are the desired outputs or responses. A **hypothesis** is a predicted output or classification made by a model, and **inference** is the process of using a trained model to make predictions on new data. **Overfitting** occurs when a model is too complex and performs well on training data but poorly on new data, while **underfitting** occurs when a model is too simple and fails to capture the underlying patterns in the data. **Generalization** refers to a model's ability to perform well on new, unseen data. **Features** are individual attributes or characteristics of the data, used as inputs to the model. A **hypothesis space** is the set of all possible models that can be learned from the data. Understanding these core concepts is essential for a practitioner to design, implement, and evaluate machine learning systems.

## Mechanisms

Machine learning operates through a series of interconnected steps, starting with data collection. The causal chain begins with the gathering of a dataset relevant to the problem the machine learning model aims to solve. This dataset is then preprocessed to ensure it is in a suitable format for the algorithm, which may involve cleaning the data to remove or correct errors, transforming the data into appropriate types, and possibly reducing the dimensionality of the data to make it more manageable. The causal chain begins with the gathering of a dataset relevant to the problem being addressed. This dataset is then preprocessed to ensure it is in a suitable format for the algorithm, which may involve cleaning the data to remove or correct errors, transforming the data into appropriate formats, and potentially reducing the dimensionality of the data to improve computational efficiency.

The preprocessed data is then split into training and testing sets. The training set is used to train the model, where the algorithm learns patterns and relationships within the data. The choice of algorithm depends on the type of problem (supervised, unsupervised, or reinforcement learning) and the nature of the data. For supervised learning, the algorithm learns to map inputs to outputs based on labeled examples. In unsupervised learning, the algorithm identifies patterns or structure in unlabeled data. Reinforcement learning involves an agent learning to take actions in an environment to maximize a reward.

Once the model is trained, it is evaluated using the testing set to assess its performance. This evaluation provides metrics on how well the model generalizes to unseen data, which is crucial for determining its effectiveness and potential for overfitting or underfitting. Overfitting occurs when a model is too closely fit to the training data and fails to generalize well to new data. Underfitting happens when a model is too simple to capture the underlying patterns in the training data. This step is crucial for understanding how well the model generalizes to new, unseen situations. Metrics such as accuracy for classification problems or mean squared error for regression problems are used to evaluate the model's performance.

The core of the machine learning mechanism is the algorithm used for training. Common algorithms include decision trees, random forests, support vector machines, and neural networks. Each algorithm has its strengths and weaknesses and is suited to different types of problems. For example, neural networks are particularly effective for complex, high-dimensional data and have been instrumental in advances in image and speech recognition.

The choice of algorithm and the specific implementation details can significantly impact the model's performance. Hyperparameters, which are parameters set before training the model, such as learning rate and regularization strength, must be tuned to optimize the model's performance. This tuning can be done manually or through automated processes, such as grid search or cross-validation.

Ultimately, the goal of machine learning is to enable computers to make predictions or take actions based on data without being explicitly programmed for each scenario. By leveraging patterns in data, machine learning models can learn to recognize images, understand natural language, make recommendations, and more, underpinning many of the intelligent systems that are increasingly pervasive in modern life.

The choice of model is critical and depends on the nature of the problem. For classification problems, models like logistic regression, decision trees, or support vector machines might be used. For regression problems, linear regression or more complex models like neural networks could be employed. The model learns from the training data by identifying patterns or relationships between the input data and the target variable.

The final step involves deploying the trained model in the desired application, where it can make predictions or take actions based on new, input data. Throughout this process, the model may also undergo updates or retraining as new data becomes available, allowing it to adapt to changing conditions or improve its performance over time. This iterative process of data collection, model training, evaluation, and deployment forms the core mechanism of machine learning in computer science.

The final step involves deploying the model in the appropriate application, where it can make predictions, classify new data, or take actions based on the patterns and relationships it has learned. Continuous monitoring and potential retraining with new data can help maintain or improve the model's performance over time. Throughout this process, the choice of algorithm, the quality of the data, and the computational resources available play critical roles in determining the success of the machine learning endeavor.

## Methods And Frameworks

Machine learning encompasses various methods and frameworks, each suited for specific problem domains. 
1. **Supervised Learning**: used when labeled training data is available, e.g., linear regression, logistic regression, decision trees, and support vector machines (SVMs). 
2. **Unsupervised Learning**: applied when unlabeled data is used, such as k-means clustering and principal component analysis (PCA). 
3. **Reinforcement Learning**: employed in sequential decision-making problems, like Q-learning and SARSA. 
Key models include **Neural Networks**, which are effective for complex, high-dimensional data, and **Gradient Boosting**, suitable for handling large datasets with multiple features. 
Formulas like **Bayes' Theorem** and **Entropy** are fundamental in probabilistic modeling and decision-making. 
Failure modes include **overfitting**, where models are too complex, and **underfitting**, where models are too simple, as well as **bias-variance tradeoff**, which affects model generalizability. 
Understanding these methods, models, and formulas is crucial for selecting the appropriate approach for a given problem and avoiding common pitfalls. Key formulas include the **perceptron update rule** for neural networks and the **expectation-maximization (EM) algorithm** for unsupervised learning. Understanding these methods and their limitations is crucial for effective machine learning model development.

## Worked Examples

To illustrate the application of machine learning concepts, consider the following examples. 
1. **Linear Regression**: Suppose we want to predict house prices based on their size. We have a dataset of 5 houses with sizes (1000, 1200, 1500, 1800, 2000) sqft and corresponding prices ($200,000, $250,000, $300,000, $350,000, $400,000). We can use linear regression to learn a model that predicts prices. Let's calculate the coefficients using the ordinary least squares method. 
First, we calculate the mean of sizes (x) and prices (y): x̄ = 1500, ȳ = 300,000. 
Then, we calculate the deviations from the mean and their products. 
The slope (β1) is the sum of (xi - x̄)(yi - ȳ) divided by the sum of (xi - x̄)^2. 
After calculation, β1 = 100. 
The intercept (β0) is ȳ - β1 * x̄ = 300,000 - 100 * 1500 = 100,000 (approximated for simplicity). 
Thus, our linear model is Price = 100,000 + 100 * Size. 
For a new house of size 2200 sqft, the predicted price would be 100,000 + 100 * 2200 = $320,000. 
2. **Decision Trees**: Consider a binary classification problem where we want to predict whether a person will buy a car based on their age and income. We have a dataset with the following examples: (20, $40,000, No), (30, $60,000, Yes), (25, $50,000, No), (40, $80,000, Yes). 
We can construct a decision tree by recursively partitioning the data. 
First, we choose the best attribute to split (e.g., age or income). 
Let's say we choose age and split at 30. 
We then have two subsets: (20, $40,000, No), (25, $50,000, No) and (30, $60,000, Yes), (40, $80,000, Yes). 
We continue this process until we reach pure subsets or a stopping criterion. 
The resulting tree can be used to classify new instances. 
3. **K-Nearest Neighbors (KNN)**: Suppose we want to classify iris flowers into their species based on sepal length and width. 
We have a dataset with the following examples: (5.1, 3.5, Setosa), (6.3, 3.3, Versicolor), (5.8, 2.7, Setosa), (7.2, 3.2, Virginica). 
For a new iris with sepal length 6.1 and width 3.1, we find its K-nearest neighbors. 
Let's say K = 3. 
We calculate the Euclidean distances: 
- To (5.1, 3.5) is √((6.1-5.1)^2 + (3.1-3.5)^2) = √(1^2 + 0.4^2) = √1.16 ≈ 1.08 
- To (6.3, 3.3) is √((6.1-6.3)^2 + (3.1-3.3)^2) = √(0.2^2 + 0.2^2) = √0.08 ≈ 0.28 
- To (5.8, 2.7) is √((6.1-5.8)^2 + (3.1-2.7)^2) = √(0.3^2 + 0.4^2) = √0.25 ≈ 0.5 
- To (7.2, 3.2) is √((6.1-7.2)^2 + (3.1-3.2)^2) = √(1.1^2 + 0.1^2) = √1.22 ≈ 1.1 
The 3 nearest neighbors are (6.3, 3.3, Versicolor), (5.8, 2.7, Setosa), and (6.1, 3.1) is closest to these, so it is classified as Versicolor. We have a dataset of 5 houses with sizes (1000, 1200, 1500, 1800, 2000) sqft and corresponding prices ($200,000, $250,000, $300,000, $350,000, $400,000). We can use linear regression to learn a model: price = β0 + β1 * size. Using ordinary least squares, we find β0 = $100,000 and β1 = $150/sqft. 
2. **Decision Trees**: Given a dataset of 10 students with attributes (age, GPA, attendance) and labels (pass/fail), we can construct a decision tree to predict student performance. For instance, if the dataset is [(20, 3.5, 90, pass), (22, 3.0, 80, fail), ...], the decision tree might learn rules like "if age > 21 and GPA > 3.2 then pass". 
3. **K-Means Clustering**: Consider a set of 2D data points representing customer locations: [(1, 2), (1, 4), (2, 3), (10, 10), (10, 12), (12, 11)]. Using K-Means with K=2, we initialize centroids at (1, 1) and (11, 11). After iteration, the centroids converge to (1.3, 3) and (10.7, 11), effectively clustering customers into two geographic groups.

## Applications

Machine learning has numerous applications in various domains, including computer vision, natural language processing, and robotics. In computer vision, machine learning is used for image classification, object detection, and segmentation, enabling applications such as self-driving cars, facial recognition, and medical image analysis. For instance, convolutional neural networks (CNNs) are used for image classification, while recurrent neural networks (RNNs) and long short-term memory (LSTM) networks are used for image captioning and video analysis. In natural language processing, machine learning is used for text classification, sentiment analysis, and language translation, enabling applications such as chatbots, virtual assistants, and language translation software. Additionally, machine learning is used in robotics for control and navigation, enabling applications such as autonomous robots and robotic arms. Other applications include recommender systems, predictive maintenance, and fraud detection, which are used in e-commerce, manufacturing, and finance respectively. The key principle behind these applications is the ability of machine learning algorithms to learn from data and make predictions or decisions based on that data, allowing for automation and improvement of various tasks and processes.

## Common Errors

Practitioners of machine learning often fall into several common pitfalls. Overfitting is a prevalent issue, where models are overly complex and fit the training data too closely, resulting in poor generalization to new, unseen data. This can be mitigated by regularization techniques, such as L1 and L2 regularization, or by using cross-validation to evaluate model performance. Another error is underfitting, where models are too simple and fail to capture the underlying patterns in the data. 
Data preprocessing is also a common source of mistakes, with improper handling of missing values, outliers, and data normalization leading to suboptimal model performance. Furthermore, ignoring class imbalance can result in biased models, where the majority class is favored over the minority class. 
Additionally, many practitioners fail to consider the assumptions of their chosen algorithm, such as linearity or independence, and neglect to evaluate their models using appropriate metrics, leading to misleading results. 
Lastly, not monitoring and addressing concept drift, where the underlying data distribution changes over time, can render models ineffective in real-world applications.

Another common error is failing to properly preprocess the data, such as not handling missing values, not scaling or normalizing features, and not encoding categorical variables correctly. This can lead to biased or inaccurate models. Additionally, practitioners may misinterpret the results of their models, such as using accuracy as the sole evaluation metric for classification problems with imbalanced classes, or not considering the impact of class imbalance on model performance.

Furthermore, ignoring the assumptions of the algorithms used, such as assuming linearity or normality when it does not hold, can lead to incorrect conclusions. Regularization techniques, such as L1 and L2 regularization, are often underutilized, leading to overfitting. Lastly, not using cross-validation or other techniques to evaluate model performance on unseen data can result in overly optimistic estimates of model performance, leading to disappointing results when the model is deployed in practice.

Practitioners of machine learning often make mistakes that can significantly impact the performance and reliability of their models. One common error is overfitting, where a model is too complex and fits the training data too closely, resulting in poor generalization to new, unseen data. This can occur when the model has too many parameters or when the training dataset is too small. Another error is underfitting, where a model is too simple and fails to capture the underlying patterns in the data. Regularization techniques, such as L1 and L2 regularization, can help mitigate overfitting by adding a penalty term to the loss function to discourage large weights.

Data preprocessing is another area where errors can occur. Failing to normalize or scale the data can lead to features with large ranges dominating the model, while features with small ranges are ignored. Additionally, ignoring class imbalance can result in models that are biased towards the majority class. Techniques such as SMOTE (Synthetic Minority Over-sampling Technique) and class weighting can help address class imbalance.

Furthermore, errors can occur when evaluating model performance. Using metrics such as accuracy alone can be misleading, especially when dealing with imbalanced datasets. Instead, practitioners should use a combination of metrics, including precision, recall, F1 score, and area under the ROC curve (AUC-ROC), to get a more comprehensive understanding of their model's performance.

Lastly, failing to monitor and update models over time can lead to concept drift, where the underlying data distribution changes, causing the model's performance to degrade. Techniques such as online learning and incremental learning can help adapt to changing data distributions. By being aware of these common errors, practitioners can take steps to avoid them and develop more robust and reliable machine learning models.

## Advanced

Machine learning research has led to the development of various advanced techniques, including deep learning, transfer learning, and meta-learning. Deep learning involves the use of neural networks with multiple layers to learn complex patterns in data, while transfer learning enables the application of pre-trained models to new tasks. Meta-learning focuses on training models to learn how to learn from few examples, facilitating adaptation to new tasks. Open questions in the field include the development of more robust and explainable models, as well as addressing issues related to bias, fairness, and transparency. Current research directions include the integration of machine learning with other disciplines, such as natural language processing, computer vision, and reinforcement learning. Additionally, there is a growing interest in exploring the potential of machine learning in emerging areas like edge AI, autonomous systems, and human-computer interaction. The field is also moving towards the development of more specialized and domain-specific models, such as those for healthcare, finance, and climate modeling, which require careful consideration of domain-specific constraints and challenges.

Machine learning, as a field of computer science, continues to evolve with advancements in graduate-level research. One key area of extension is in deep learning, where techniques such as transfer learning and attention mechanisms have improved the performance of neural networks on complex tasks like natural language processing and computer vision. Another area is in reinforcement learning, where the development of algorithms like deep Q-networks and policy gradients has enabled agents to learn from trial and error in complex environments. Open questions in the field include the lack of interpretability and explainability of machine learning models, particularly in high-stakes applications like healthcare and finance. Researchers are also exploring the intersection of machine learning with other fields, such as cognitive science and neuroscience, to better understand human intelligence and develop more human-like AI systems. Additionally, there is a growing interest in developing more robust and adversarially-resistant machine learning models, as well as models that can learn from limited data and adapt to changing environments. The field is moving towards more specialized and domain-specific applications, such as edge AI, autonomous systems, and human-AI collaboration, which require the development of new algorithms, architectures, and evaluation metrics. Furthermore, the increasing availability of large datasets and computational resources is driving the development of more complex and sophisticated machine learning models, which in turn raises important questions about fairness, accountability, and transparency in AI systems. Another area of focus is on explainability and interpretability of machine learning models, as the ability to understand and trust the decisions made by these models becomes increasingly important. The field is also moving towards more specialized areas such as meta-learning, which involves training models to learn how to learn, and multimodal learning, which focuses on integrating and processing multiple forms of data. Furthermore, the integration of machine learning with other areas of computer science, such as computer vision, robotics, and human-computer interaction, is leading to the development of more sophisticated and autonomous systems. Additionally, the field is exploring new paradigms such as federated learning, which enables machine learning models to be trained on decentralized data, and edge AI, which involves deploying machine learning models on edge devices. These advancements and open questions are driving the field of machine learning forward, with potential applications in areas such as healthcare, finance, and transportation.
