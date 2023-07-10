## Cherry Leaves Mildew Detector

### Deployed version at [powdery-mildew-detector.herokuapp.com](https://powdery-mildew-detector-app-f1fbb6ec0583.herokuapp.com)

## Dataset Content

The dataset contains 4208 featured photos of single cherry leaves against a neutral background. The images are taken from the client's crop fields and show leaves that are either healthy or infested by [powdery mildew](https://extension.psu.edu/powdery-mildew-of-cherry-and-plum-in-home-fruit-plantings#:~:text=This%20disease%20is%20caused%20by,powdery%20mildew%20group%20of%20fungi.&text=The%20same%20fungus%20reportedly%20causes,and%20a%20few%20ornamental%20plants.) a biotrophic fungus. This disease affects many plant species but the client is particularly concerned about their cherry plantation crop since bitter cherries are their flagship product. The dataset is sourced from [Kaggle](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves).

## Business Requirements

We were requested by our client, Farmy & Foods, a company in the agricultural sector, to develop a Machine Learning-based system that can instantly detect whether a certain cherry tree is affected by powdery mildew and requires treatment with a fungicide. The system should be capable of analyzing a tree leaf image and determining its health status promptly.

The purpose of this system is to automate the detection process, which has been performed manually until now. Farmy & Foods has thousands of cherry trees spread across multiple farms, making the manual inspection process time-consuming and non-scalable.

### To Summarise

The project encompasses the following business requirements:

1. Conduct a study to visually differentiate a healthy cherry leaf from one infected by powdery mildew.
2. Develop a prediction model to accurately classify cherry trees as healthy or affected by powdery mildew.
3. Generate a prediction report that provides detailed information about the examined leaves.

The aim of these requirements is to assist the client in effectively identifying and managing powdery mildew in their cherry trees, enabling them to make informed decisions based on the analysis of leaf conditions.

## Hypothesis and Validation

- **Hypothesis**: Infected leaves exhibit distinct marks that differentiate them from healthy leaves.
- **Validation Approach**: Conduct research on the disease and perform an average image study to further investigate and confirm the presence of clear distinguishing marks on infected leaves.


### Hypothesis: Differentiation of Infected Leaves

**Introduction**

Infected cherry leaves are expected to exhibit clear marks that differentiate them from healthy leaves. The initial symptom typically manifests as a light-green, circular lesion on either leaf surface, followed by the development of a subtle white cotton-like growth in the infected area. To enable effective machine learning analysis, image preprocessing techniques are employed to optimize feature extraction and model training.

- **Business Requirement 1: Data Visualisation**

  - We will display the "mean" and "standard deviation" images for infected and uninfected cherry leaves.
  - We will visualise the difference between an average infected cherry leaf and an average uninfected cherry leaf.
  - Image montages for infected or uninfected cherry leaves will be generated.

- **Business Requirement 2: Classification**

  - Our objective is to predict whether a given cherry leaf is infected with powdery mildew or not.
  - We will develop a binary classifier specifically for this task and generate prediction reports.

- **Business Requirement 3: Report**

  - The client's requirement is to obtain a comprehensive prediction report of the examined cherry leaves.
  - The report should provide detailed insights, analysis, and evaluation of the predictions made by the system.

## Rationale for Mapping Business Requirements to Data Visualisations and ML Tasks

The three main business requirements have been broken down into several user stories, which have been translated into specific machine learning tasks. All tasks have been manually tested and verified to ensure they function as expected.

By mapping the business requirements to data visualisations and ML tasks, we can effectively address the client's needs and provide accurate predictions and reports. This approach ensures that the implemented solutions align with the client's objectives and provide valuable insights for their cherry leaf analysis.

### Business Requirement 1: Data Visualisation

The client is interested in conducting a study that visually differentiates a cherry leaf affected by powdery mildew from a healthy one.

#### User Story:
- As a client, I want to navigate easily around an interactive dashboard so that I can view and understand the presented data.
- As a client, I want to display an image montage for healthy cherry leaves and cherry leaves affected by powdery mildew to visually differentiate them.
- As a client, I want to display the "mean" and "standard deviation" images for healthy cherry leaves and cherry leaves affected by powdery mildew to visually differentiate them.
- As a client, I want to display the difference between an average healthy cherry leaf and a cherry leaf affected by powdery mildew to visually differentiate them.

These user stories were addressed by implementing the following tasks, which are presented in the Streamlit dashboard and calculated in the Data Visualisation notebook:

- Development of a Streamlit-based dashboard with an easy-to-navigate side bar.
- Calculation of the difference between an average infected leaf and an average healthy leaf.
- Display of the "mean" and "standard deviation" images for healthy and powdery mildew-infected leaves.
- Image montage for both infected and healthy leaves.

### Business Requirement 2: Classification

The client is interested in determining whether a given cherry leaf is affected by powdery mildew or not.


## Cloud IDE Reminders

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you, so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.


## Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
* The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.



## Business Requirements
The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute.  The company has thousands of cherry trees, located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.


* 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
* 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.


## Hypothesis and how to validate?

* I am hypothesising that analyzing visual characteristics of cherry blossom images can differentiate healthy leaves from powdery mildew-infected ones. By extracting relevant features and training a machine learning model, I'm aiming to predict the health status of cherry leaves based on their images.

To validate my hypothesis, I will:

1. Explore the dataset and visually compare features of healthy and powdery mildew-infected cherry leaves.
2. Extract meaningful features from the images, focusing on color distributions, texture patterns, and shape characteristics.
3. Analyze and compare the extracted features between healthy and infected leaves.
4. Build and evaluate machine learning models using the extracted features.
Assess the model's performance using accuracy, precision, recall, and F1-score metrics.
5. Validate my hypothesis by determining if the model accurately distinguishes between healthy and infected cherry leaves.

By conducting these steps, I aim to validate my hypothesis and provide evidence that visual characteristics can be used to identify the health status of cherry leaves.


## The rationale to map the business requirements to the Data Visualisations and ML tasks

1. As a client, I want to conduct a study that visually differentiates a healthy cherry leaf from one that contains powdery mildew. This will allow me to accurately identify and classify cherry leaves based on their health condition.
2. As a client, I want to predict whether a cherry leaf is healthy or contains powdery mildew. By having this predictive capability, I can proactively identify and manage potential issues related to powdery mildew infection in cherry trees, ensuring the overall health and quality of the produce.

Rationale for Mapping to Data Visualisations and ML Tasks:

As a client, I want to conduct a study to visually differentiate a healthy cherry leaf from one that contains powdery mildew, so that I can effectively identify and manage potential health issues in cherry trees.

To achieve this, the following objectives and tasks are essential:

1. Data Visualisation:
* Objective: By visualising the characteristics of healthy and infected cherry leaves, such as colour, texture, and shape, I can identify distinct patterns and differences that aid in the differentiation process.
* Task: Utilize data visualisation techniques to explore and represent the visual features of cherry leaves, enabling a comprehensive understanding of the variations between healthy and powdery mildew-infected leaves.
2. ML Tasks:
* Objective: I want to leverage machine learning algorithms to predict whether a cherry leaf is healthy or contains powdery mildew, providing an automated and reliable assessment.
* Task: Develop ML models that can learn from labelled data, using the visual features extracted from the cherry leaf images. By mapping the business requirement to ML tasks, I can train classification models that accurately classify cherry leaves based on their visual characteristics.

Furthermore, I understand the significance of data visualisation in evaluating the ML models' performance and ensuring their effectiveness:

1. Data Visualisation:
* Objective: By visualising the predictions made by the ML models, I can gain insights into the model's performance and assess the accuracy of the classification task.
* Task: Utilise visualisation techniques to present the model's predictions and classification results, allowing stakeholders to understand the model's capability in predicting the health status of cherry leaves.
2. ML Tasks:
* Objective: By effectively mapping the business requirement to ML tasks, I can develop robust classification models that leverage the visual features of cherry leaf images for accurate predictions.
* Task: Train machine learning models using labelled data, enabling them to predict the health status of cherry leaves based on the extracted visual features.


## ML Business Case
Aim: The aim of the ML task is to develop a predictive model that can accurately differentiate between healthy cherry leaves and those infected with powdery mildew.

Learning Method: The ML task will utilize a supervised learning approach, specifically binary classification, to train the model on a labeled dataset of cherry leaf images.

Ideal Outcome: The ideal outcome is to create a model that can accurately classify cherry leaves as healthy or powdery mildew-infected based on their visual features, with a high degree of accuracy.

Success/Failure Metrics: The success of the ML task will be evaluated based on the model's accuracy, precision, recall, and F1 score in classifying cherry leaves. A high accuracy rate, along with balanced precision and recall scores, indicates a successful model.

Model Output and Relevance: The model will output a prediction for each cherry leaf image, indicating whether it is healthy or infected with powdery mildew. This prediction is relevant to stakeholders as it provides a quick and automated method to identify diseased cherry leaves, aiding in effective management and prevention strategies.

Training Data: The model will be trained using a dataset of labeled cherry leaf images, where each image is annotated as healthy or infected. The training data will include a sufficient number of samples representing both healthy and powdery mildew-infected leaves to ensure the model captures the relevant visual patterns.

By framing the ML business case in this manner, we establish clear objectives, define the learning approach, outline the desired outcomes and metrics, highlight the relevance of the model's output, and specify the heuristics and training data necessary for successful model development.


## Dashboard Design
* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other items, that your dashboard library supports.
* Finally, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project, you were confident you would use a given plot to display an insight, but later, you chose another plot type).


## Unfixed Bugs
* You will need to mention unfixed bugs and why they were unfixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable for consideration, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file. 


## Main Data Analysis and Machine Learning Libraries
* Here you should list the libraries used in the project and provide an example(s) of how you used these libraries.


## Credits 

* In this section, you need to reference where you got your content, media and from where you got extra help. It is common practice to use code from other repositories and tutorials. However, it is necessary to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A.
- Instructions on how to implement form validation on the Sign-Up page were taken from [Specific YouTube Tutorial](https://www.youtube.com/).
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/).

### Media

- The photos used on the home and sign-up page are from This Open-Source site.
- The images used for the gallery page were taken from this other open-source site.



## Acknowledgements (optional)
* Thank the people that provided support throughout this project.
