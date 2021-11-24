Dorna example
====================

Example of Sequence Planner controlling some simulated resources.

Requirements:
-----------------
1. [ROS2 Galactic](https://docs.ros.org/en/foxy/Releases/Release-Galactic-Geochelone.html)
2. [Colcon](https://colcon.readthedocs.io/en/released/user/installation.html)
3. [Rust](https://rustup.rs/)
4. [NuXmv](https://nuxmv.fbk.eu)
5. llvm and clang(https://rust-lang.github.io/rust-bindgen/requirements.html#clang)

Building:
-----------------
Make sure you source and build every repo in the order of sp_msgs, sp-ros and dorna_example using:

```
source /opt/ros/galactic/setup.bash
colcon build
```


```
colcon build
```

To rebuild the generated Rust messages, you can run:
```
colcon build --cmake-args -DCARGO_CLEAN=ON
```

Running:
-----------------

```
ros2 launch dorna_example simulation.launch.py
```
