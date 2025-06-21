import pandas as pd
import numpy as np

# Step 1: Create initial DataFrame with 10 rows and 5 columns
df = pd.DataFrame(np.random.randint(1, 100, size=(10, 5)),
                  columns=['A', 'B', 'C', 'D', 'E'])

# Step 2: Append 10 more rows (first time)
df_append1 = pd.DataFrame(np.random.randint(1, 100, size=(10, 5)),
                          columns=['A', 'B', 'C', 'D', 'E'])
df = pd.concat([df, df_append1], ignore_index=True)

# Step 3: Append 10 more rows (second time)
df_append2 = pd.DataFrame(np.random.randint(1, 100, size=(10, 5)),
                          columns=['A', 'B', 'C', 'D', 'E'])
df = pd.concat([df, df_append2], ignore_index=True)

# Step 4: Export to CSV
df.to_csv('data/output.csv', index=False)

print("DataFrame exported to output.csv")
