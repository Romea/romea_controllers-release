Name:           ros-indigo-four-wheel-steering-controller
Version:        0.2.0
Release:        0%{?dist}
Summary:        ROS four_wheel_steering_controller package

Group:          Development/Libraries
License:        GPLv3
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-controller-interface
Requires:       ros-indigo-four-wheel-steering-msgs
Requires:       ros-indigo-nav-msgs
Requires:       ros-indigo-realtime-tools
Requires:       ros-indigo-tf
Requires:       ros-indigo-urdf-vehicle-kinematic
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-controller-interface
BuildRequires:  ros-indigo-four-wheel-steering-msgs
BuildRequires:  ros-indigo-nav-msgs
BuildRequires:  ros-indigo-realtime-tools
BuildRequires:  ros-indigo-tf
BuildRequires:  ros-indigo-urdf-vehicle-kinematic

%description
Controller for a four wheel steering mobile base.

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
        -DCMAKE_INSTALL_LIBDIR="lib" \
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
* Fri Jan 20 2017 Vincent Rousseau <vincent.rousseau@irstea.fr> - 0.2.0-0
- Autogenerated by Bloom

