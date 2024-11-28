# 📊 R Community Trends on Stack Overflow

This repository contains the source code, datasets, and analysis for my thesis, which explores trends and popular topics in the R programming language community on Stack Overflow. By leveraging statistical analysis and natural language processing (NLP) techniques, this research identifies key areas of interest such as **DataFrame Operations** and **Data Visualization**, while uncovering insightful patterns within the R-tagged questions.

---
[License of the Thesis](https://ikee.lib.auth.gr/record/354696/?ln=el)
---

## 🛠️ Methodology

The methodology for this project follows a structured pipeline as illustrated below:


1. **Data Collection**  
   - Stack Overflow data was retrieved via the **API**, focusing on questions tagged with "R".
   - The collected data was saved as a CSV file for further processing.

2. **Data Cleaning and Pre-processing**  
   - Raw data was cleaned and pre-processed to ensure quality, removing noise and irrelevant information.

3. **Statistical Analysis**  
   - Descriptive statistics were applied to provide an overview of user participation, question types, and engagement metrics.

4. **Topic Modeling**  
   - **Latent Dirichlet Allocation (LDA)** was employed to discover prevalent topics within the questions.

5. **Named Entity Recognition (NER)**  
   - Using **spaCy**, entities were extracted to analyze key terms and trends in the R community.

6. **Word Embedding**  
   - The final dataset includes additional columns for topics and entities, enabling richer insights and visualization.

---

## 💻 Technologies Used

- **Programming Language**: Python  
- **Natural Language Processing (NLP)**: spaCy, LDA  
- **Data Analysis and Visualization**: Pandas, Matplotlib, Seaborn  
- **Topic Modeling**: Latent Dirichlet Allocation (LDA)  
- **Named Entity Recognition (NER)**: spaCy  
- **API Integration**: Stack Overflow API  

---



