%define oname	ckeditor

Name:		drupal-wysiwyg-%{oname}
Summary:	CKEditor for Drupal Wysiwyg module
Version:	3.6.4
Release:	2
License:	GPLv2+ or LGPLv2.1+ or MPL
Group:		Networking/WWW
URL:		http://ckeditor.com/
Source0:	http://download.cksource.com/CKEditor/CKEditor/CKEditor%%20%{version}/%{oname}_%{version}.tar.gz
Requires:	drupal-wysiwyg
Provides:	drupal-wysiwyg-editor
BuildArch:	noarch

%description
CKEditor is a text editor to be used inside web pages. It's a WYSIWYG editor,
which means that the text being edited on it looks as similar as possible
to the results users have when publishing it. It brings to the web common
editing features found on desktop editing applications like Microsoft Word
and OpenOffice.

%prep
%setup -q -n %{oname}

%build

%install
%__install -d %{buildroot}%{_var}/www/drupal//sites/all/libraries/
cp -a . %{buildroot}%{_var}/www/drupal//sites/all/libraries/%{oname}
rm %{buildroot}%{_var}/www/drupal//sites/all/libraries/%{oname}/*.html

%files
%{_var}/www/drupal//sites/all/libraries/%{oname}
%doc CHANGES.html LICENSE.html


%changelog
* Thu Aug 09 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 3.6.4-1
+ Revision: 813306
- update to 3.6.4

* Fri May 11 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 3.6.3-2
+ Revision: 798357
- fix URL tag

* Fri May 11 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 3.6.3-1
+ Revision: 798336
- imported package drupal-wysiwyg-ckeditor

