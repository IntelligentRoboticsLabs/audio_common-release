Name:           ros-indigo-audio-common-msgs
Version:        0.2.11
Release:        0%{?dist}
Summary:        ROS audio_common_msgs package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/audio_common_msgs
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-message-runtime
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-message-generation

%description
Messages for transmitting audio via ROS

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Tue Feb 16 2016 Austin Hendrix <namniart@gmail.com> - 0.2.11-0
- Autogenerated by Bloom

* Thu Jan 21 2016 Austin Hendrix <namniart@gmail.com> - 0.2.10-0
- Autogenerated by Bloom

* Wed Dec 02 2015 Austin Hendrix <namniart@gmail.com> - 0.2.9-0
- Autogenerated by Bloom

* Fri Oct 02 2015 Austin Hendrix <namniart@gmail.com> - 0.2.8-0
- Autogenerated by Bloom

