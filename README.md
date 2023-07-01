![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Codeanywhere Template Instructions

Welcome,

This is the Code Institute student template for Codeanywhere. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions. Click the `Use this template` button above to get started.

You can safely delete the Gitpod Template Instructions section of this README.md file,  and modify the remaining paragraphs for your own project. Please do read the Gitpod Template Instructions at least once, though! It contains some important information about Gitpod and the extensions we use. 

## How to use this repo

1. Use this template to create your GitHub project repo

1. Log into <a href="https://app.codeanywhere.com/" target="_blank" rel="noreferrer">CodeAnywhere</a> with your GitHub account.

1. On your Dashboard, click on the New Workspace button

1. Paste in the URL you copied from GitHub earlier

1. Click Create

1. Wait for the workspace to open. This can take a few minutes.

1. Open a new terminal and <code>pip3 install -r requirements.txt</code>

1. In the terminal type <code>pip3 install jupyter</code>

1. In the terminal type <code>jupyter notebook --NotebookApp.token='' --NotebookApp.password=''</code> to start the jupyter server.

1. Open port 8888 preview or browser

1. Open the jupyter_notebooks directory in the jupyter webpage that has opened and click on the notebook you want to open.

1. Click the button Not Trusted and choose Trust.

Note that the kernel says Python 3. It inherits from the workspace so it will be Python-3.8.12 as installed by our template. To confirm this you can use <code>! python --version</code> in a notebook code cell.


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

1. Conduct a study to visually differentiate a healthy cherry leaf from one that contains powdery mildew.
2. Predict if a cherry leaf is healthy or contains powdery mildew.

Rationale for Mapping to Data Visualisations and ML Tasks:

1. Conduct a study to visually differentiate a healthy cherry leaf from one that contains powdery mildew:
* Data Visualisation: By visualising the characteristics of healthy and infected cherry leaves, such as colour, texture, and shape, we can identify patterns and differences that aid in differentiation.
* ML Tasks: Machine learning algorithms can be trained on the visual features extracted from the images to learn the patterns associated with healthy and infected leaves. This enables the development of models that can classify new cherry leaves based on their visual characteristics.
2. Predict if a cherry leaf is healthy or contains powdery mildew:
* Data Visualisation: Visualising the predictions made by the ML models can provide insights into the performance and accuracy of the classification task. It helps stakeholders understand the model's ability to predict the health status of cherry leaves.
* ML Tasks: Machine learning models can be trained using labelled data to predict the health status of cherry leaves. By mapping the business requirement to ML tasks, we can develop classification models that leverage the visual features of the cherry leaf images to make accurate predictions.


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
