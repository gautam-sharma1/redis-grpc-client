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

# Import necessary modules/classes from your package
from .redislite import client
#from .redislite_client import redislite_client  # If needed

# Optionally, you can define __all__ to specify what gets imported when using 'from package import *'
__all__ = ['redislite.py']

# Optionally, if you want to specify the version of your package
__version__ = '1.0.0'