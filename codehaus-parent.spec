Name:           codehaus-parent
Version:        4
Release:        8.4
Summary:        Parent pom file for codehaus projects
Group:		System/Libraries
License:        ASL 2.0
URL:            https://codehaus.org/
BuildArch:      noarch
# Literal, so the first rpmbuild -bs records them before sysjar is installed.
BuildRequires:	maven
BuildRequires:	java-current-devel
BuildSystem:	maven

#Next version with license is at https://github.com/sonatype/codehaus-parent/blob/master/pom.xml
Source0:        http://repo1.maven.org/maven2/org/codehaus/codehaus-parent/%{version}/codehaus-parent-%{version}.pom
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

Patch0:         %{name}-enforcer.patch


%description
This package contains the parent pom file for codehaus projects.

%prep
%setup -q -c -T
cp -p %{SOURCE0} pom.xml
cp -p %{SOURCE1} LICENSE
%patch 0

%files -f .mfiles
%doc LICENSE
