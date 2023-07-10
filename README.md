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

#### User Story:
- As a client, I want a machine learning (ML) model that can predict with at least 86% accuracy whether a given cherry leaf is healthy or contains powdery mildew.

These user stories were addressed by implementing the following tasks, which are presented in the Streamlit dashboard and calculated in the Data Visualisation notebook:

- The client can upload cherry leaf images to the dashboard using an uploader widget for instant evaluation. The following key features are associated with this functionality:
  - Images must be uploaded in `.jpeg` format.
  - Multiple images can be uploaded at once, up to a total size of 200MB.
  - The dashboard will display the uploaded image along with a prediction statement indicating whether the leaf is infected with powdery mildew or not, as well as the associated probability.

### Business Requirement 3: Report

The client is interested in obtaining a prediction report for the examined leaves.

#### User Story:
- As a client, I want to receive a report from the machine learning (ML) predictions on new leaves.

This user story was addressed by implementing the following task, which is presented in the Streamlit dashboard:
- After each batch of uploaded images, a downloadable `.csv` report is generated containing the predicted status for each leaf.

## Dashboard Design (Streamlit App User Interface)

### Page 1: Quick Project Summary
- General Information:
    - Powdery mildew is a fungal disease in cherry trees caused by Podosphaera clandestina. It forms a layer of mildew on the leaves, affecting plant growth and causing crop loss.
    - Visual criteria for infected leaves: light-green circular lesions and white cotton-like growth on the leaves and fruits.
- Project Dataset:
    - 4208 photos of cherry leaves categorized as healthy or infected with powdery mildew.
- Business requirements:
    1. Visually differentiate between infected and healthy leaves.
    2. Determine if a leaf is infected or not.
    3. Generate a prediction report for examined leaves.
- Link to this Readme.md file for more information about the project.

### Page 2: Leaves Visualizer
- Checkbox 1: Average vs. Variability Image
- Checkbox 2: Average Infected vs. Average Healthy Leaves
- Checkbox 3: Image Montage

### Page 3: Powdery Mildew Detector
- User-friendly interface with a file uploader widget for uploading cherry leaf images.
- Display of uploaded image, prediction visualization, and prediction statement.
- Table showing image names and prediction results.
- Download button for report in CSV format.

### Page 4: Project Hypothesis and Validation
- Blocks for each project hypothesis, validation, and conclusion.

### Page 5: ML Performance Metrics
- Label Frequencies
- Model History - LSTM Model Accuracy and Losses
- Generalised Performance on Test Set

## Unfixed Bugs
A persistent issue was encountered with the Kaleido library, resulting in the inability to save the generated image. Despite extensive troubleshooting, the error message "ValueError: Failed to start Kaleido subprocess. Error stream:" persisted, rendering a resolution unattainable at the present moment. The bug can be found in the "03-ModelingEvaluating.ipynb" file. 

For now I have manually saved the image, but I would need to explore further libraries to find one that is able to save the image generated.

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
