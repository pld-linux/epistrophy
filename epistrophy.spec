Summary:	Keygrabber for BlackBox window manager
Summary(pl):	Program do obs³ugi klawiatury dla zarz±dcy okien BlackBox
Name:		epistrophy
Version:	1.0
Release:	1
License:	GPL
Group:		Applications/Console
Source0:	http://nexus.carleton.ca/~smoynes/%{name}.tar.gz
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Epistrophy is a lightweight keygrabber for BlackBox window manager.

%description -l pl
Epistrophy jest lekkim programem do obs³ugi klawiatury dla zarz±dcy
okien BlackBox.

%define		_prefix		/usr/X11R6

%prep
%setup -q -n epist

xmkmf -a
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install epist $RPM_BUILD_ROOT%{_bindir}

gzip -9nf README rcfile

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%doc *.gz
