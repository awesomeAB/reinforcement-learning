import keras
from keras.models import load_model
import matplotlib.pyplot as plt
from agent.agent import Agent
from functions import *
import sys
import time

# if len(sys.argv) != 3:
# 	print("Usage: python evaluate.py [stock] [model]")
# 	exit()


# stock_name, model_name = sys.argv[1], sys.argv[2]
def trade(stock_name = '^NSEI'):
	model_name = 'model_ep100'
	model = load_model("models/" + model_name)
	window_size = model.layers[0].input.shape.as_list()[1]

	agent = Agent(window_size, True, model_name)
	data = getStockDataVec(stock_name)
	l = len(data) - 1
	batch_size = 32

	state = getState(data, 0, window_size + 1)
	total_profit = 0
	agent.inventory = []

	# plot data
	stock_data = []
	buy_x = []
	buy_y = []
	sell_x = []
	sell_y = []

	plt.plot(stock_data, color="#5b5b5b", label=stock_name)
	plt.scatter(buy_x, buy_y, color="#4edd46", label="Buy")
	plt.scatter(sell_x, sell_y, color="#ff2626", label="Sell")

	for t in range(l):
		action = agent.act(state)
		stock_data.append(data[t])

		# sit
		next_state = getState(data, t + 1, window_size + 1)
		reward = 0
		# print(action)
		# time.sleep(0.1)
		if action == 1:  # buy
			agent.inventory.append(data[t])
			buy_x.append(t)
			buy_y.append(data[t])
			print("Buy: " + formatPrice(data[t]))

		elif action == 2 and len(agent.inventory) > 0:  # sell
			sell_x.append(t)
			sell_y.append(data[t])
			bought_price = agent.inventory.pop(0)
			reward = max(data[t] - bought_price, 0)
			total_profit += data[t] - bought_price
			print("Sell: " + formatPrice(data[t]) + " | Profit: " + formatPrice(data[t] - bought_price))

		done = True if t == l - 1 else False
		agent.memory.append((state, action, reward, next_state, done))
		state = next_state

		plt.plot(stock_data, color="#5b5b5b")
		plt.scatter(buy_x, buy_y, color="#4edd46")
		plt.scatter(sell_x, sell_y, color="#ff2626")
		plt.savefig('foo.png', bbox_inches='tight', dpi=200)

		if done:
			print("--------------------------------")
			print(stock_name + " Total Profit: " + formatPrices(total_profit))
			print("--------------------------------")

	# plt.plot(data, label=stock_name)
	# plt.scatter(buy_x, buy_y, color="green", label="Buy")
	# plt.scatter(sell_x, sell_y, color="red", label="Sell")
	# # plt.savefig('foo.png')
	plt.legend()
	plt.show()