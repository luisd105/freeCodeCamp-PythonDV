import pandas as pd


def calculate_demographic_data(print_data=True):
    """
    Analyzes demographic data from "adult.data.csv" to calculate various statistics.

    This rewritten version uses more idiomatic pandas operations for better
    performance and readability.
    """
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset?
    # This is already idiomatic pandas.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df.loc[df['sex'] == 'Male', 'age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    # Calculating the mean of a boolean series is a concise way to find the percentage.
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # Create boolean masks for education levels and salary
    higher_education_mask = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education_mask = ~higher_education_mask
    salary_mask = df['salary'] == '>50K'

    # Calculate percentages using the masks and the .mean() trick
    higher_education_rich = round((df.loc[higher_education_mask, 'salary'] == '>50K').mean() * 100, 1)
    lower_education_rich = round((df.loc[lower_education_mask, 'salary'] == '>50K').mean() * 100, 1)
    
    # What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_workers_mask = df['hours-per-week'] == min_work_hours
    rich_percentage = round((df.loc[min_workers_mask, 'salary'] == '>50K').mean() * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    # This vectorized approach is much more efficient than a for loop.
    country_salary_percentage = (df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts()) * 100
    highest_earning_country = country_salary_percentage.idxmax()
    highest_earning_country_percentage = round(country_salary_percentage.max(), 1)
    
    # Identify the most popular occupation for those who earn >50K in India.
    # .mode()[0] is a direct way to get the most frequent value (the mode).
    top_IN_occupation = df.loc[(df['native-country'] == 'India') & (df['salary'] == '>50K'), 'occupation'].mode()[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }