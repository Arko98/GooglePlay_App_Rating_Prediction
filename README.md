# Introduction
This Project uses Keras Deep Learning Library and it's functional API to predict App Rating of Google PlayStore using given features of 10,841 unique App informations.

# Dataset
The Dataset source: https://www.kaggle.com/lava18/google-play-store-apps/version/1
The Data consists of 10,481 unique app records each having 13 features(Some of them are categorical and rest of them are Continous). 

# Summary
With a custom distance metric the architecture achieves 88% of Training accuracy and 87% of Testing accuracy on a randomly chosen unseen subset of the dataset(i.e testset)

# Future Scope
1. Different Architectures can be implemented to check and tweak performance enhancement.
2. Custom Metrics thresold can be tightened along with increasing the training epoch to achieve higher accuracy.
3. As Functional API is used, the architecture can be changed very easily by just tweaking the architecuture method.
