import tensorflow as tf

import numpy as np
import os
import time

def generate(text):
  states = None
  next_char = tf.constant([text])
  result = [next_char]
  one_step_reloaded = tf.saved_model.load('one_step')
  for n in range(100):
    
    next_char, states = one_step_reloaded.generate_one_step(next_char, states=states)
    if next_char=='C':
      break
    result.append(next_char)


  return tf.strings.join(result)[0].numpy().decode("utf-8")



