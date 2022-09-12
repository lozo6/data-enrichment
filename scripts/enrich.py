import pandas as pd
import numpy as np

# assign a variable for dataset
hospital = pd.read_csv('data/Hospital_Inpatient_Discharges__SPARCS_De-Identified___2015.csv')
adi = pd.read_csv('data/NY_2015_ADI_9 Digit Zip Code_v3.1.csv')

# print column names
print(hospital.columns)
print(adi.columns)

# added smaller version of data
df_hospital_small = hospital[['Health Service Area', 'Hospital County', 'Zip Code - 3 digits']]
df_adi_small = adi[['ZIPID']]

# clean up column names and values
df_hospital_small.columns = df_hospital_small.columns.str.replace('[^A-Za-z0-9]+', '_').str.lower().str.strip()
df_adi_small.columns = df_adi_small.columns.str.replace('[^A-Za-z0-9]+', '_').str.lower().str.strip()

needsChange_hospital = df_hospital_small.select_dtypes(object).columns
df_hospital_small[needsChange_hospital] = df_hospital_small[needsChange_hospital].apply(lambda x : x.str.replace('[^A-Za-z0-9]+', '_').str.lower().str.strip())

needsChange_adi = df_adi_small.select_dtypes(object).columns
df_adi_small[needsChange_adi] = df_adi_small[needsChange_adi].apply(lambda x : x.str.replace('[^A-Za-z0-9]+', '_').str.lower().str.strip())

# df_adi_small['zipid'] = df_adi_small['zipid'].str.slice(start=1, stop=4)

#print a small sample and number of rows and columns
print(df_hospital_small.sample(10).to_markdown())
print(df_adi_small.sample(10).to_markdown())

# now combining small versions into one csv
# df_sparcs = df_hospital_small.merge(df_adi_small, how='left', left_on='zip_code_3_digits', right_on='zipid')
# df_sparcs = pd.merge(df_hospital_small, df_adi_small,how='left', left_on='zip_code_3_digits', right_on='zipid')

df_sparcs = pd.concat([df_hospital_small, df_adi_small])

print(df_sparcs.sample(10).to_markdown())

# save to file
df_sparcs.to_csv('data/sparcs.csv')
print(df_sparcs.shape)