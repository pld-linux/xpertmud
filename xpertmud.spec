Summary:	xpertmud - extensible MUD client
Summary(pl):	xpertmud - elastyczny klient MUD
Name:		xpertmud
Version:	20031115
Release:	0.1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dooh.civ.pl/xpertmud/%{name}-%{version}.tar.bz2
# Source0-md5:	6e34861e1dee06fc5818d80a23344d02
URL:		http://xpertmud.sourceforge.net
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	kdelibs-devel
BuildRequires:	libart_lgpl-devel
BuildRequires:	libtool
BuildRequires:	perl-devel
BuildRequires:	python-devel
BuildRequires:	qt-devel
BuildRequires:	ruby-devel
Requires:	kdelibs >= 3.1
Requires:	perl >= 5.6

%description
Xpertmud is an extensible perl, python and ruby (partialy) scriptable
MUD client. It supports multiple windows (which are scriptable, yeah),
and you can use triggers, aliases or whatever you want on every bit of
text that comes from or goes to the server. There's a stable and
intuitive plugin API, so you can extend the client with Qt-based C++
code.

%package scripting-python
Summary:	Python scripting package
Group:		X11/Applications/Games
Requires:	xpertmud = %{version}-%{release}
Requires:	python >= 2.2.2

%description scripting-python
Python scripting library for xpertmud.


%package scripting-ruby
Summary:	Ruby scripting package
Group:		X11/Applications/Games
Requires:	xpertmud = %{version}-%{release}
Requires:	ruby >= 1.6.8

%description scripting-ruby
Ruby scripting library for xpertmud.

%package plugins-misc-BattleTech
Requires:	xpertmud = %{version}-%{release}
Summary:	BattleTech plugin
Group:		X11/Applications/Games

%description plugins-misc-BattleTech
Xpertmud BattleTech plugin.

%prep

%setup -q -n xpertmud

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%{__make} -f Makefile.dist

%configure
%{__make}


%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%%doc AUTHORS ChangeLog DESIGN TODO
%%attr(755,root,root) %{_bindir}/*
%{_libdir}/kde3/kfile_xmud.la
%{_libdir}/kde3/kfile_xmud.so
%{_libdir}/kde3/libxmperlinterpreter.la
%{_libdir}/kde3/libxmperlinterpreter.so
%{_libdir}/kde3/xmud_example.la
%{_libdir}/kde3/xmud_example.so
%{_applnkdir}/Games/xpertmud.desktop
%{_datadir}/apps/xpertmud/artwork/*
%{_datadir}/apps/xpertmud/bookmarks/*
%{_datadir}/apps/xpertmud/perl/XMExample.pm
%{_datadir}/apps/xpertmud/perl/pipes.pl
%{_datadir}/apps/xpertmud/perl/completion.pl
%{_datadir}/apps/xpertmud/perl/snake.pl
%{_datadir}/apps/xpertmud/perl/speedwalk.pl
%{_datadir}/apps/xpertmud/xpertmudui.rc
%{_pixmapsdir}/hicolor/16x16/apps/xpertmud.png
%{_pixmapsdir}/hicolor/32x32/apps/xpertmud.png
%{_pixmapsdir}/locolor/16x16/apps/xpertmud.png
%{_pixmapsdir}/locolor/32x32/apps/xpertmud.png
%{_datadir}/locale/de/LC_MESSAGES/xpertmud.mo
%{_datadir}/mimelnk/application/x-xpertmud-bookmark.desktop
%{_datadir}/services/kfile_xmud.desktop
%{_datadir}/services/xpertmud.protocol

%files scripting-python
%defattr(644,root,root,755)
%{_libdir}/kde3/libxmpythoninterpreter.la
%{_libdir}/kde3/libxmpythoninterpreter.so
%{_datadir}/apps/xpertmud/python/tapp.py

%files scripting-ruby
%defattr(644,root,root,755)
%{_libdir}/kde3/libxmrubyinterpreter.la
%{_libdir}/kde3/libxmrubyinterpreter.so

%files plugins-misc-BattleTech
%defattr(644,root,root,755)
%{_libdir}/kde3/xmud_battletech.la
%{_libdir}/kde3/xmud_battletech.so
%{_datadir}/apps/xpertmud/perl/XMBattleContacts.pm
%{_datadir}/apps/xpertmud/perl/XMBattleCore.pm
%{_datadir}/apps/xpertmud/perl/XMBattleHeat.pm
%{_datadir}/apps/xpertmud/perl/XMBattleMapView.pm
%{_datadir}/apps/xpertmud/perl/XMBattleSpeed.pm
%{_datadir}/apps/xpertmud/perl/XMBattleWeapons.pm
%{_datadir}/apps/xpertmud/perl/xperthud.pl
%{_datadir}/apps/xpertmud/python/battletech.py
%{_datadir}/apps/xpertmud/python/bt3030.py
%{_datadir}/apps/xpertmud/python/btcockpit.py
%{_datadir}/apps/xpertmud/python/claims.py
%{_datadir}/apps/xpertmud/python/contacts.py
%{_datadir}/apps/xpertmud/python/frequencies.py
%{_datadir}/apps/xpertmud/python/keybindings.py
