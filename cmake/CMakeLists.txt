cmake_minimum_required(VERSION 3.10)

# set the project name
project(Demo VERSION 2.0)

# add the executable
# add_executable(hello hello.cpp)

# 查找当前目录下的所有源文件
# 并将名称保存到 DIR_SRCS 变量
aux_source_directory(. DIR_SRCS)

# 添加 math 子目录
add_subdirectory(math)

# 指定生成目标 
add_executable(Demo main.cpp)

# 添加链接库
target_link_libraries(Demo MathFunctions)


# specify the C++ standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)