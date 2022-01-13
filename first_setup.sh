# Copyright 2022 Franklin Selva. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

echo "INSTALLING UPF AND PLANNERS"
rm -rf upf && git clone https://github.com/aiplan4eu/upf && pip install upf/
rm -rf tamer-upf && git clone https://github.com/aiplan4eu/tamer-upf && pip install tamer-upf/
rm -rf pyperplan-upf && git clone https://github.com/aiplan4eu/pyperplan-upf && pip install pyperplan-upf/
pip install -r requirements.txt

echo "GENERATING PYTHON PROTO PARSER"
python -m grpc_tools.protoc -I=./python/ --python_out=./python --grpc_python_out=./python/  ./python/upf.proto

echo "GENERATING RUST PROTO PARSER"
cargo build