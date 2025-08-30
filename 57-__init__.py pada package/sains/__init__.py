# file ini akan dieksekusi ketika memanggil import sains
# disini kegunaan nya untuk import dari folder sains yang telah dipanggil, lalu import lagi ke file matematika.py dan fisika.py
from . import matematika
from . import fisika

# bisa cuman tidak disarankan
# _all__ = [
#     'matematika',
#     'fisika'
# ]