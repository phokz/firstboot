Name:       virtualmaster-firstboot
Version:    0.1
Release:    1
Summary:    Configures network and users on first boot of VM
License:    GPL
URL:        http://www.virtualmaster.cz
Group:      System/Boot
Source:     http://www.virtualmaster.cz/virtualmaster-firstboot/virtualmaster-firstboot-0.1.tar.gz
Requires:   patch
BuildRoot:  %{_tmppath}/buildroot-%{name}-%{version}
BuildArch:  noarch

%description
Configures network and users on first boot of VM
Virtualmaster package is a set of scripts to kickoff freshly installed
virtual machine. Most of tasks are performed only once, on first boot.
Idea of this package is to have one universal distro-independent config
file and then set of distro-specific packages (e.g. .deb, .rpm, .tgz).
Main tasks are:
    - set up networking (IP, gateway, nameservers) on first booot
    - resize root filesystem to actual size of partition
    - ensure swap partition has swap signature
    - set root's password
    - optionaly create users and add ssh keys
                              
%prep
%setup -q

%build

%install
%__mkdir -p %{buildroot}%{_docdir}/virtualmaster-firstboot
%__mkdir -p %{buildroot}%{_sysconfdir}/init.d
%__mkdir -p %{buildroot}%{_sysconfdir}/virtualmaster
%__install -m 755 ./etc/init.d/virtualmaster-redhat %{buildroot}/%{_sysconfdir}/init.d/%{name}
%__install -m 755 ./etc/virtualmaster/*.tpl %{buildroot}/%{_sysconfdir}/virtualmaster/
%__install -m 755 ./rc.sysinit.patch %{buildroot}/%{_sysconfdir}/virtualmaster/
%__install -m 755 ./usr/share/doc/* %{buildroot}/%{_docdir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_sysconfdir}/init.d/%{name}
%{_sysconfdir}/virtualmaster/*
%doc %{_docdir}/*

%preun
cd /etc/rc.d
patch -R < /etc/virtualmaster/rc.sysinit.patch
%post
cd /etc/rc.d
patch < /etc/virtualmaster/rc.sysinit.patch

%changelog
* Fri Jun 26 2009 Josef Liska <jl@chl.cz> <0.1> <1>
- initial release 
 
