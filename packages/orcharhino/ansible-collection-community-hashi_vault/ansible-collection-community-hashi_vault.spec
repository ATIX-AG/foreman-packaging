%global debug_package %{nil}

%global collection_namespace community
%global collection_name hashi_vault
%global collection_directory %{_datadir}/ansible/collections/ansible_collections/%{collection_namespace}/%{collection_name}

%global release 1

Name:       ansible-collection-%{collection_namespace}-%{collection_name}
Version:    6.2.0
Release:    %{?prerelease:0.}%{release}%{?prerelease}%{?nightly}%{?dist}
Summary:    The Ansible modules collection for HashiCorp Vault

License:    GPL-3.0+
URL:        %{ansible_collection_url community hashi_vault}
Source0:    https://github.com/ansible-collections/%{collection_namespace}.%{collection_name}/archive/refs/tags/%{version}.tar.gz
BuildArch:  noarch

Provides: ansible-collection(%{collection_namespace}.%{collection_name}) = %{version}

BuildRequires: ansible-packaging

Requires: ansible-core
Requires: (python3-requests if ansible-core >= 1:2.14.7)
Requires: (python3-pyyaml if ansible-core >= 1:2.14.7)
Requires: (python3.11-requests if (ansible-core >= 2.14.2-3 and ansible-core < 1:2.14.7))
Requires: (python3.11-pyyaml if (ansible-core >= 2.14.2-3 and ansible-core < 1:2.14.7))
Requires: (python3.12-requests if (ansible-core >= 2.16.0))
Requires: (python3.12-pyyaml if (ansible-core >= 2.16.0))

%description
Collection of Ansible Modules to manage HashiCorp Vault.

%prep
%setup -q -n %{collection_namespace}.%{collection_name}-%{version}
rm -frv ".github"

%build
%ansible_collection_build

%install
%ansible_collection_install

%files -f %{ansible_collection_filelist}

%changelog
* Thu Jul 18 2024 Maximilian Kolb - 6.2.0-1
- Initial packaging
