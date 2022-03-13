# ==================================================================================== #
#    thread_loop.py - This file is part of the YFrake package.                         #
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
from threading import Thread
import asyncio
import time


# ==================================================================================== #
class ThreadLoop:
    """
    This class is responsible for running a separate
    async event loop in a thread, when the YFrake
    client is being used in the sync mode.
    """
    loop: asyncio.AbstractEventLoop = None
    thread: Thread = None

    # ------------------------------------------------------------------------------------ #
    @classmethod
    def run_background_thread(cls) -> None:
        asyncio.set_event_loop(cls.loop)
        cls.loop.run_forever()

    # ------------------------------------------------------------------------------------ #
    @classmethod
    def start_thread_loop(cls) -> None:
        ThreadLoop.loop = asyncio.new_event_loop()
        cls.thread = Thread(target=cls.run_background_thread, daemon=True)
        cls.thread.start()

    # ------------------------------------------------------------------------------------ #
    @classmethod
    def stop_thread_loop(cls) -> None:
        force_iter = True
        cls.loop.call_soon_threadsafe(cls.loop.stop)
        while force_iter or cls.loop.is_running():
            force_iter = False
            time.sleep(0)
        cls.loop.close()
        cls.thread.join()
