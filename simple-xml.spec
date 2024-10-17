%{?_javapackages_macros:%_javapackages_macros}
Name:          simple-xml
Summary:       An XML serialization framework for Java
Version:       2.7.1
Release:       4%{?dist}
License:       ASL 2.0
Url:           https://simple.sourceforge.net/
Source0:       http://downloads.sourceforge.net/simple/%{name}-%{version}.tar.gz
Source1:       http://repo1.maven.org/maven2/org/simpleframework/%{name}/%{version}/%{name}-%{version}.pom

BuildRequires: java-devel
BuildRequires: javapackages-tools
BuildRequires: ant
BuildRequires: ant-junit
BuildRequires: bea-stax
BuildRequires: bea-stax-api
BuildRequires: junit
BuildRequires: xpp3

Requires:      bea-stax
Requires:      xpp3

Requires:      javapackages-tools
BuildArch:     noarch

%description
Simple is a high performance XML serialization and
configuration framework for Java. Its goal is to
provide an XML framework that enables rapid development
of XML configuration and communication systems.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
# clean up
rm -r javadoc/* test/report/*
find . -name "*.jar" -delete
find . -name "*.class" -delete

sed -i 's/\r//' LICENSE.txt
# test @ random fails
sed -i 's|haltonfailure="yes"|haltonfailure="no"|' test/build.xml

%build

%ant -Dlib.path=%{_javadir} all

%install

mkdir -p %{buildroot}%{_javadir}
install -m 644 jar/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr javadoc/* %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%doc LICENSE.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt

%changelog
* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 2.7.1-3
- Use Requires: java-headless rebuild (#1067528)

* Wed Jan 15 2014 gil cattaneo <puntogil@libero.it> 2.7.1-2
- fix license field
- add javapackages-tools (provides jpackage-utils) references

* Fri Aug 23 2013 gil cattaneo <puntogil@libero.it> 2.7.1-1
- update to 2.7.1

* Wed May 08 2013 gil cattaneo <puntogil@libero.it> 2.7-1
- update to 2.7

* Wed Jan 23 2013 gil cattaneo <puntogil@libero.it> 2.6.9-1
- update to 2.6.9

* Sat Aug 04 2012 gil cattaneo <puntogil@libero.it> 2.6.6-1
- update to 2.6.6

* Wed Jun 27 2012 gil cattaneo <puntogil@libero.it> 2.6.4-1
- Initial import