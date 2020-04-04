# Install script for directory: /home/revati/UMD/ENPM661/Projects/Path-Planning-using-A_Star/phase_4/src/roomba_walker

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/revati/UMD/ENPM661/Projects/Path-Planning-using-A_Star/phase_4/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roomba_walker/cmake" TYPE FILE FILES "/home/revati/UMD/ENPM661/Projects/Path-Planning-using-A_Star/phase_4/build/roomba_walker/catkin_generated/installspace/roomba_walker-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/revati/UMD/ENPM661/Projects/Path-Planning-using-A_Star/phase_4/devel/share/roseus/ros/roomba_walker")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python2" -m compileall "/home/revati/UMD/ENPM661/Projects/Path-Planning-using-A_Star/phase_4/devel/lib/python2.7/dist-packages/roomba_walker")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/revati/UMD/ENPM661/Projects/Path-Planning-using-A_Star/phase_4/devel/lib/python2.7/dist-packages/roomba_walker")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/revati/UMD/ENPM661/Projects/Path-Planning-using-A_Star/phase_4/build/roomba_walker/catkin_generated/installspace/roomba_walker.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roomba_walker/cmake" TYPE FILE FILES "/home/revati/UMD/ENPM661/Projects/Path-Planning-using-A_Star/phase_4/build/roomba_walker/catkin_generated/installspace/roomba_walker-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roomba_walker/cmake" TYPE FILE FILES
    "/home/revati/UMD/ENPM661/Projects/Path-Planning-using-A_Star/phase_4/build/roomba_walker/catkin_generated/installspace/roomba_walkerConfig.cmake"
    "/home/revati/UMD/ENPM661/Projects/Path-Planning-using-A_Star/phase_4/build/roomba_walker/catkin_generated/installspace/roomba_walkerConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roomba_walker" TYPE FILE FILES "/home/revati/UMD/ENPM661/Projects/Path-Planning-using-A_Star/phase_4/src/roomba_walker/package.xml")
endif()

