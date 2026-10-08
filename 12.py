import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

array = np.array([27, 50, 44, 6, 58, 61, 23, 86, 67, 20, 75, 7, 79, 61, 90, 54])
print("Array:\n", array)
print("Mean:", array.mean())
print("25th Percentile:", np.percentile(array, 25))
print("50th Percentile:", np.percentile(array, 50))
print("75th Percentile:", np.percentile(array, 75))
print("100th Percentile:", np.percentile(array, 100))

def outDetection(arr):
    Q1, Q3 = np.percentile(arr, [25, 75])
    IQR = Q3 - Q1
    lr = Q1 - (1.5 * IQR)
    ur = Q3 + (1.5 * IQR)
    return lr, ur

lr, ur = outDetection(array)
print(f"Lower Range: {lr}, Upper Range: {ur}")

sns.displot(array)
plt.title("Distribution Plot of Array")
plt.show()

sns.histplot(array, kde=True)
plt.title("Histogram & KDE of Array")
plt.show()

new_array = array[(array > lr) & (array < ur)]
print("New Array after removing outliers:\n", new_array)

sns.displot(new_array)
plt.title("Distribution Plot after Filtering")
plt.show()

lr1, ur1 = outDetection(new_array)
print(f"Recalculated Lower Range: {lr1}, Upper Range: {ur1}")

final_array = new_array[(new_array > lr1) & (new_array < ur1)]
print("Final Array:\n", final_array)

sns.histplot(final_array, kde=True)
plt.title("Final Array Distribution")
plt.show()