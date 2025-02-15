Name:           vulkan-volk
Version:        1.4.304
Release:        1
Summary:        Meta loader for Vulkan API
Group:          System/Libraries
License:        MIT
URL:            https://github.com/zeux/volk
Source0:        https://github.com/zeux/volk/archive/vulkan-sdk-%{version}/volk-vulkan-sdk-%{version}.tar.gz
# from opensuse
Patch0:         vulkan-volk-shared.patch

BuildRequires:  cmake
BuildRequires:  vulkan-headers

Requires:       vulkan-headers

# Both vulkan-volk and volk-devel provide file with same name. To avoid problems, lets conflicts it
Conflicts:      volk-devel

%description
Meta loader for Vulkan API.

%prep
%autosetup -n volk-vulkan-sdk-%{version} -p1

%build
%cmake \
        -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
        -DVOLK_INSTALL:BOOL=ON
        
%make_build

%install
%make_install -C build

%files
%license LICENSE.md
%doc README.md
%{_includedir}/volk.h
%{_includedir}/volk.c
%{_libdir}/cmake/volk/
%{_libdir}/libvolk.so
