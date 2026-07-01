import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("clean_repos.csv")

# language_counts = df['language'].value_counts()
language_counts = df['language'].value_counts().sort_values(ascending=True)
print(language_counts)

print(language_counts.dropna())

# Drawing a bar chart for the languages used in the repositories

language_counts.dropna().plot(kind='barh', color='skyblue')
plt.title("Languages Used in Repositories")
plt.xlabel("Number of Repositories")
plt.ylabel("Programming Languages")
plt.tight_layout()

try:
    plt.savefig("language_distribution.png")
    print("\nLanguage distribution chart has been saved to 'language_distribution.png'")
except Exception as e:
    print(f"An error occurred while saving the chart: {e}")    

plt.show()




