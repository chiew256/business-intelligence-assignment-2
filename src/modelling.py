import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the data from the CSV file
df = pd.read_csv('./output/merged.csv')

# Group the data by 'Element'
grouped = df.groupby('Element')

# Get the data for 'Standard Deviation' and 'Temperature Change'
std_dev = grouped.get_group('Standard Deviation')
temp_change = grouped.get_group('Temperature change')

# Define a function to perform linear regression
def perform_linear_regression(df):
    # Define the feature variables and the target variable
    X = df[['Total', 'Coal', 'Oil', 'Gas', 'Cement', 'Flaring', 'Other']]
    y = df['Value']

    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create a Linear Regression object
    model = LinearRegression()

    # Train the model
    model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f'Mean Squared Error: {mse}')
    print(f'R-squared: {r2}')

# Perform linear regression on the 'Standard Deviation' data
print("Linear Regression for 'Standard Deviation':")
perform_linear_regression(std_dev)

# Perform linear regression on the 'Temperature change' data
print("\nLinear Regression for 'Temperature change':")
perform_linear_regression(temp_change)