Summary:	Keygrabber for BlackBox window manager
Summary(pl.UTF-8):	Program do obsługi klawiatury dla zarządcy okien BlackBox
Name:		epistrophy
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://nexus.carleton.ca/~smoynes/%{name}.tar.gz
# Source0-md5:	bcf685d355a6c1f159abc67d04852430
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Epistrophy is a lightweight keygrabber for BlackBox window manager.

%description -l pl.UTF-8
Epistrophy jest lekkim programem do obsługi klawiatury dla zarządcy
okien BlackBox.

%prep
%setup -q -n epist

%build
xmkmf -a
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install epist $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%doc README rcfile
