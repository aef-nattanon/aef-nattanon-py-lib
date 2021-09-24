# aef-nattanon-py-lib
## Install

```bash
$ pip install aefNattanon
```

## Simple Demo

```python
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# Import Multiplication from your library
import aef-nattanon-py as aef
from medium_multiply.multiplication import Multiplication
from my_example.photoExample import PhotoExample

# Instantiate a Multiplication object
multiplication = aef.Multiplication(2)

# Call the multiply method
print(multiplication.multiply(5))


byExample = aef.PhotoExample('coco.names', 'yolov3-tiny.cfg', 'yolov3-tiny.weights')
byExample.show_by_photo('my-photo.jpeg')

```