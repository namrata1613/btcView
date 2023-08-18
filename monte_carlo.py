import numpy as np
import pandas as pd
import talib
import matplotlib.pyplot as plt
import csv
from numpy import genfromtxt



data = genfromtxt('daily.csv', delimiter=',')
historical_prices = data[:,4]

initial_price = historical_prices[0]
num_iterations = 100
forecast_period = 30

short_sma_period = 20
long_sma_period = 50
short_sma = talib.SMA(historical_prices, timeperiod=short_sma_period)
long_sma = talib.SMA(historical_prices, timeperiod=long_sma_period)


historical_returns = np.diff(historical_prices) / historical_prices[:-1]

# Monte Carlo 
simulated_prices = np.empty((num_iterations, forecast_period))
for i in range(num_iterations):
    simulated_returns = np.random.choice(historical_returns, size=forecast_period)
    simulated_prices[i] = historical_prices[-1] * np.cumprod(1 + simulated_returns)


plt.figure(figsize=(10, 6))
plt.plot(historical_prices, label='Historical Prices')
plt.plot(np.arange(len(historical_prices), len(historical_prices) + forecast_period), simulated_prices.T, color='gray', alpha=0.1)
plt.plot(np.arange(len(historical_prices), len(historical_prices) + forecast_period), np.mean(simulated_prices, axis=0), color='blue', label='Mean Simulation')
plt.plot(np.arange(len(historical_prices), len(historical_prices) + forecast_period), short_sma[-1] * np.ones(forecast_period), color='red', label=f'SMA-{short_sma_period}')
plt.plot(np.arange(len(historical_prices), len(historical_prices) + forecast_period), long_sma[-1] * np.ones(forecast_period), color='green', label=f'SMA-{long_sma_period}')
plt.xlabel('Days')
plt.ylabel('Price')
plt.title('Monte Carlo with SMA Crossover')
plt.legend()
plt.show()

mean_simulated_prices = np.mean(simulated_prices, axis=0)
std_dev_simulated_prices = np.std(simulated_prices, axis=0)
percentiles = np.percentile(simulated_prices, [10, 50, 90], axis=0)


print(f"Mean simulated prices: {mean_simulated_prices}")
print(f"Standard deviation of simulated prices: {std_dev_simulated_prices}")
print("Percentiles of simulated prices:")
print(f"10th percentile: {percentiles[0]}")
print(f"50th percentile (median): {percentiles[1]}")
print(f"90th percentile: {percentiles[2]}")

# Defining potential price target scenarios
target_percentage_increase = 10  
target_percentage_decrease = 5   

# Calculating potential price targets based on scenarios
target_prices_increase = historical_prices[-1] * (1 + target_percentage_increase / 100)
target_prices_decrease = historical_prices[-1] * (1 - target_percentage_decrease / 100)


print(f"Potential price target (increase by {target_percentage_increase}%): {target_prices_increase}")
print(f"Potential price target (decrease by {target_percentage_decrease}%): {target_prices_decrease}")
