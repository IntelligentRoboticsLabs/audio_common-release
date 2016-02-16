Name:           ros-jade-sound-play
Version:        0.2.11
Release:        0%{?dist}
Summary:        ROS sound_play package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/sound_play
Source0:        %{name}-%{version}.tar.gz

Requires:       festival
Requires:       festvox-kal-diphone
Requires:       gstreamer
Requires:       gstreamer-plugins-base
Requires:       gstreamer-plugins-good
Requires:       gstreamer-plugins-ugly
Requires:       gstreamer-python
Requires:       ros-jade-actionlib-msgs
Requires:       ros-jade-audio-common-msgs
Requires:       ros-jade-diagnostic-msgs
Requires:       ros-jade-message-runtime
Requires:       ros-jade-roscpp
Requires:       ros-jade-roslib
Requires:       ros-jade-rospy
BuildRequires:  gstreamer-devel
BuildRequires:  gstreamer-plugins-base-devel
BuildRequires:  ros-jade-actionlib
BuildRequires:  ros-jade-actionlib-msgs
BuildRequires:  ros-jade-audio-common-msgs
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-diagnostic-msgs
BuildRequires:  ros-jade-message-generation
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-roslib

%description
sound_play provides a ROS node that translates commands on a ROS topic
(robotsound) into sounds. The node supports built-in sounds, playing OGG/WAV
files, and doing speech synthesis via festival. C++ and Python bindings allow
this node to be used without understanding the details of the message format,
allowing faster development and resilience to message format changes.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Tue Feb 16 2016 Austin Hendrix <namniart@gmail.com> - 0.2.11-0
- Autogenerated by Bloom

* Thu Jan 21 2016 Austin Hendrix <namniart@gmail.com> - 0.2.10-0
- Autogenerated by Bloom

* Wed Dec 02 2015 Austin Hendrix <namniart@gmail.com> - 0.2.9-0
- Autogenerated by Bloom

* Fri Oct 02 2015 Austin Hendrix <namniart@gmail.com> - 0.2.8-0
- Autogenerated by Bloom

* Thu Jun 25 2015 Austin Hendrix <ahendrix@willowgarage.com> - 0.2.7-0
- Autogenerated by Bloom

