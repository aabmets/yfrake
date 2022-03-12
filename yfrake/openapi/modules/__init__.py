# ================================================================================== #
#   __init__.py - This file is part of the yfrake package.                           #
# ================================================================================== #
#                                                                                    #
#   MIT License                                                                      #
#                                                                                    #
#   Copyright (c) 2022 Mattias Aabmets                                               #
#                                                                                    #
#   Permission is hereby granted, free of charge, to any person obtaining a copy     #
#   of this software and associated documentation files (the "Software"), to deal    #
#   in the Software without restriction, including without limitation the rights     #
#   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell        #
#   copies of the Software, and to permit persons to whom the Software is            #
#   furnished to do so, subject to the following conditions:                         #
#                                                                                    #
#   The above copyright notice and this permission notice shall be included in all   #
#   copies or substantial portions of the Software.                                  #
#                                                                                    #
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR       #
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,         #
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE      #
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER           #
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,    #
#   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE    #
#   SOFTWARE.                                                                        #
#                                                                                    #
# ================================================================================== #
from pathlib import Path
from importlib import util


# ================================================================================== #
# Here we collect all the modules from the current folder, load them,
# and add them to the modules list, which is then used by the generator.py
# module to generate the 'yfrake_spec.yaml' file.

modules = list()
param_specs = dict()

folder = Path(__file__).parent
for file_path in folder.iterdir():
    module_name = file_path.stem
    if '__' not in str(module_name):
        spec = util.spec_from_file_location(
            module_name, file_path)
        module = util.module_from_spec(spec)
        spec.loader.exec_module(module)
        modules.append(module)

        # generating endpoint param specs, which is
        # used by validate_input func in validators.py.
        module_params = dict()
        for param in getattr(module, 'parameters'):
            item = {param['name']: param['schema']['type']}
            module_params.update(item)

        param_specs[module_name] = module_params
