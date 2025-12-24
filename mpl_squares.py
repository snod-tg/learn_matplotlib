import matplotlib.pyplot as plt
# 引入相关库

# 创建数组
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# 设置图题并给坐标轴加上标签
ax.set_title("Square Number", fontsize=24)
ax.set_xlabel("Value", fontsize=24)
ax.set_ylabel("Square of Value", fontsize=24)

# 设置刻度标记的样式
ax.tick_params(labelsize=24)

plt.show()
