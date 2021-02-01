# Financial and Election Data Analysis

## Background 

This analysis has two parts where a Python programming scripts have been written to calculate the bank's profitability and to determine the results of an election process in a rural town in the CSV datasets provided. 

## 1. Financial Analysis

## Requirements

The project is done in two parts are per the below sections.  For each of the section, we must calculate the information in the bullet points.

 **Financial Data Analysis**
* Total Months
* Total Profits
* Average Profit Change
* Greatest Profit Increase in Month and Amount
* Greatest Profit Decrease in Month and Amount


## Datasets:

[Financial CSV Dataset](https://github.com/cecileung1208/Financial-and-Election-Data-Analysis/blob/main/Financial%20Analysis/Results/Resources/Financial_Data.csv)


## Method
* Use Visual Studio Code to write Python script
* Ensure the Financial CSV Dataset is in chronological order
* Import the Financial CSV Dataset
* Create Empty Lists with respective headings to store information
* Loop through the data to calculate the following:
        * Monthly Profit Changes
        * Total Profits
        * Average Monthly Profit Change
        *  Greatest Profit Increase in Month and Amount
        * Greatest Profit Decrease in Month and Amount
* Output results to terminal
* Export results in a text file

## Results

#### 1. Financial Analysis
#### 2. Election Analysis



        
 **2.  Election Data Analysis**
 * Total Number of Votes Casted
 * Complete List of Candidates who Received Votes
 * Percentage Won by Each Candidate
 * Total Number of Votes by Each Candidate
 * The Winner of the Election Based on Popular Vote




## **This Homework has 2 Folders:**

### **1.  PyBank**

This program is to provide a summary of the Profit & Losses (P&L) over the periods of Jan 2010 - Feb 2017 from the [PyBank Records](https://github.com/cecileung1208/Py-Me-Up-Charlie/blob/main/PyBank/Results/Resources/PyBank_Resources_budget_data.csv).  It calculates the result for the following:

*    Number of months
*    Total P&L
*    Average Change in P&L
*    Month with Minimum Change in P&L
*    Month with Maximum Change in P&L


There are 2 Folders that include:

* **Results**
    
    *   [Main.py](https://github.com/cecileung1208/Py-Me-Up-Charlie/blob/main/PyBank/Results/main.py) - This is the main code for PyBank.  Please run it on Visual Studio Code.
    
    *   [PyBank Terminal Output](https://github.com/cecileung1208/Py-Me-Up-Charlie/blob/main/PyBank/Results/PyBank%20-%20Terminal%20Output.docx) - This is the screenshot of how the code is displayed on the Visual Studio Code Terminal upon success.
    
    *   [Financial Summary](https://github.com/cecileung1208/Py-Me-Up-Charlie/blob/main/PyBank/Results/Financial_Summary.txt) - Text output file for the results.
    
    *   [Resources](https://github.com/cecileung1208/Py-Me-Up-Charlie/tree/main/PyBank/Results/Resources) - The CSV source file of all the P&L over Jan 2017 - Feb 2017.

**Note:  Please check the directory path before running the code.  It should be ...\Homework\Unit 3- Python Challenge\PyBank\Results**

* **Test**

    *   [PyBank_Test.py](https://github.com/cecileung1208/Py-Me-Up-Charlie/blob/main/PyBank/Test/PyBank_Test.py) - This is where I tested to ensure the code runs properly.  Comments are provided to explain how I got the solution.
    
    *  [Resources](https://github.com/cecileung1208/Py-Me-Up-Charlie/tree/main/PyBank/Test/Resources) - The CSV source file of all the P&L over Jan 2017 - Feb 2017.

**Note:  Please check the directory path before running the code.  It should be ...\Homework\Unit 3- Python Challenge\PyBank\Test**

### **2.  PyPoll**

This program is to provide an efficient counting process to provide the Election Results for a small rural town.  It calculates the result for the following:
* Total Number of Votes Cast
* Complete List of Candidates who Received Votes
* Percentage Won by Each Candidate
* Total Number of Votes by Each Candidate
* The Winner of the Election Based on Popular Vote

There are 2 Folders inside this code that includes:

* **Results**
    
    *  [Main.py](https://github.com/cecileung1208/Py-Me-Up-Charlie/blob/main/PyPoll/Results/main.py) - This is the main code for PyPoll.  Please run it on Visual Studio Code.
    
    *  [PyPoll Terminal Output](https://github.com/cecileung1208/Py-Me-Up-Charlie/blob/main/PyPoll/Results/PyPoll%20-%20Terminal%20Output.docx) - This is the screenshot of how the code is displayed on Visual Studio Code Terminal upon success.
    
    *  [PyPoll_Results](https://github.com/cecileung1208/Py-Me-Up-Charlie/blob/main/PyPoll/Results/PyPoll_Results.txt) - Text output file for the results.
    
    *  [Resources](https://github.com/cecileung1208/Py-Me-Up-Charlie/tree/main/PyPoll/Results/Resources) - The CSV source file of the election results.

**Note:  Please check the directory path before running the code.  It should be ...\Homework\Unit 3- Python Challenge\PyPollResults**


* **Test**

    *   [PyPoll_Test_Index.py](https://github.com/cecileung1208/Py-Me-Up-Charlie/blob/main/PyPoll/Test/Py_Poll_Test_Index.py) - Code is ran based on the index number of the unique list generated in the code.  Comments are provided to explain how I got the solution.
    
    *   [PyPoll_Test_Loop.py](https://github.com/cecileung1208/Py-Me-Up-Charlie/blob/main/PyPoll/Test/PyPoll_Test_Loop.py) - Another code is written because running the file based on the index requires manual inputs for more lines if new candidates are added to the list.  Using a for loop will overcome this as the code will go through every row to search for the candidate.  Comments are provided to explain how I got the solution.
    
    *    [Resources](https://github.com/cecileung1208/Py-Me-Up-Charlie/tree/main/PyPoll/Test/Resources) - The CSV source file for the election results.

**Note:  Please check the directory path before running the code.  It should be ...\Homework\Unit 3- Python Challenge\PyPoll\Test**
