Name:           codehaus-parent
Version:        3
Release:        1
Summary:        Parent pom file for codehaus projects

Group:          Development/Java
License:        ASL 2.0
URL:            http://codehaus.org/
#Next version with license is at https://github.com/sonatype/codehaus-parent/blob/master/pom.xml
Source0:        http://repo1.maven.org/maven2/org/codehaus/codehaus-parent/3/codehaus-parent-3.pom
#Patch0:         %{name}-enforcer.patch
BuildArch:      noarch

BuildRequires:  jpackage-utils

Requires:       jpackage-utils

%description
This package contains the parent pom file for codehaus projects.


%prep
%setup -q -c -T
cp %{SOURCE0} .
#%patch0

%build


%install
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 codehaus-parent-4.pom \
        %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

#%add_to_maven_depmap org.codehaus codehaus-parent %{version} JPP codehaus-parent
%add_maven_depmap JPP-%{name}.pom 

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

