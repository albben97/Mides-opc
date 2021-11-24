Mides-opc
====================

Example of Sequence Planner controlling some simulated resources.

Requirements:
-----------------
1. [ROS2 Galactic](https://docs.ros.org/en/foxy/Releases/Release-Galactic-Geochelone.html)
2. [Colcon](https://colcon.readthedocs.io/en/released/user/installation.html)
3. [Rust](https://rustup.rs/)
4. [NuXmv](https://nuxmv.fbk.eu)
5. llvm and clang(https://rust-lang.github.io/rust-bindgen/requirements.html#clang)
6. [lark](https://pypi.org/project/lark/)
7. [cargo](https://doc.rust-lang.org/cargo/getting-started/installation.html) 
8. [opcua](https://github.com/FreeOpcUa/opcua-asyncio)
9. [sbt](https://www.scala-sbt.org/download.html)

Make sure NuXmv is extracted in the working directory. There is no installation other than extracting the zip-file.

__TODO:__ Check in another repo if this is working as intended.
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

Install
```
. install/setup.bash
```

To rebuild the generated Rust messages, you can run:
```
colcon build --cmake-args -DCARGO_CLEAN=ON --packages-skip-by-dep sp-rust-ui
```

__TODO:__ Look over all commands for running. How to setup server?
Running:
-----------------
To launch the opc server enter opc_testing and run:
```
python3 server-minimal.py
```


To launch the simulation run:
```
ros2 launch dorna_example test.launch.py
```

And to run MIDES use:
```
sbt mides/run
```
