%undefine __brp_mangle_shebangs
%global _missing_build_ids_terminate_build 0
%global debug_package %{nil}

Name:           golang
Version:        1.22.4
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
* Tue Jun 11 2024 Jamie Curnow <jc@jc21.com> - 1.22.4-1
- v1.22.4

* Wed May 8 2024 Jamie Curnow <jc@jc21.com> - 1.22.3-1
- v1.22.3

* Mon Apr 22 2024 Jamie Curnow <jc@jc21.com> - 1.22.2-1
- v1.22.2

* Thu Mar 7 2024 Jamie Curnow <jc@jc21.com> - 1.22.1-1
- v1.22.1

* Mon Feb 12 2024 Jamie Curnow <jc@jc21.com> - 1.22.0-1
- v1.22.0

* Thu Feb 1 2024 Jamie Curnow <jc@jc21.com> - 1.21.6-1
- v1.21.6

* Tue Dec 5 2023 Jamie Curnow <jc@jc21.com> - 1.21.4-1
- v1.21.4

* Thu Oct 12 2023 Jamie Curnow <jc@jc21.com> - 1.21.3-1
- v1.21.3

* Thu Sep 14 2023 Jamie Curnow <jc@jc21.com> - 1.21.1-1
- v1.21.1

* Thu Aug 24 2023 Jamie Curnow <jc@jc21.com> - 1.21.0-1
- v1.21.0
