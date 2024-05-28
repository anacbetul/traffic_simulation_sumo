# CMake generated Testfile for 
# Source directory: /home/betul/ns-allinone-3.41/ns-3.41
# Build directory: /home/betul/ns-allinone-3.41/ns-3.41/cmake-cache
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(ctest-stdlib_pch_exec "ns3.41-stdlib_pch_exec-default")
set_tests_properties(ctest-stdlib_pch_exec PROPERTIES  WORKING_DIRECTORY "/home/betul/ns-allinone-3.41/ns-3.41/cmake-cache/" _BACKTRACE_TRIPLES "/home/betul/ns-allinone-3.41/ns-3.41/build-support/custom-modules/ns3-executables.cmake;47;add_test;/home/betul/ns-allinone-3.41/ns-3.41/build-support/macros-and-definitions.cmake;1280;set_runtime_outputdirectory;/home/betul/ns-allinone-3.41/ns-3.41/CMakeLists.txt;149;process_options;/home/betul/ns-allinone-3.41/ns-3.41/CMakeLists.txt;0;")
subdirs("src")
subdirs("examples")
subdirs("scratch")
subdirs("utils")
