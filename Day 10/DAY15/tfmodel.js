const model = tf.sequential();

//model.add(tf.layers.dense({units: 1, inputShape: [1]}));
model.add(tf.layers.dense({units: 64, inputShape: [1]}));
model.add(tf.layers.dense({units: 1, inputShape: [64]}));
model.compile({loss: 'meanSquaredError', optimizer: 'sgd'});

const xs = tf.tensor2d([[1], [2], [3], [4], [5]]);
const ys = tf.tensor2d([[2], [4], [6], [8], [10]]);

model.fit(xs, ys, {epochs:150});
result=model.predict(tf.tensor2d([6],[1,1])).dataSync();

console.log(result);