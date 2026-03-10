import matplotlib.pyplot as plt
import seaborn as sns

def demographic_analysis(df):

    sns.countplot(x='gender', data=df)
    plt.title("Gender Distribution")
    plt.show()

    sns.boxplot(x='gender', y='math_score', data=df)
    plt.title("Math Score by Gender")
    plt.show()
