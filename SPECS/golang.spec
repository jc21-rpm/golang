%undefine __brp_mangle_shebangs
%global _missing_build_ids_terminate_build 0
%global debug_package %{nil}

# Turn off strip'ng of binaries
%global __strip /bin/true

Name:           golang
Version:        1.25.0
Release:        1%{?dist}
Summary:        The Go Programming Language
License:        BSD and Public Domain
URL:            https://go.dev
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
* Wed Aug 13 2025 Jamie Curnow <jc@jc21.com> - 1.25.0-1
- v1.25.0

* Thu Aug 7 2025 Jamie Curnow <jc@jc21.com> - 1.24.6-1
- v1.24.6

* Thu Jul 3 2025 Jamie Curnow <jc@jc21.com> - 1.24.5-1
- v1.24.5

* Tue Jun 2 2025 Jamie Curnow <jc@jc21.com> - 1.24.4-1
- v1.24.4

* Wed May 7 2025 Jamie Curnow <jc@jc21.com> - 1.24.3-1
- v1.24.3

* Thu Apr 3 2025 Jamie Curnow <jc@jc21.com> - 1.24.2-1
- v1.24.2

* Wed Mar 5 2025 Jamie Curnow <jc@jc21.com> - 1.24.1-1
- v1.24.1

* Thu Feb 13 2025 Jamie Curnow <jc@jc21.com> - 1.24.0-1
- v1.24.0

* Thu Feb 6 2025 Jamie Curnow <jc@jc21.com> - 1.23.6-1
- v1.23.6

* Mon Jan 20 2025 Jamie Curnow <jc@jc21.com> - 1.23.5-1
- v1.23.5

* Thu Dec 5 2024 Jamie Curnow <jc@jc21.com> - 1.23.4-1
- v1.23.4

* Fri Nov 8 2024 Jamie Curnow <jc@jc21.com> - 1.23.3-1
- v1.23.3

* Thu Oct 3 2024 Jamie Curnow <jc@jc21.com> - 1.23.2-1
- v1.23.2

* Fri Sep 6 2024 Jamie Curnow <jc@jc21.com> - 1.23.1-1
- v1.23.1

* Thu Aug 15 2024 Jamie Curnow <jc@jc21.com> - 1.23.0-1
- v1.23.0

* Thu Aug 8 2024 Jamie Curnow <jc@jc21.com> - 1.22.6-1
- v1.22.6

* Wed Jul 3 2024 Jamie Curnow <jc@jc21.com> - 1.22.5-1
- v1.22.5

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
