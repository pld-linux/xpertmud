%define		_rc	alpha2
%define		_snap	20050319
Summary:	Xpertmud - extensible MUD client
Summary(pl):	Xpertmud - elastyczny klient MUD
Name:		xpertmud
Version:	3.1
Release:	0.%{_rc}_%{_snap}.1
License:	GPL
Group:		X11/Applications/Games
Source0:	ftp://distfiles.pld-linux.org/src/%{name}-%{version}%{_rc}-%{_snap}.tar.bz2
# Source0-md5:	a8126a7d9420a6fa8fe4c244d00f2ea4
Source1:	%{name}.desktop
Patch0:		xpertmud-cvs.patch
URL:		http://xpertmud.sourceforge.net/
BuildRequires:	artsc-devel
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	fam-devel
BuildRequires:	kdelibs-devel
BuildRequires:	libart_lgpl-devel
BuildRequires:	libtool
BuildRequires:	pcre-devel
BuildRequires:	perl-devel
BuildRequires:	perl-perldoc
BuildRequires:	python-devel
BuildRequires:	qt-devel
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
Requires:	kdelibs >= 3.1
Requires:	perl(DynaLoader) = %(%{__perl} -MDynaLoader -e 'print DynaLoader->VERSION')
%ruby_mod_ver_requires_eq
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xpertmud is an extensible perl, python and ruby (partialy) scriptable
MUD client. It supports multiple windows (which are scriptable, yeah),
and you can use triggers, aliases or whatever you want on every bit of
text that comes from or goes to the server. There's a stable and
intuitive plugin API, so you can extend the client with Qt-based C++
code.

%description -l pl
Xpertmud jest elastycznym klientem MUD. Wspiera takie jêzyki skryptowe
jak perl, python oraz czê¶ciowo ruby. Posiada obs³ugê wielu okien
(które mo¿na do woli oskryptowaæ!). Oczywi¶cie mo¿na stosowaæ
triggery, aliasy oraz jest mo¿liwo¶æ zrobienia czego siê tylko
zapragnie z wysy³anym do, b±d¼ odbieranym z serwera mud tekstem. Poza
tym Xpertmud posiada stabilne oraz proste do poznania API do wtyczek.
Dziêki temu mo¿na poszerzyæ jego mo¿liwo¶ci pisz±c dodatki oparte na
Qt.

%package scripting-python
Summary:	Xpertmud - Python scripting package
Summary(pl):	Xpertmud - biblioteka do pisania skryptów w pythonie
Group:		X11/Applications/Games
Requires:	xpertmud = %{version}-%{release}
Requires:	python >= 2.2.2

%description scripting-python
Python scripting library for Xpertmud.

%description scripting-python -l pl
Biblioteka Xpertmuda do pisania skryptów w Pythonie.

%package scripting-ruby
Summary:	Xpertmud - Ruby scripting package
Summary(pl):	Xpertmud - biblioteka do pisania skryptów w Ruby
Group:		X11/Applications/Games
Requires:	xpertmud = %{version}-%{release}
Requires:	ruby >= 1:1.6.8

%description scripting-ruby
Ruby scripting library for Xpertmud.

%description scripting-ruby -l pl
Biblioteka Xpertmuda do pisania skryptów w Ruby.

%package plugins-misc-BattleTech
Summary:	Xpertmud - BattleTech plugin
Summary(pl):	Xpertmud - wtyczka Xpertmuda do BattleTech
Group:		X11/Applications/Games
Requires:	xpertmud = %{version}-%{release}

%description plugins-misc-BattleTech
Xpertmud BattleTech plugin.

%description plugins-misc-BattleTech -l pl
Wtyczka Xpertmuda do BattleTech.

%package plugins-misc-html
Summary:	Xpertmud - Rapid Gui Development plugin
Summary(pl):	Xpertmud - wtyczka do szybkiego tworzenia GUI
Group:		X11/Applications/Games
Requires:	xpertmud = %{version}-%{release}

%description plugins-misc-html
Plugin for "Rapid Gui Development" utilizing (D)HTML and javascript.

%description plugins-misc-html -l pl
Wtyczka do szybkiego tworzenia GUI ("Rapid Gui Development"),
wykorzystuj±ca do tego (D)HTML oraz javascript.

%prep
%setup -q -n %{name}-%{version}%{_rc}
%patch0 -p0

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
make -f Makefile.dist
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_desktopdir}
cp %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

install -d $RPM_BUILD_ROOT%{_kdedocdir}/en/xpertmud
install doc/en/{index.cache.bz2,index.docbook,perl-devel.docbook,python-devel.docbook} \
	$RPM_BUILD_ROOT%{_kdedocdir}/en/xpertmud

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog DESIGN TODO
%attr(755,root,root) %{_bindir}/*
%{_libdir}/kde3/kfile_xmud.la
%attr(755,root,root) %{_libdir}/kde3/kfile_xmud.so
%{_libdir}/kde3/libxmperlinterpreter.la
%attr(755,root,root) %{_libdir}/kde3/libxmperlinterpreter.so
%{_libdir}/kde3/xmud_example.la
%attr(755,root,root) %{_libdir}/kde3/xmud_example.so
%{_desktopdir}/%{name}.desktop
%dir %{_datadir}/apps/xpertmud
%{_datadir}/apps/xpertmud/artwork
%{_datadir}/apps/xpertmud/bookmarks
%dir %{_datadir}/apps/xpertmud/perl
%{_datadir}/apps/xpertmud/perl/XMExample.pm
%{_datadir}/apps/xpertmud/perl/pipes.pl
%{_datadir}/apps/xpertmud/perl/completion.pl
%{_datadir}/apps/xpertmud/perl/snake.pl
%{_datadir}/apps/xpertmud/perl/speedwalk.pl
%{_datadir}/apps/xpertmud/xpertmudui.rc
%{_datadir}/mimelnk/application/x-xpertmud-bookmark.desktop
%{_datadir}/services/kfile_xmud.desktop
%{_datadir}/services/xpertmud.protocol
%{_iconsdir}/hicolor/16x16/apps/xpertmud.png
%{_iconsdir}/hicolor/32x32/apps/xpertmud.png
# non-existent dir
#%{_iconsdir}/locolor/16x16/apps/xpertmud.png
#%{_iconsdir}/locolor/32x32/apps/xpertmud.png

%files scripting-python
%defattr(644,root,root,755)
%{_libdir}/kde3/libxmpythoninterpreter.la
%attr(755,root,root) %{_libdir}/kde3/libxmpythoninterpreter.so
%{_datadir}/apps/xpertmud/python/tapp.py

%files scripting-ruby
%defattr(644,root,root,755)
%{_libdir}/kde3/libxmrubyinterpreter.la
%attr(755,root,root) %{_libdir}/kde3/libxmrubyinterpreter.so

%files plugins-misc-BattleTech
%defattr(644,root,root,755)
%{_libdir}/kde3/xmud_battletech.la
%attr(755,root,root) %{_libdir}/kde3/xmud_battletech.so
%{_datadir}/apps/xpertmud/perl/XMBattleContacts.pm
%{_datadir}/apps/xpertmud/perl/XMBattleCore.pm
%{_datadir}/apps/xpertmud/perl/XMBattleHeat.pm
%{_datadir}/apps/xpertmud/perl/XMBattleMapView.pm
%{_datadir}/apps/xpertmud/perl/XMBattleSpeed.pm
%{_datadir}/apps/xpertmud/perl/XMBattleWeapons.pm
%{_datadir}/apps/xpertmud/perl/battlerecorder.pl
%{_datadir}/apps/xpertmud/perl/htmlmapper.pl
%{_datadir}/apps/xpertmud/perl/xperthud.pl
%dir %{_datadir}/apps/xpertmud/python
%{_datadir}/apps/xpertmud/python/battletech.py
%{_datadir}/apps/xpertmud/python/bt3030.py
%{_datadir}/apps/xpertmud/python/btcockpit.py
%{_datadir}/apps/xpertmud/python/claims.py
%{_datadir}/apps/xpertmud/python/contacts.py
%{_datadir}/apps/xpertmud/python/frequencies.py
%{_datadir}/apps/xpertmud/python/keybindings.py

%files plugins-misc-html
%defattr(644,root,root,755)
%{_libdir}/kde3/xmud_html.la
%attr(755,root,root) %{_libdir}/kde3/xmud_html.so
%{_datadir}/apps/xpertmud/perl/XMHTML.pm
