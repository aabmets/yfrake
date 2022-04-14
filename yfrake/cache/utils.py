# ==================================================================================== #
#    utils.py - This file is part of the YFrake package.                               #
# ------------------------------------------------------------------------------------ #
#                                                                                      #
#    MIT License                                                                       #
#                                                                                      #
#    Copyright (c) 2022 Mattias Aabmets                                                #
#                                                                                      #
#    Permission is hereby granted, free of charge, to any person obtaining a copy      #
#    of this software and associated documentation files (the "Software"), to deal     #
#    in the Software without restriction, including without limitation the rights      #
#    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell         #
#    copies of the Software, and to permit persons to whom the Software is             #
#    furnished to do so, subject to the following conditions:                          #
#                                                                                      #
#    The above copyright notice and this permission notice shall be included in all    #
#    copies or substantial portions of the Software.                                   #
#                                                                                      #
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR        #
#    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,          #
#    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE       #
#    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER            #
#    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,     #
#    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE     #
#    SOFTWARE.                                                                         #
#                                                                                      #
# ==================================================================================== #
from .const import DATE_FORMAT, BYTES_OVERHEAD
from datetime import datetime, timedelta
import hashlib
import json


# ==================================================================================== #
def get_request_key(endpoint, params) -> str:
    data_string = ''.join([endpoint, json.dumps(params)])
    _hash = hashlib.sha3_256(data_string.encode())
    return _hash.hexdigest()


# ------------------------------------------------------------------------------------ #
def get_entry_size(response: str) -> int:
    return response.__sizeof__() + BYTES_OVERHEAD


# ------------------------------------------------------------------------------------ #
def get_expiration_date(ttl: float) -> str:
    exp_date = datetime.utcnow() + timedelta(seconds=ttl)
    return date_to_str(exp_date)


# ------------------------------------------------------------------------------------ #
def is_expired(exp_date: str) -> bool:
    exp_date = str_to_date(exp_date)
    return datetime.utcnow() >= exp_date


# ------------------------------------------------------------------------------------ #
def date_to_str(_dt: datetime) -> str:
    return _dt.strftime(DATE_FORMAT)


# ------------------------------------------------------------------------------------ #
def str_to_date(_str: str) -> datetime:
    return datetime.strptime(_str, DATE_FORMAT)


# ------------------------------------------------------------------------------------ #
def megs_to_bytes(megs: int) -> int:
    return megs * 1000000
