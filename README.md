# TDS-Project-1
# Dublin GitHub Users Analysis

This project scrapes data from GitHub for users located in Dublin with over 50 followers, along with their repositories. The data is then saved in two CSV files: `users.csv` and `repositories.csv`. Below, we detail the data scraping process, findings from the analysis, and actionable recommendations for developers.

## Data Scraping Process

The data was obtained using the GitHub API, with the following steps:
1. **Identify Users:** We searched for GitHub users in Dublin with over 50 followers.
2. **Collect User Details:** For each user, detailed information including name, company, location, bio, email, and account creation date was fetched.
3. **Retrieve Repositories:** For each user, up to 500 public repositories were obtained with data on stargazers, watchers, language, license, and repository features like projects and wikis.
4. **Data Cleaning:** Company names were trimmed, standardized to uppercase, and cleaned of any leading "@" symbols.

The data extraction process was designed to handle multiple pages of results, ensuring a thorough capture of available data for each user and repository.

## Key Finding

After analyzing the dataset, one of the most interesting insights was the **limited usage of GitHub’s wiki and project features**. Despite these features being available for most repositories, they were often disabled or unused. This may suggest a preference for external documentation tools or a lack of awareness about the benefits of these features on GitHub.

## Actionable Recommendation
For developers, **enabling GitHub’s project and wiki features** could increase the visibility and usability of repositories. Using these features allows contributors and followers to understand project objectives better and collaborate more efficiently. Consider leveraging GitHub wikis for documentation and project boards to manage tasks, especially for open-source projects or repositories with significant follower counts.

## Repository Structure

- `users.csv`: Contains information about each user, including:
  - `login`, `name`, `company`, `location`, `email`, `hireable`, `bio`, `public_repos`, `followers`, `following`, `created_at`
  
- `repositories.csv`: Contains information on each user's public repositories:
  - `login`, `full_name`, `created_at`, `stargazers_count`, `watchers_count`, `language`, `has_projects`, `has_wiki`, `license_name`

## Files in This Repository

- **users.csv**: Data of Dublin-based GitHub users with over 50 followers.
- **repositories.csv**: Information on public repositories of the users in `users.csv`.
- **README.md**: Documentation and findings from the project.
- **data_scraper.py**: Code for data scraping and cleaning.
- **data_analysis.ipynb** (optional): Notebook with visualizations and deeper insights.

---

By exploring this data and enabling GitHub features more effectively, developers can foster stronger communities and make their repositories more attractive to potential collaborators.
