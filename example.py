#  /*
#   * MIT License
#   *
#   * Copyright (c) 2024 Gautam Sharma
#   *
#   * Permission is hereby granted, free of charge, to any person obtaining a copy
#   * of this software and associated documentation files (the "Software"), to deal
#   * in the Software without restriction, including without limitation the rights
#   * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#   * copies of the Software, and to permit persons to whom the Software is
#   * furnished to do so, subject to the following conditions:
#   *
#   * The above copyright notice and this permission notice shall be included in all
#   * copies or substantial portions of the Software.
#   *
#   * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#   * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#   * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#   * SOFTWARE.
#   */

#
# Created by Gautam Sharma on 2/19/24.
#

from __future__ import print_function
import logging
from  redisgrpc import redisgrpc as rg
import random
import string
import time

def generate_random_key(length=10):
    """Generate a random string key."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_random_value(length=10):
    """Generate a random string value."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_random_data(num_items):
    """Generate random key-value pairs."""
    data = {}
    for _ in range(num_items):
        key = generate_random_key()
        value = generate_random_value()
        data[key] = value
    return data


def runRedisGrpc(random_data):
    c = rg.Client(50051)
    c.init_connection()
    for k,v in random_data.items():
        c.set(k, v)
        cached_val = c.get(k)

if __name__ == "__main__":
    num_items = 1000
    random_data = generate_random_data(num_items)

    # Run RedisGrpc with 1000 items
    start_time = time.time()
    runRedisGrpc(random_data)
    end_time = time.time()
    print("RedisGrpc took: {}s".format(end_time- start_time))