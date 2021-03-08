# Financial and Election Data Analysis

## Background 

This analysis has two parts where a Python programming scripts have been written to calculate the bank's profitability and to determine the results of an election process in a rural town in the CSV datasets provided. 

## 1. Financial Analysis

![Image](https://3fssfi2d8cso2spw9o1uumfp-wpengine.netdna-ssl.com/wp-content/uploads/2020/09/shutterstock_362054459-1536x1038.jpg)

## Requirements

Calculate the following:
* Total Months
* Total Profits
* Average Profit Change During the Entire Period
* Greatest Profit Increase in Month and Amount
* Greatest Profit Decrease in Month and Amount

## Datasets:

* [Financial CSV Dataset](https://github.com/cecileung1208/Financial-and-Election-Data-Analysis/blob/main/Financial%20Analysis/Resources/Financial_Data.csv)

## Method
* Use Visual Studio Code to write Python script
* Ensure the Financial CSV Dataset is in chronological order
* Import the Financial CSV Dataset
* Create Empty Lists with respective headings to store information
 * Loop through the data to calculate the following:
    * Monthly Profit Changes
    * Total Profits
    * Average Profits During the Entire Period
    * Greatest Profit Increase in Month and Amount
    * Greatest Profit Decrease in Month and Amount
* Output results to terminal
* Export results in a text file

## Python Scripts

* [Financial Analysis Script](https://github.com/cecileung1208/Financial-and-Election-Data-Analysis/blob/main/Financial%20Analysis/Financial_Analysis.py)

## Results

Financial Results are as follows:
* There are a total of 86 months of profit data.
* The bank's total profit during this period is $38,382578.
* The average profit change during the entire period is a loss of $2,315.12.
* The greatest increase in profits is during January, 2012 with a gain of $1,926,159.
* The greatest decrease in profits is during August, 2013 with a loss of $2,196,167.

Terminal Output:

![Image](https://github.com/cecileung1208/Financial-and-Election-Data-Analysis/blob/main/Images/Financial%20Results%20Terminal%20Output.png)

Text File Output:

![Image](https://github.com/cecileung1208/Financial-and-Election-Data-Analysis/blob/main/Images/Financial%20Results%20Text%20Output.png)


## 2. Election Analysis

![Image](https://s7d2.scene7.com/is/image/TWCNews/Getty_Vote_Ballot_Election?wid=1250&hei=703&$wide-bg$)

## Requirements

 Determine the following:
 * Total Number of Votes Casted
 * Complete List of Candidates who Received Votes
 * Percentage Won by Each Candidate
 * Total Number of Votes by Each Candidate
 * The Winner of the Election Based on Popular Vote

## Datasets:

* [Election CSV Dataset](https://github.com/cecileung1208/Financial-and-Election-Data-Analysis/blob/main/Election%20Analysis/Resources/Election_Data.csv)

## Method
* Use Visual Studio Code to write Python script
* Import the Election CSV Dataset
* Create Empty Lists with respective headings to store information
* Calculate the total votes
 * Loop through the data to calculate the following:
    * Complete List of Candidates who Received Votes
    * Percentage Won by Each Candidate
    * Average Monthly Profits
    * Total Number of Votes by Each Candidate
* Determine the winner of the election
* Output results to terminal
* Export results in a text file

## Python Scripts

* [Election Analysis Script](https://github.com/cecileung1208/Financial-and-Election-Data-Analysis/blob/main/Election%20Analysis/Election_Analysis.py) 

## Results

Election Results are as follows:
* There are a total of 3,521,001 votes.
* There are 4 candidates:  Corey, Khan, Li, and O'Tooley.
* Corey received 20% of the votes with 704,200 votes.
* Li recieived 14% of the votes with 492,940 votes.
* Khan received 63% of the votes with 2,218,231 votes.
* O'Tooley recieved 3% of the votes with 105,630 votes.
* Khan is the winner of the election.

Terminal Output:

![Image](https://github.com/cecileung1208/Financial-and-Election-Data-Analysis/blob/main/Images/Election%20Results%20Terminal%20Output.png)

Text File Output:

![Image](https://github.com/cecileung1208/Financial-and-Election-Data-Analysis/blob/main/Images/Election%20Results%20Text%20Output.png)

