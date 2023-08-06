%global             source_name floorp
%global             application_name floorp

Name:               floorp
Version:            11.1.0
Release:            1%{?dist}
Summary:            Floorp Web browser

License:            MPLv1.1 or GPLv2+ or LGPLv2+
URL:                https://www.github.com/Floorp-Projects/Floorp
Source0:            https://github.com/Floorp-Projects/Floorp/releases/download/floorp-%{version}.en-US.linux-x86_64.tar.bz2
Source1:	    https://raw.githubusercontent.com/LovecraftianGodsKiller/RandomStuff/main/floorp.desktop

ExclusiveArch:      x86_64

Requires(post):     xdg-utils
Requires(post):     gtk-update-icon-cache

%description
Floorp Web Browser

%prep
%setup -q -n %{source_name}

%install
%__rm -rf %{buildroot}

%__install -d %{buildroot}{/opt/%{application_name},%{_bindir},%{_datadir}/applications}

%__cp -r * %{buildroot}/opt/%{application_name}

%__ln_s /opt/%{application_name}/floorp %{buildroot}%{_bindir}/%{application_name}

%__install -D -m 0644 %{SOURCE1} -t %{buildroot}%{_datadir}/applications

%__install -D -m 0444 %{SOURCE2} -t %{buildroot}/opt/%{application_name}/distribution


%post
xdg-icon-resource install --novendor --size 128 /opt/floorp/browser/chrome/icons/default/default128.png floorp gtk-update-icon-cache -f -t /usr/share/icons/hicolor

%files
%{_datadir}/applications/floorp.desktop
%{_bindir}/%{application_name}
/opt/%{application_name}

%changelog
* Sun Aug 06 2023 Kirb GodsKiller - 11.1.0
- Initial build
