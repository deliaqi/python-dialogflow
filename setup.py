# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import io
import os

import setuptools

name = "dialogflow"
description = "Client library for the Dialogflow API"
version = "2.16.1"
release_status = "Development Status :: 5 - Production/Stable"
dependencies = [
    "google-api-core[grpc] >= 1.32.0, <3.0.0dev,!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*",
    "proto-plus >= 1.22.0, <2.0.0dev",
    "protobuf>=3.19.5,<5.0.0dev,!=3.20.0,!=3.20.1,!=4.21.0,!=4.21.1,!=4.21.2,!=4.21.3,!=4.21.4,!=4.21.5",
]

package_root = os.path.abspath(os.path.dirname(__file__))

readme_filename = os.path.join(package_root, "README.rst")
with io.open(readme_filename, encoding="utf-8") as readme_file:
    readme = readme_file.read()

packages = setuptools.PEP420PackageFinder.find()

setuptools.setup(
    name="google-cloud-dialogflow",
    description=description,
    long_description=readme,
    version=version,
    author="Google LLC",
    author_email="googleapis-packages@google.com",
    license="Apache 2.0",
    url="https://github.com/googleapis/dialogflow-python-client-v2",
    classifiers=[
        release_status,
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    platforms="Posix; MacOS X; Windows",
    packages=packages,
    extras={"libcst": "libcst >=0.2.5"},
    scripts=[
        "scripts/fixup_dialogflow_v2_keywords.py",
        "scripts/fixup_dialogflow_v2beta1_keywords.py",
    ],
    install_requires=dependencies,
    python_requires=">=3.7",
    include_package_data=True,
    zip_safe=False,
)
