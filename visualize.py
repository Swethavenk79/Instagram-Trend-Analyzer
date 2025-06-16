import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the extracted data
df = pd.read_csv("instagram_data.csv")

# Plot Likes
plt.figure(figsize=(10, 5))
sns.barplot(x="profile", y="likes", data=df, ci=None)
plt.title("Total Likes per Profile")
plt.xticks(rotation=45)
plt.show()

# Plot Comments
plt.figure(figsize=(10, 5))
sns.barplot(x="profile", y="comments", data=df, ci=None)
plt.title("Total Comments per Profile")
plt.xticks(rotation=45)
plt.show()