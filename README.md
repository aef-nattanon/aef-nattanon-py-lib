# aef-nattanon-py-lib
## Install

```bash
$ pip install aef-nattanon-py
```

## Simple Demo

```python
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# Import Multiplication from your library
import aef_nattanon_py as aef

# Instantiate a Multiplication object
multiplication = aef.Multiplication(2)

# Call the multiply method
print(multiplication.multiply(5))

byExample = aef.PhotoExample('coco.names', 'yolov3-tiny.cfg', 'yolov3-tiny.weights')
byExample.show_by_photo('my-photo.jpeg')

# or 
import aef_nattanon_py.multiplication as Multiplication
import aef_nattanon_py.photoExample as PhotoExample


# Instantiate a Multiplication object
multiplication = Multiplication(2)

# Call the multiply method
print(multiplication.multiply(5))

byExample = PhotoExample('coco.names', 'yolov3-tiny.cfg', 'yolov3-tiny.weights')
byExample.show_by_photo('my-photo.jpeg')


```