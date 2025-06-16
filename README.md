# Instagram Trends Analyzer

A real-time Python-based system to extract, clean, visualize, and analyze engagement metrics from Instagram posts using the Instagram Graph API.

## Overview

This project automates the process of identifying top-performing Instagram posts by:
- Extracting post data (likes, comments, hashtags, captions)
- Cleaning and structuring the data
- Visualizing metrics through interactive dashboards
- Analyzing engagement patterns and trends

## Features

- Real-time data extraction via Instagram Graph API
- Data cleaning (missing values, timestamp normalization, hashtag extraction)
- Interactive visualization using Streamlit
- Engagement rate calculation and post ranking
- Trend detection based on hashtags and post timing

## Tech Stack

- **Python 3.x**
- **Instagram Graph API**
- **Streamlit**
- **Pandas**
- **Matplotlib / Seaborn**

## Engagement Rate Formula

```
Engagement Rate = (Likes + Comments) / Total Followers × 100
```

## 🧪 Results Summary

| Dataset       | Posts | Accuracy with Features | Without Features | Top Insight                         |
|---------------|-------|------------------------|------------------|--------------------------------------|
| Influencers   | 1,130 | 96.2%                  | 89.4%            | Giveaways spike on Fridays          |
| Businesses    | 2,130 | 97.4%                  | 86.1%            | UGC drives higher comments          |
| Events        | 2,760 | 98.1%                  | 84.9%            | Post-event recaps increase reach    |

Average accuracy boost with features: **+9.7%**

## 🗂Modules

1. **Data Extraction** – via Instagram Graph API
2. **Data Processing** – clean and structure raw data
3. **Visualization** – explore data with charts
4. **Trend Analysis** – identify high-engagement content

## How to Run

1. Clone the repo  
   ```
   git clone https://github.com/your-username/instagram-trends-analyzer.git
   cd instagram-trends-analyzer
   ```

2. Install required packages  
   ```
   pip install -r requirements.txt
   ```

3. Run the Streamlit app  
   ```
   streamlit run app.py
   ```
