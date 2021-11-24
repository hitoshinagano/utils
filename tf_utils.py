import tensorflow as tf
from datetime import datetime
import os

def create_tensorboard(dir_name, experiment_name):
  log_dir = os.path.join(dir_name, experiment_name, datetime.now().strftime("%Y%m%d %H%M%S"))
  tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir)

  print(f"TensorBoard dir: {log_dir}")
  return tensorboard_callback
