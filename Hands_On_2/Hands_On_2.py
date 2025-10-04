import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  

np.random.seed(42) 

# Generate realistic engine sizes and corresponding CO2 emissions 
# 100 engine sizes from 1.5 to 4.5 
engine_sizes = np.linspace(1.5, 4.5, 100)   
slope = 60  
intercept = 50  

# Adding random noise
noise = np.random.normal(0, 15, size=engine_sizes.shape)  
co2_emissions = slope * engine_sizes + intercept + noise  

# Create a DataFrame  
df = pd.DataFrame({'Engine_size': engine_sizes,  
                   'CO2_Emissions': co2_emissions})

df.head()

# Prepare the plot  
fig, axs = plt.subplots(2, 2, figsize=(10, 8))  
legend_properties = {'weight': 'bold'}  

# Define the different a and b parameters for the plots  
params = [  
    (10, 15, 'r'),  
    (20, 25, 'y'),  
    (30, 35, 'g'),  
    (65, 15, 'k')  
]  

# Loop through and create each subplot  
for i, ax in enumerate(axs.flatten()):  
    a, b, color = params[i]  
    x = np.linspace(1.5, 4.5, 100)  # Define the range for Engine_size  
    
    # Scatter plot  
    x_scatter = df['Engine_size']  
    y_scatter = df['CO2_Emissions']  
    ax.scatter(x_scatter, y_scatter, edgecolors='b', linewidths=4.)  
    
    # Linear regression line  
    y = a * x + b  
    ax.plot(x, y, color, label=f'a = {a}, b = {b}')  
    
    # Labels and grid  
    ax.set_xlabel('Engine Size')  
    ax.set_ylabel('CO2 Emissions')  
    ax.legend(prop=legend_properties)  
    ax.grid(alpha=0.5)  
    ax.set_title(f'Plot {i + 1}')  

# Adjust layout  
plt.tight_layout()  
plt.show()