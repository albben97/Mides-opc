Mides-opc
====================

Example of Sequence Planner controlling some simulated resources.

Requirements:
-----------------
1. [ROS2 Galactic](https://docs.ros.org/en/foxy/Releases/Release-Galactic-Geochelone.html)
2. [Colcon](https://colcon.readthedocs.io/en/released/user/installation.html)
3. [Rust](https://rustup.rs/)
4. [NuXmv](https://nuxmv.fbk.eu)
5. [llvm and clang](https://rust-lang.github.io/rust-bindgen/requirements.html#clang)
6. [lark](https://pypi.org/project/lark/)
7. [cargo](https://doc.rust-lang.org/cargo/getting-started/installation.html) 
8. [opcua](https://github.com/FreeOpcUa/opcua-asyncio)
9. [sbt](https://www.scala-sbt.org/download.html)
10. [UaBrowser(Optional)](https://www.prosysopc.com/products/opc-ua-browser/)

Make sure NuXmv is extracted in the working directory. There is no installation other than extracting the zip-file.
UaBrowser is a helpful tool to track the value of the variables on the OPC server.

Building:
-----------------
Source the project
```
. /opt/ros/galactic/setup.bash
```

Build
```
colcon build
```

Alternatively if sp-rust gives too many problems build with:
```
colcon build --packages-ignore sp-rust-ui
```

Install
```
. install/setup.bash
```

To rebuild the generated Rust messages, you can run:
```
colcon build --cmake-args -DCARGO_CLEAN=ON
```

__TODO:__ Look over all commands for running. How to setup server?
Running:
-----------------

Open a new terminal window and start the OPC server:
```
cd opcua-asyncio/examples
python3 server-minimal_copy.py
```

(Optional) Open a new terminal window and start the UaBrowser
```
cd ../..
cd opt/prosync-opc-ua-browser
. UaBrowser
```
In the UaBrowser connect to opc.tpc://127.0.0.1:4848 and select which variables to monitor.

Open a new terminal window and run the simulation
```
. install/setup.bash
ros2 launch dorna_example test.launch.py
```
Open a new terminal window and run Mides
```
sbt mides/run
```

Useful tools:
-----------------
[prosysopc, for visualizing opc](https://www.prosysopc.com/products/opc-ua-browser/)

To export graph image from .dot to .ps file use 
```
dot -Tps file.dot file.ps
```

