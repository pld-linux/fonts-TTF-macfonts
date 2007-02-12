Summary:	Mac OS X fonts
Summary(pl.UTF-8):   Fonty z Mac OS X
Name:		fonts-TTF-macfonts
Version:	0.1
Release:	1
License:	distributable
Group:		Fonts
Source0:	Fonts.zip
# Source0-md5:	9ec9adb4403b2f99cc0b0d1c70b0c178
URL:		http://www.osx-e.com/downloads/misc/macfonts.html
BuildRequires:	unzip
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/TTF
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ttffontsdir	%{_fontsdir}/TTF

%description
Mac OS X fonts.

%description -l pl.UTF-8
Fonty z Mac OS X.

%prep
%setup -q -n Fonts

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_ttffontsdir}

install *.ttf *.TTF $RPM_BUILD_ROOT%{_ttffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%doc *.txt
%{_ttffontsdir}/*
