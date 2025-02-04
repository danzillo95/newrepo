import tensorflow as tf


ten = tf.constant(3)
ten1 = tf.constant(5)
x =10

# print(tf.add(ten, x))
# print(dtype(ten))

var = tf.Variable([2, 5,63], dtype=tf.int16)
var.assign([100,4325,523])

# print(var)

list = [[1,2,3],[4,5,6]]
ten100 = tf.convert_to_tensor(list, dtype=tf.int32)
# print(ten100)

ten5 = tf.zeros([2,3])
ten6 = tf.ones([2,3])
# print(ten5, ten6)

# print(ten100[0, 0])

var[0].assign(25)
# print(var)

var = tf.random.uniform([2,3], minval=10, maxval = 100, dtype = tf.int32)
# print(var)

var3 = tf.random.normal([2,3], mean= 5, stddev=10)
# print(var3)


var4 = tf.random.uniform([2,3], seed = 42)
print(var4)