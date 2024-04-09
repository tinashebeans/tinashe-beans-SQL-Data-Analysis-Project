# Introduction
Dive into the data job market!Focusing on Data Analyst roles, this project explores:
(a) top_paying jobs (b) in-demand skills (c) where high demand meets high salary in Data Analytics.

SQL queries? Check them out more here:[project_sql folder](/project_sql/)
# Background
Following my Google Data Analytics certificate from [Coursera](), I was really hungry to improve my SQL skills and as I was going thruogh youtube I came across this amaizing SQL course from [Luke Barousse]() the Data Nerd. It is well structured, easy to follow and taught me new skills that I am using in my other projects.

Special thanks to Luke and ... for this amazing SQL course and thank you for sharing your invaluable knowledge with the world.

### The questions answered in the Analysis
1. What are the top-paying Data Analyst jobs?
2. What skills are required for these top-paying jobs?
3. What skills are most in demand in Data Analytics?
4. Which skills are associated with higher salaries?
5. What are the most optimal skills to learn?
# Tools I Used
These are the tools that i used for my Analysis:
- **SQL:** The backbone of the analysis, allowing me to sift through the large datasets and help discover critical insights.

- **Excel:** I used Excel for further analysis, filtering and visualizations.

- **PostgreSQL:** The database management tool for handling data.

- **Git & GitHub:** Essential for version control and sharing my SQL scripts and analysis, ensuring collaboration and project tracking.
# The Analysis
Each query for this project is aimed at investigating specific aspects of the data analyst job market. Here is how i approached each question:

### 1. Top Paying Data Analyst Roles
To identify the top 10 highest paying roles. I filtered Data Analyst Positions using their average yearly salary and location (focusing on remote jobs). This query Highlights the high paying opportunities in the field.

```sql
SELECT
    job_id,
    job_title,
    job_location,
    job_schedule_type,
    salary_year_avg,
    job_posted_date,
    company_dim.name AS company_name
FROM
    job_postings_fact
LEFT JOIN company_dim ON job_postings_fact.company_id = company_dim.company_id
WHERE
    job_title_short = 'Data Analyst'
    AND job_location = 'Anywhere'
    AND salary_year_avg IS NOT NULL
ORDER BY
    salary_year_avg DESC
LIMIT 10

```
Here's the breakdown of the top data analyst jobs in 2023:

-**Wide Salary Range:** Top 10 paying data analyst roles span from $184,000 to $650,000, indicating significant salary potential in the field.

**Diverse Employers:** Companies like SmartAsset, Meta, and AT&T are among those offering high salaries, showing a broad interest across different industries.

**Job Title Variety:** There's a high diversity in job titles, from Data Analyst to Director of Analytics, reflecting varied roles and specializations within data analytics.

![[Top Paying Roles]](assets\top_paying_jobs.png)
*Bar graph to show the top 10 paying job roles*

### 2. Skills Required For These Top Paying Roles
Created a CTE to join the job_postings_fact table with the company_dim table, this was to get the name of te company with the associated role.

Then joined the CTE with the skills_job_dim table to the results of joining the skills table and the skills_job_table to match the role with the associated skill.
Below is the code.

```sql
WITH top_paying_jobs AS(
    SELECT
        job_id,
        job_title,
        company_dim.name AS company_name,
        salary_year_avg 
    FROM
        job_postings_fact
    LEFT JOIN company_dim ON job_postings_fact.company_id = company_dim.company_id
    WHERE
        job_title_short = 'Data Analyst'
        AND job_location = 'Anywhere'
        AND salary_year_avg IS NOT NULL
    ORDER BY
        salary_year_avg DESC
    LIMIT 10
)

SELECT 
    top_paying_jobs.*,
    skills
FROM
    top_paying_jobs
INNER JOIN skills_job_dim ON top_paying_jobs.job_id = skills_job_dim.job_id
INNER JOIN skills_dim ON skills_job_dim.skill_id = skills_dim.skill_id
ORDER BY 
    salary_year_avg DESC
```
### The results from this query are not conclusive to the question hence i then used excel to perform further analysis.

***Step 1:** Uploaded the table from the query to Excel.

***Step :** Removed duplicates from the skills column to obtain unique skill values.


***Step 3:** Use the **=COUNTIF()** function to get the count of the individual skills.
![[Top Paying Roles Skills]](assets/Skills%20paying%20highly/1%20countif.png)

![Top Paying Role Skills](assets/Skills%20paying%20highly/2%20countif.png)

***Step 4:** then I arranged the results in descending order to show which skill had the highest frequency

![Top Paying Role Skills](assets/Skills%20paying%20highly/3%20desc.png)

Here's the breakdown of the most demanded skills for the top 10 highest paying data analyst jobs in 2023:

-**SQL** is leading with a bold count of 8.

**Python** follows closely with a bold count of 7.

**Tableau** is also highly sought after, with a bold count of 6.

 Other skills like R, Snowflake, Pandas, and Excel show varying degrees of demand.

 ![Top Paying Role Skills](assets/Skills%20paying%20highly/top%20paying%20skill%20count.png)

 ### 3. In-Demand Skills For Data Analytics
 This query helped identify the skills most frequently requested in job postings, directing focus to areas with high demand.

 ```sql
 SELECT 
    skills,
    COUNT(skills_job_dim.job_id) AS demand_count

FROM
    job_postings_fact
INNER JOIN skills_job_dim ON job_postings_fact.job_id = skills_job_dim.job_id
INNER JOIN skills_dim ON skills_job_dim.skill_id = skills_dim.skill_id

WHERE
    job_title_short = 'Data Analyst'
GROUP BY
    skills

ORDER BY
    demand_count DESC
LIMIT 5 
 ```
 Here's the breakdown of the most demanded skills for data analysts in 2023

**SQL** and **Excel** remain fundamental, emphasizing the need for strong foundational skills in data processing and spreadsheet manipulation.

Programming and Visualization Tools like **Python**, **Tableau**, and **Power BI** are essential, pointing towards the increasing importance of technical skills in data storytelling and decision support.

![Top Paying Role Skills](assets/skill%20count.png)
*Graph of the demand for the top 5 skills in data analyst job postings*

### 4. Skills With High Salaries
Exploring the average salaries associated with different skills revealed which skills are the highest paying **FOR REMOTE** Data Analyst jobs

```sql
SELECT 
    skills,
    ROUND(AVG(salary_year_avg), 0) AS avg_salary

FROM
    job_postings_fact
INNER JOIN skills_job_dim ON job_postings_fact.job_id = skills_job_dim.job_id
INNER JOIN skills_dim ON skills_job_dim.skill_id = skills_dim.skill_id

WHERE
    job_title_short = 'Data Analyst'
    AND salary_year_avg IS NOT NULL
    AND job_work_from_home = TRUE
GROUP BY
    skills

ORDER BY
    avg_salary DESC
LIMIT 10
```
Here's a breakdown of the results for top paying skills for Data Analysts:

**High Demand for Big Data & ML Skills:** Top salaries are commanded by analysts skilled in big data technologies (PySpark, Couchbase), machine learning tools (DataRobot, Jupyter), and Python libraries (Pandas, NumPy), reflecting the industry's high valuation of data processing and predictive modeling capabilities.

**Software Development & Deployment Proficiency:** Knowledge in development and deployment tools (GitLab, Kubernetes, Airflow) indicates a lucrative crossover between data analysis and engineering, with a premium on skills that facilitate automation and efficient data pipeline management.

**Cloud Computing Expertise:** Familiarity with cloud and data engineering tools (Elasticsearch, Databricks, GCP) underscores the growing importance of cloud-based analytics environments, suggesting that cloud proficiency significantly boosts earning potential in data analytics.

![Average salaries of top paying skills](assets/Skills%20paying%20highly/average%20salary%20for%20top%20payin%20skills.png).
*average salary for the top 10 paying skills for remote data analysts*

### 5.  Most Optimal Skills to Learn (High demand and High paying)
Combining insights from demand and salary data, this query aimed to pinpoint skills that are both in high demand and have high salaries, offering a strategic focus for skill development **FOR REMOTE WORK.**

```sql
WITH skills_demand AS(
    SELECT 
        skills_dim.skill_id,
        skills_dim.skills,
        COUNT(skills_job_dim.job_id) AS demand_count

    FROM
        job_postings_fact
    INNER JOIN skills_job_dim ON job_postings_fact.job_id = skills_job_dim.job_id
    INNER JOIN skills_dim ON skills_job_dim.skill_id = skills_dim.skill_id

    WHERE
        job_title_short = 'Data Analyst'
        AND salary_year_avg IS NOT NULL
        AND job_work_from_home = TRUE
    GROUP BY
        skills_dim.skill_id
), average_salary AS(
    SELECT 
    skills_dim.skill_id,
    skills,
    ROUND(AVG(salary_year_avg), 0) AS avg_salary

FROM
    job_postings_fact
INNER JOIN skills_job_dim ON job_postings_fact.job_id = skills_job_dim.job_id
INNER JOIN skills_dim ON skills_job_dim.skill_id = skills_dim.skill_id

WHERE
    job_title_short = 'Data Analyst'
    AND salary_year_avg IS NOT NULL
GROUP BY
    skills_dim.skill_id

)

SELECT
    skills_demand.skill_id,
    skills_demand.skills,
    demand_count,
    avg_salary
FROM
    skills_demand
INNER JOIN average_salary ON skills_demand.skill_id = average_salary.skill_id
ORDER BY
    demand_count DESC,
    avg_salary
LIMIT 25
```
![high paying and high demand skills](assets/Skills%20paying%20highly/top_25_high-demand%20and%20high%20paying%20skills.png).

Here's a breakdown of the most optimal skills for Data Analysts in 2023:

- **High-Demand Programming Languages:** Python and R stand out for their high demand, with demand counts of 236 and 148 respectively. Despite their high demand, their average salaries are around $101,397 for Python and $100,499 for R, indicating that proficiency in these languages is highly valued but also widely available.

- **Cloud Tools and Technologies:** Skills in specialized technologies such as Snowflake, Azure, AWS, and BigQuery show significant demand with relatively high average salaries, pointing towards the growing importance of cloud platforms and big data technologies in data analysis.

- **Business Intelligence and Visualization Tools:** Tableau and Looker, with demand counts of 230 and 49 respectively, and average salaries around $99,288 and $103,795, highlight the critical role of data visualization and business intelligence in deriving actionable insights from data.

- **Database Technologies:** The demand for skills in traditional and NoSQL databases (Oracle, SQL Server, NoSQL) with average salaries ranging from $97,786 to $104,534, reflects the enduring need for data storage, retrieval, and management expertise.

# What I Learned
Throughout this adventure, I've turbocharged my SQL toolkit with some serious firepower:

**🧩 Complex Query Crafting:** Mastered the art of advanced SQL, merging tables like a pro and wielding WITH clauses for CTE table creation

**🧩 Refreshed My Excel Knowledge:** Refreshed my excel knowledge, cementing it in my mind!

**📊 Data Aggregation:** Got cozy with GROUP BY and turned aggregate functions like COUNT() and AVG() into my data-summarizing sidekicks.

**💡 Analytical Wizardry:** Improved my real-world puzzle-solving skills, turning questions into actionable, insightful SQL queries.
# Conclusions
From the analysis, several general insights emerged:

## Insights
- **Top-Paying Data Analyst Jobs:** The highest-paying jobs for data analysts that allow remote work offer a wide range of salaries, the highest at $650,000!

- **Skills for Top-Paying Jobs:** High-paying data analyst jobs require advanced proficiency in SQL, suggesting it’s a critical skill for earning a top salary.
**Most In-Demand Skills:** SQL is also the most demanded skill in the data analyst job market, thus making it essential for job seekers.

- **Skills with Higher Salaries:** Specialized skills, such as SVN and Solidity, are associated with the highest average salaries, indicating a premium on niche expertise.

- **Optimal Skills for Job Market Value:** SQL leads in demand and offers for a high average salary, positioning it as one of the most optimal skills for data analysts to learn to maximize their market value.

# Closing Thoughts
This project enhanced my SQL skills and provided valuable insights into the data analyst job market. The findings from the analysis serve as a guide to prioritizing skill development and job search efforts. Aspiring data analysts can better position themselves in a competitive job market by focusing on high-demand, high-salary skills. This exploration highlights the importance of continuous learning and adaptation to emerging trends in the field of data analytics.