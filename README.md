# External Influences on California High School Performance
ECE 143 Spring 2018 Group Project  
Group 5: Kenny Chen, Kevin Lai, Yan Sun  
[Project Proposal](https://docs.google.com/document/d/1NXY5QkYFd78zrLC9b8EnWYyzunz2E4unk_1N1ArQeUQ/edit)

### 1. Description of Project
Parents and family members care about the physical well beings and academic performances of their children at schools. Nowadays, two significant measures for high school student performance in these categories are the standardized SAT exam and physical fitness test results. However, apart from their own inherited physical characterization and ability to study and absorb knowledge, there exists many other external factors that may affect a student’s performance, including regional weather condition, financial income situation, and local safety situation. In order to explore the possible subliminal relations among these factors and student performance, our group plans to use several relevant datasets in order to investigate any correlations and visualize any findings. Specifically, we are interested in investigating how weather, crime rates, and financial factors affect the performance of high school students both physically and academically. The relevant and publically available datasets online that we plan to use for this analysis are listed above, and include average annual California temperatures, student SAT scores, student physical fitness abilities, arrests and crime rates in California, and financial situations. All data is given by county and a yearly time frame, and is provided by the government that will ensure accuracy.

It has been long understood both intuitively and by means of formal peer reviewed studies that several factors contribute to the academic and physical development of children. While this study is not novel in its premise, it is original in the exact factors and datasets that it uses for analysis (as far as we can tell). While we are not creating a product or resource that has any utility in the traditional sense, we believe the work is important as it generates awareness of a problem that has not received a fair share of attention. We aim to accomplish this with a multivariate analysis using multiple datasets and clear, easy-to-digest figures, and animations to paint our picture clearly. We hope that we can educate our peers in our findings regarding how external factors can affect academic and physical aptitude in high school students.

### 2. Public Datasets
In this project we used the following datasets:

* California SAT Scores Dataset:
https://www.cde.ca.gov/ds/sp/ai/

* California Crime Dataset:
    * Crime Events Data: https://openjustice.doj.ca.gov/data
    * Population Data: https://data.ca.gov/dataset/california-population-projection-county-age-gender-and-ethnicity

* California Unemployment Rate Dataset:
https://www.ers.usda.gov/data-products/county-level-data-sets/download-data/

* California Physical Test Dataset:
https://www.cde.ca.gov/ta/tg/pf/pftresearch.asp

These datasets are all from government websites (.gov), which ensures that the contained data is accurate and reliable. We used an additional Population dataset to calculate the crime rate percentage, as the raw crime events dataset only supplied the number of crimes within the county.

### 3. Data Preprocessing
The datasets listed above contained a large amount of information, and as such we needed to preprocess each dataset in order to extract meaningful data and information that we want to use for this project. To give an idea of how large some of these raw datasets were, in the Physical Fitness Test dataset, each year contained nearly 400MB of data! With our goal of looking at data across multiple years, this quickly added up to GB's of data, making it unfeasible to use the raw data as is. Therefore, prior to analysis, we took the following steps:

1. Download all the aforementioned datasets.
2. Put them in the same path with notebooks for preprocessing in ```./src/data_preprocess/``` then run the preprocessing notebooks.
3. Then all the dataframes contain preprocessed data could be generated and saved into pickle files.
4. These pickle files are saved in ```./data/```.

These preprocessing scripts extracted data from the corresponding datasets and placed them into a Pandas dataframe of dimension 7x58. The seven rows were the seven years that we extracted data from (2007 - 2013) and the columns were the 58 counties in California. For example, in the SAT preprocessed Pandas dataframe, it would contain the average SAT score per county (58 columns) for each of the seven years from 2007 to 2013 (7 rows). These dataframes were then saved into a Pickle file for easy distribution and data sharing.

### 4. Visualizations and Animations
To visualize the data, we first used the Plotly library in order to create a heatmap of the California map of each preprocessed dataset. A sign-up for Plotly was required at https://plot.ly/ to generate an API key for use. After plotting each individual dataset, we then looked at the correlations between crime, unemployement rate, and physical fitness to the average SAT score per county. This was visualized in different plots, as can be seen in this Jupyter notebook.

### 5. Dependencies
* python3
* pandas == 0.22.0
* numpy == 1.14.1
* pickle
* glob
* zipfile
* imageio == 2.1.2
* matplotlib == 2.2.0
* plotly == 2.7.0
