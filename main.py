# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# Import Multiplication from your library
from medium_multiply.multiplication import Multiplication
from my_example.photoExample import PhotoExample


if __name__ == '__main__':
    byExample = PhotoExample('coco.names', 'yolov3-tiny.cfg', 'yolov3-tiny.weights')
    byExample.show_by_photo('my-photo.jpeg')
    # Instantiate a Multiplication object
    multiplication = Multiplication(2)

    # Call the multiply method
    print(multiplication.multiply(5))
