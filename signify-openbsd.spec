Summary:	OpenBSD tool to sign and verify signatures on files
Name:		signify-openbsd
Version:	32
Release:	1
License:	ISC
Group:		Applications/File
Source0:	https://github.com/aperezdc/signify/releases/download/v%{version}/signify-%{version}.tar.xz
# Source0-md5:	2e2e41bf841a0c8e3f5febbc39823a1a
Patch0:		link.patch
URL:		https://github.com/aperezdc/signify
BuildRequires:	libbsd-devel >= 0.8
BuildRequires:	libseccomp-devel
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	libbsd >= 0.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenBSD tool to sign and verify signatures on files.

%prep
%setup -q -n signify-%{version}
%patch -P0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	EXTRA_CFLAGS="%{rpmcflags} %{rpmcppflags}" \
	EXTRA_LDFLAGS="%{rpmldflags}" \
	PLEDGE=waive

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	CC="%{__cc}" \
	EXTRA_CFLAGS="%{rpmcflags} %{rpmcppflags}" \
	EXTRA_LDFLAGS="%{rpmldflags}" \
	PLEDGE=waive \
	PREFIX="%{_prefix}"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md COPYING README.md
%attr(755,root,root) %{_bindir}/signify
%{_mandir}/man1/signify.1*
