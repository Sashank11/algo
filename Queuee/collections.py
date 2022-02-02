from collections import deque
# front and back compatibility with or without maxlen and has o(1) compexity
custom_queue = deque(maxlen = 3)
print(custom_queue)
custom_queue.append(1)
custom_queue.append(2)
custom_queue.append(3)
custom_queue.append(4)
print(custom_queue)
print(custom_queue.clear())
print(custom_queue)