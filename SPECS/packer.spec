Name: packer	
Version: 1.6.3
Release: 1%{?dist}
Summary: Create machine and container images for multiple platforms
Group: Development/Tools
License: MPLv2.0
URL: https://www.packer.io/

Source0: https://releases.hashicorp.com/packer/%{version}/packer_%{version}_linux_amd64.zip

%description
Packer is a tool for creating machine and container images for
multiple platforms from a single source configuration. 

%prep

%build

%install
mkdir -p %{buildroot}%{_bindir}
unzip -o %{SOURCE0} -d %{buildroot}%{_bindir}

# Rename to packerio since packer conflicts with Fedora
pushd %{buildroot}%{_bindir}
  mv packer packerio
popd

%files
%{_bindir}/*
