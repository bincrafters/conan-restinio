project(test_package CXX)
cmake_minimum_required(VERSION 3.1.2)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(${CMAKE_PROJECT_NAME} test_package.cpp)
target_link_libraries(${CMAKE_PROJECT_NAME} ${CONAN_LIBS})
target_compile_features(${CMAKE_PROJECT_NAME} PRIVATE cxx_std_14)