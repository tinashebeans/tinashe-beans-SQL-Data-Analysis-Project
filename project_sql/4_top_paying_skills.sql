/*
    Qeustion: What are the top paying skills ased on salary?
    -Look at the average salary associated with each skill for Data Analyst roles
    - Focus on specified salaries regardless of location
    -Why? It reveals how skills impact salary levels for Data Analysts an
            it identifies the most financially rwarding skills to learn or improve
*/    

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
LIMIT 25