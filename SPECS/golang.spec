%undefine __brp_mangle_shebangs
%global _missing_build_ids_terminate_build 0
%global debug_package %{nil}

Name:           golang
Version:        1.21.3
Release:        1
Summary:        The Go Programming Language
License:        BSD and Public Domain
URL:            https://www.shellcheck.net/
Source:         https://go.dev/dl/go%{version}.linux-amd64.tar.gz
Source1:        gopath.sh

%description
%{summary}.

%prep
%setup -n go

%install
install -Dm0644 %{SOURCE1} %{buildroot}/etc/profile.d/gopath.sh
mkdir -p %{buildroot}/usr/local
cp -prv %{_builddir}/go %{buildroot}/usr/local/

%files
/usr/local/go/*
/etc/profile.d/gopath.sh
%doc LICENSE

%changelog
* Thu Oct 12 2023 Jamie Curnow <jc@jc21.com> - 1.21.3-1
- v1.21.3

* Thu Sep 14 2023 Jamie Curnow <jc@jc21.com> - 1.21.1-1
- v1.21.1

* Thu Aug 24 2023 Jamie Curnow <jc@jc21.com> - 1.21.0-1
- v1.21.0
