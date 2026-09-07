"""Read and plot companies.csv"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_path = '/Users/sd/Documents/APAN5400/data/companies.csv'

def load_data(data_path):
    """Returns a dataframe from the data path"""
    return pd.read_csv(data_path)

def clean_data(df):
    """Returns int for select string ints"""
    return df.astype({'revenue': int, 'employees': int})
def sort_data(df, sort_by, ascending=False):
    """Returns a sorted dataframe by revenue"""
    return df.sort_values(by=sort_by, ascending=ascending)

def scatter_plot(x,y,xlabel,ylabel):
    """Returns a scatter plot of the data"""
    plt.scatter(x,y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title('Scatter Plot')
    plt.show()

def log_fit_plot_alternate(x, y, x_label, y_label):
    """Fit a polynomial log(y) and plot the log line.
    np.linspace gives increasing x, and 200 points make y = m·ln(x) + c look smooth. 
    Scatter still uses the real data; only the line uses the grid."""
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)

    slope, intercept = np.polyfit(np.log(x), y, 1)

    x_line = np.linspace(x.min(), x.max(), 200)
    y_line = slope * np.log(x_line) + intercept

    plt.figure(figsize=(8, 5))
    plt.scatter(x, y, color='darkorange', alpha=0.7, label='Data Points')
    plt.plot(
        x_line, y_line, color='royalblue', linewidth=2.5,
        label=f'Log Fit: y = {slope:.2f}*ln(x) + {intercept:.2f}',
    )
    plt.title("Scatter Plot with Logarithmic Fit Line", fontsize=14)
    plt.xlabel(x_label, fontsize=12)
    plt.ylabel(y_label, fontsize=12)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()

def formatter(x, pos):
    """A function to divide values by 1 million"""
    return str(round(x / 1e6, 1)) + " million"

def log_fit_plot(x, y, x_label, y_label):
    """Fit a first-degree polynomial (a line) to log(x) and y. This finds the slope (m) and intercept (c) 
    for the equation: y = m * log(x) + c. Calculate the predicted Y values for the fit line. 
     Plot the original scatter points. Plot the logarithmic trend line"""
    slope, intercept = np.polyfit(np.log(x), y, 1)
    y_fit = slope * np.log(x) + intercept
    plt.figure(figsize=(8, 5))
    plt.scatter(x, y, color='darkorange', alpha=0.7, label='Data Points')
    plt.plot(x, y_fit, color='royalblue', linewidth=2.5, label=f'Log Fit: y = {slope:.2f}*ln(x) + {intercept:.2f}')
    plt.title("Scatter Plot with Logarithmic Fit Line", fontsize=14)
    plt.ticklabel_format(useOffset=False, style='plain') #remove scientific notation
    plt.gca().get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:.1f}".format(x / 1000000)))
    plt.xlabel(x_label, fontsize=12)
    plt.ylabel(y_label, fontsize=12)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()

def main():
    df = load_data(data_path)
    print(df.columns)
    print(df.shape)
    df = clean_data(df)
    df = sort_data(df, sort_by='revenue', ascending=False)
    print("Sorted by revenue")
    print(df[['revenue','employees']])
    scatter_plot( df['revenue'],df['employees'], "Revenue","Employees")
    #log_fit_plot_alternative(df['employees'], df['revenue'],"Employees (000s)", "Revenue (000s)" )
    log_fit_plot(df['revenue'],df['employees'], "Revenue","Employees (million)" )


if __name__ == "__main__":
    main()
