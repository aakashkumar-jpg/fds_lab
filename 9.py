import matplotlib.pyplot as plt
import seaborn as sns

iris = sns.load_dataset('iris')

print(iris.head())
print(iris.info())
print(iris.describe())

sns.countplot(x='species', data=iris)
plt.title('Species Distribution')
plt.show()

sns.scatterplot(x='sepal_length', y='sepal_width', hue='species', data=iris)
plt.title('Sepal Length vs Sepal Width')
plt.show()

sns.scatterplot(x='petal_length', y='petal_width', hue='species', data=iris)
plt.title('Petal Length vs Petal Width')
plt.show()

sns.pairplot(iris, hue='species')
plt.show()

sns.FacetGrid(iris, hue='species', height=5).map(sns.histplot, 'petal_length').add_legend()
plt.title('Petal Length Distribution by Species')
plt.show()

sns.FacetGrid(iris, hue='species', height=5).map(sns.histplot, 'sepal_width').add_legend()
plt.title('Sepal Width Distribution by Species')
plt.show()