# ================================================================================== #
#   generator.py - This file is part of the yfrake package.                          #
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
from .components import components
from .modules import modules
from . import utils
import tomli
import yaml
import copy


yfrake_spec = {
    'openapi': '3.0.0',
    'info': {},
    'paths': {},
    'components': components
}


# ================================================================================== #
def generate_openapi_spec() -> None:
    """
    Poetry dependency manager uses this function to
    generate the 'yfrake_spec.yaml' file, before the
    package is published to the PyPI.
    """
    for module in modules:
        spec = {
            'summary': module.summary,
            'description': module.description,
            'parameters': _build_parameters(module),
            'responses': _build_responses()
        }
        endpoint = '/' + module.summary.lower().replace(' ', '_')
        yfrake_spec['paths'].update({endpoint: {'get': spec}})
        yfrake_spec['info'].update(_build_info())

    path = utils.get_spec_file_path()
    with open(path, 'w', encoding='utf-8') as file:
        file.write(yaml.dump(yfrake_spec))

    print('OpenAPI yaml file has been built.')


# ---------------------------------------------------------------------------------- #
def _build_parameters(module) -> list:
    """
    This function is responsible for building the
    parameters section of the documentation.
    """
    parameters = list()
    for param in module.parameters:
        param = copy.deepcopy(param)
        _type: object = param['schema']['type']
        _type: str = utils.get_openapi_datatype(_type)
        param['schema']['type'] = _type
        parameters.append(param)
    return parameters


# ---------------------------------------------------------------------------------- #
def _build_responses() -> dict:
    """
    This function is responsible for building the
    responses section of the documentation.
    """
    # Note: Currently, only the base response is being set for each endpoint,
    # because the recursive function required to build the response models
    # in the correct yaml format was taking too much time to design.
    # This deficiency is somewhat mitigated by the fact that the
    # swagger openapi server allows performing test queries, from
    # which the response model of each endpoint can be examined.
    return {
        '200': {
            'description': 'Successful Request',
            'content': {
                'application/json': {
                    'schema': {
                        '$ref': '#/components/schemas/BaseResponse'
                    }
                }
            }
        }
    }


# ---------------------------------------------------------------------------------- #
def _build_info() -> dict:
    """
    This function is responsible for building the
    information section of the documentation.
    """
    with open(utils.get_toml_file_path(), "rb") as file:
        data = tomli.load(file)
    data = data['tool']['poetry']
    contact = data['authors'][0].split()
    email = contact.pop().strip('<>')
    name = ' '.join(contact)
    url = data['urls']['Homepage']
    return {
        'title': data['name'],
        'version': data['version'],
        'description': data['description'],
        'contact': {
            'name': name,
            'email': email,
            'url': url
        },
        'license': {
            'name': data['license'],
            'url': url + '/blob/main/LICENSE'
        }
    }
