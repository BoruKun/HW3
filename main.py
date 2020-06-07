# Import statements
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# Set up the randomizer for reproducibility
# Initialize the data
np.random.seed(1000)
data_methods = pd.read_excel('./tests_meta_analysis.xls')

elisa_data = [data_methods['Sensitivity (95% CI) '][0:6], data_methods['Specificity (95% CI) '][0:6]]
lfia_data = [data_methods['Sensitivity (95% CI) '][6:16], data_methods['Specificity (95% CI) '][6:16]]
clia_data = [data_methods['Sensitivity (95% CI) '][16:22], data_methods['Specificity (95% CI) '][16:22]]

fig, ax = plt.subplots(nrows=2, ncols=3, figsize=(16, 8))

for dummy_i in range(3):
    ax[0][dummy_i].set_ylabel('Sensitivity values')
    ax[1][dummy_i].set_ylabel('Specificity values')
    ax[0][dummy_i].grid(), ax[1][dummy_i].grid()

elisa_sensitivities = sorted([float(elisa_data[0][dummy_i][0:5]) for dummy_i in range(0, 6)])
lfia_sensitivities = sorted([float(lfia_data[0][dummy_i][0:5]) for dummy_i in range(6, 16)])
clia_sensitivities = sorted([float(clia_data[0][dummy_i][0:5]) for dummy_i in range(16, 22)])
elisa_specificities = sorted([float(elisa_data[1][dummy_i][0:5]) for dummy_i in range(0, 6)])
lfia_specificities = sorted([float(lfia_data[1][dummy_i][0:5]) for dummy_i in range(6, 16)])
clia_specificities = sorted([float(clia_data[1][dummy_i][0:5]) for dummy_i in range(16, 22)])

sns.swarmplot(data=elisa_sensitivities, ax=ax[0, 0])
sns.boxplot(data=elisa_sensitivities, ax=ax[0, 0], width=0.2, color='lightgreen')
ax[0][0].set_xlabel('ELISA sensitivity data points')
ax[0][0].set_xticks(ticks=[])

sns.swarmplot(data=lfia_sensitivities, ax=ax[0, 1])
sns.boxplot(data=lfia_sensitivities, ax=ax[0, 1], width=0.2, color='lightgreen')
ax[0][1].set_xlabel('LFIA sensitivity data points')
ax[0][1].set_xticks(ticks=[])

sns.swarmplot(data=clia_sensitivities, ax=ax[0, 2])
sns.boxplot(data=clia_sensitivities, ax=ax[0, 2], width=0.2, color='lightgreen')
ax[0][2].set_xlabel('CLIA sensitivity data points')
ax[0][2].set_xticks(ticks=[])

sns.swarmplot(data=elisa_specificities, ax=ax[1, 0])
sns.boxplot(data=elisa_specificities, ax=ax[1, 0], width=0.2, color='lightgreen')
ax[1][0].set_xlabel('ELISA specificity data points')
ax[1][0].set_xticks(ticks=[])

sns.swarmplot(data=lfia_specificities, ax=ax[1, 1])
sns.boxplot(data=lfia_specificities, ax=ax[1, 1], width=0.2, color='lightgreen')
ax[1][1].set_xlabel('LFIA specificity data points')
ax[1][1].set_xticks(ticks=[])

sns.swarmplot(data=clia_specificities, ax=ax[1, 2])
sns.boxplot(data=clia_specificities, ax=ax[1, 2], width=0.2, color='lightgreen')
ax[1][2].set_xlabel('CLIA specificity data points')
ax[1][2].set_xticks(ticks=[])

fig.suptitle('Methods analytical performance in detection of SARS-CoV-2 antibodies')

#plt.tight_layout()
plt.show()