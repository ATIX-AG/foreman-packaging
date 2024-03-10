# template: default
%global gem_name apipie-dsl

Name: rubygem-%{gem_name}
Version: 2.6.2
Release: 1%{?dist}
Summary: Ruby DSL documentation tool
License: MIT
URL: https://github.com/Apipie/apipie-dsl
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.5.0
BuildRequires: ruby >= 2.5.0
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Ruby DSL documentation tool.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%license %{gem_instdir}/APACHE-LICENSE-2.0
%license %{gem_instdir}/MIT-LICENSE
%{gem_instdir}/app
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/test

%changelog
* Sun Mar 10 2024 Foreman Packaging Automation <packaging@theforeman.org> - 2.6.2-1
- Update to 2.6.2

* Wed Nov 08 2023 Oleh Fedorenko <ofedoren@redhat.com> 2.6.1-1
- Update to 2.6.1

* Fri Oct 13 2023 Oleh Fedorenko <ofedoren@redhat.com> 2.6.0-1
- Update to 2.6.0

* Wed May 25 2022 Evgeni Golov 2.5.0-1
- Update to 2.5.0

* Thu Apr 15 2021 Oleh Fedorenko <ofedoren@redhat.com> 2.4.0-1
- Update to 2.4.0

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 2.3.0-2
- Rebuild against rh-ruby27

* Tue Oct 13 2020 Oleh Fedorenko <ofedoren@redhat.com> 2.3.0-1
- Update to 2.3.0

* Mon Jul 27 2020 Oleh Fedorenko <ofedoren@redhat.com> 2.2.9-1
- Update to 2.2.9

* Mon Jul 20 2020 Oleh Fedorenko <ofedoren@redhat.com> 2.2.8-1
- Update to 2.2.8

* Fri Jun 26 2020 Oleh Fedorenko <ofedoren@redhat.com> 2.2.7-1
- Update to 2.2.7

* Fri May 29 2020 Oleh Fedorenko <ofedoren@redhat.com> 2.2.5-1
- Update to 2.2.5

* Tue Apr 28 2020 Tomer Brisker <tbrisker@gmail.com> - 2.2.2-2
- rebuild for el8

* Mon Apr 06 2020 Oleh Fedorenko <ofedoren@redhat.com> 2.2.2-1
- Add rubygem-apipie-dsl generated by gem2rpm using the scl template

