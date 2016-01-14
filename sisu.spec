%global pkg_name sisu
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^osgi\\(org\\.sonatype\\.sisu\\.guava\\)$

Name:           %{?scl_prefix}%{pkg_name}
Version:        2.3.0
Release:        11.13%{?dist}
Summary:        Sonatype dependency injection framework
License:        ASL 2.0 and EPL and MIT
URL:            http://github.com/sonatype/sisu

# git clone git://github.com/sonatype/%{pkg_name} ${name}-%{version}
# cd %{pkg_name}-%{version}
# git checkout %{pkg_name}-%{version}
# find ./ -name "*.jar" -delete
# find ./ -name "*.class" -delete
# cd ..
# tar czvf %{pkg_name}-%{version}.tar.gz %{pkg_name}-%{version}
Source0:        %{pkg_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  %{?scl_prefix_java_common}javapackages-tools
BuildRequires:  %{?scl_prefix_java_common}maven-local

BuildRequires:  %{?scl_prefix}aopalliance
BuildRequires:  %{?scl_prefix_java_common}atinject
BuildRequires:  %{?scl_prefix}cdi-api
BuildRequires:  %{?scl_prefix_java_common}felix-framework
BuildRequires:  %{?scl_prefix}forge-parent
BuildRequires:  %{?scl_prefix}google-guice
BuildRequires:  %{?scl_prefix_java_common}junit
BuildRequires:  %{?scl_prefix}plexus-classworlds
BuildRequires:  %{?scl_prefix}plexus-containers-component-annotations
BuildRequires:  %{?scl_prefix}plexus-utils
BuildRequires:  %{?scl_prefix}sisu
BuildRequires:  %{?scl_prefix}testng
BuildRequires:  %{?scl_prefix}weld-parent

Requires:       %{name}-bean              = %{version}-%{release}
Requires:       %{name}-bean-binders      = %{version}-%{release}
Requires:       %{name}-bean-containers   = %{version}-%{release}
Requires:       %{name}-bean-converters   = %{version}-%{release}
Requires:       %{name}-bean-inject       = %{version}-%{release}
Requires:       %{name}-bean-locators     = %{version}-%{release}
Requires:       %{name}-bean-reflect      = %{version}-%{release}
Requires:       %{name}-bean-scanners     = %{version}-%{release}
Requires:       %{name}-containers        = %{version}-%{release}
Requires:       %{name}-inject            = %{version}-%{release}
Requires:       %{name}-inject-bean       = %{version}-%{release}
Requires:       %{name}-inject-plexus     = %{version}-%{release}
Requires:       %{name}-osgi-registry     = %{version}-%{release}
Requires:       %{name}-parent            = %{version}-%{release}
Requires:       %{name}-plexus            = %{version}-%{release}
Requires:       %{name}-plexus-binders    = %{version}-%{release}
Requires:       %{name}-plexus-converters = %{version}-%{release}
Requires:       %{name}-plexus-lifecycles = %{version}-%{release}
Requires:       %{name}-plexus-locators   = %{version}-%{release}
Requires:       %{name}-plexus-metadata   = %{version}-%{release}
Requires:       %{name}-plexus-scanners   = %{version}-%{release}
Requires:       %{name}-plexus-shim       = %{version}-%{release}
Requires:       %{name}-registries        = %{version}-%{release}
Requires:       %{name}-spi-registry      = %{version}-%{release}

%description
Java dependency injection framework with backward support for plexus and bean
style dependency injection.

%package        parent
Summary:        Sisu parent POM

%description    parent
This package contains %{summary}.

%package        containers
Summary:        Sisu containers POM

%description    containers
This package contains %{summary}.

%package        bean
Summary:        Sisu bean POM

%description    bean
This package contains %{summary}.

%package        plexus
Summary:        Sisu Plexus POM

%description    plexus
This package contains %{summary}.

%package        registries
Summary:        Sisu registries POM

%description    registries
This package contains %{summary}.

%package        inject
Summary:        Sisu inject POM

%description    inject
This package contains %{summary}.

%package        bean-binders
Summary:        Guice Bean Binders module for Sisu

%description    bean-binders
This package contains %{summary}.

%package        bean-containers
Summary:        Guice Bean Containers module for Sisu

%description    bean-containers
This package contains %{summary}.

%package        bean-converters
Summary:        Guice Bean Converters module for Sisu

%description    bean-converters
This package contains %{summary}.

%package        bean-inject
Summary:        Guice Bean Inject module for Sisu

%description    bean-inject
This package contains %{summary}.

%package        bean-locators
Summary:        Guice Bean Locators module for Sisu

%description    bean-locators
This package contains %{summary}.

%package        bean-reflect
Summary:        Guice Bean Reflect module for Sisu

%description    bean-reflect
This package contains %{summary}.

%package        bean-scanners
Summary:        Guice Bean Scanners module for Sisu

%description    bean-scanners
This package contains %{summary}.

%package        plexus-binders
Summary:        Guice Plexus Binders module for Sisu

%description    plexus-binders
This package contains %{summary}.

%package        plexus-converters
Summary:        Guice Plexus Converters module for Sisu

%description    plexus-converters
This package contains %{summary}.

%package        plexus-lifecycles
Summary:        Guice Plexus Lifecycles module for Sisu

%description    plexus-lifecycles
This package contains %{summary}.

%package        plexus-locators
Summary:        Guice Plexus Locators module for Sisu

%description    plexus-locators
This package contains %{summary}.

%package        plexus-metadata
Summary:        Guice Plexus Metadata module for Sisu

%description    plexus-metadata
This package contains %{summary}.

%package        plexus-scanners
Summary:        Guice Plexus Scanners module for Sisu

%description    plexus-scanners
This package contains %{summary}.

%package        plexus-shim
Summary:        Guice Plexus Shim module for Sisu

%description    plexus-shim
This package contains %{summary}.

%package        inject-bean
Summary:        Bean Inject bundle for Sisu

%description    inject-bean
This package contains %{summary}.

%package        inject-plexus
Summary:        Plexus Inject bundle for Sisu

%description    inject-plexus
This package contains %{summary}.

%package        osgi-registry
Summary:        OSGi registry for Sisu

%description    osgi-registry
This package contains %{summary}.

%package        spi-registry
Summary:        SPI registry for Sisu

%description    spi-registry
This package contains %{summary}.

%package        javadoc
Summary:        API documentation for Sisu

%description    javadoc
This package contains %{summary}.

%prep
%setup -q -n %{pkg_name}-%{version}
%{?scl:scl enable %{scl_java_common} %{scl_maven} %{scl} - <<"EOF"}
set -e -x

# Animal sniffer is only causing problems
%pom_remove_plugin :animal-sniffer-maven-plugin

# Don't generate auto-requires for optional dependencies
sed -i "s|<optional>true</optional>|<scope>provided</scope>|" \
    $(grep -l "<optional>" $(find sisu-inject -name pom.xml))

# Remove bundled objectweb-asm library
rm -rf ./sisu-inject/containers/guice-bean/guice-bean-scanners/src/main/java/org/sonatype/guice/bean/scanners/asm
%pom_add_dep asm:asm sisu-inject/containers/guice-bean/guice-bean-scanners
# sisu-inject-bean bundles classes from other modules, so it also needs asm
%pom_add_dep asm:asm sisu-inject/containers/guice-bean/sisu-inject-bean

# Fix namespace of imported asm classes
sed -i 's/org.sonatype.guice.bean.scanners.asm/org.objectweb.asm/g' \
    sisu-inject/containers/guice-plexus/guice-plexus-scanners/src/{main,test}/java/org/sonatype/guice/plexus/scanners/*.java \
    sisu-inject/containers/guice-bean/guice-bean-scanners/src/{main,test}/java/org/sonatype/guice/bean/scanners/*.java \

# Fix plexus bundling
sed -i -e '/provide these APIs as a convenience/,+2d' \
    sisu-inject/containers/guice-bean/sisu-inject-bean/pom.xml
%pom_add_dep javax.inject:javax.inject sisu-inject/containers/guice-bean/sisu-inject-bean
%pom_add_dep javax.enterprise:cdi-api sisu-inject/containers/guice-bean/sisu-inject-bean

# add backward compatible location
cp sisu-inject/containers/guice-plexus/guice-plexus-lifecycles/src/main/java/org/sonatype/guice/plexus/lifecycles/*java \
   sisu-inject/containers/guice-plexus/guice-plexus-lifecycles/src/main/java/org/codehaus/plexus/
sed -i 's/org.sonatype.guice.plexus.lifecycles/org.codehaus.plexus/' \
       sisu-inject/containers/guice-plexus/guice-plexus-lifecycles/src/main/java/org/codehaus/plexus/*java

# Dependency not available
%pom_disable_module sisu-eclipse-registry sisu-inject/registries

%pom_remove_plugin :maven-surefire-plugin sisu-inject/containers/guice-bean/guice-bean-containers
%pom_remove_plugin :maven-clean-plugin sisu-inject/containers/guice-plexus/guice-plexus-binders
%pom_remove_plugin :maven-dependency-plugin sisu-inject/containers/guice-plexus/guice-plexus-binders

# logback is not available in RHEL
%pom_remove_dep :logback-classic

for pom in . sisu-inject/containers/guice-bean/guice-bean-binders \
         sisu-inject/containers/guice-bean/sisu-inject-bean; do
    %pom_xpath_inject "pom:dependency[pom:artifactId='cdi-api']" '<scope>provided</scope>' $pom
done

%{?scl:EOF}

%build
%{?scl:scl enable %{scl_java_common} %{scl_maven} %{scl} - <<"EOF"}
set -e -x
%mvn_package ":{sisu,guice}-{*}" @2
%mvn_build -s -f
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_java_common} %{scl_maven} %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files
%doc LICENSE-ASL.txt LICENSE-EPL.txt
%dir %{_mavenpomdir}/%{pkg_name}
%dir %{_javadir}/%{pkg_name}

%files parent            -f .mfiles-parent
%dir %{_mavenpomdir}/%{pkg_name}
%files containers        -f .mfiles-containers
%dir %{_mavenpomdir}/%{pkg_name}
%dir %{_javadir}/%{pkg_name}
%files bean              -f .mfiles-bean
%dir %{_mavenpomdir}/%{pkg_name}
%dir %{_javadir}/%{pkg_name}
%files plexus            -f .mfiles-plexus
%dir %{_mavenpomdir}/%{pkg_name}
%dir %{_javadir}/%{pkg_name}
%files registries        -f .mfiles-registries
%dir %{_mavenpomdir}/%{pkg_name}
%dir %{_javadir}/%{pkg_name}
%files inject            -f .mfiles-inject
%dir %{_mavenpomdir}/%{pkg_name}
%dir %{_javadir}/%{pkg_name}
%files bean-binders      -f .mfiles-bean-binders
%dir %{_mavenpomdir}/%{pkg_name}
%dir %{_javadir}/%{pkg_name}
%files bean-containers   -f .mfiles-bean-containers
%dir %{_mavenpomdir}/%{pkg_name}
%dir %{_javadir}/%{pkg_name}
%files bean-converters   -f .mfiles-bean-converters
%dir %{_mavenpomdir}/%{pkg_name}
%dir %{_javadir}/%{pkg_name}
%files bean-inject       -f .mfiles-bean-inject
%dir %{_mavenpomdir}/%{pkg_name}
%dir %{_javadir}/%{pkg_name}
%files bean-locators     -f .mfiles-bean-locators
%dir %{_mavenpomdir}/%{pkg_name}
%dir %{_javadir}/%{pkg_name}
%files bean-reflect      -f .mfiles-bean-reflect
%dir %{_mavenpomdir}/%{pkg_name}
%dir %{_javadir}/%{pkg_name}
%files bean-scanners     -f .mfiles-bean-scanners
%dir %{_mavenpomdir}/%{pkg_name}
%dir %{_javadir}/%{pkg_name}
%files plexus-binders    -f .mfiles-plexus-binders
%dir %{_mavenpomdir}/%{pkg_name}
%dir %{_javadir}/%{pkg_name}
%files plexus-converters -f .mfiles-plexus-converters
%dir %{_mavenpomdir}/%{pkg_name}
%dir %{_javadir}/%{pkg_name}
%files plexus-lifecycles -f .mfiles-plexus-lifecycles
%dir %{_mavenpomdir}/%{pkg_name}
%dir %{_javadir}/%{pkg_name}
%files plexus-locators   -f .mfiles-plexus-locators
%dir %{_mavenpomdir}/%{pkg_name}
%dir %{_javadir}/%{pkg_name}
%files plexus-metadata   -f .mfiles-plexus-metadata
%dir %{_mavenpomdir}/%{pkg_name}
%dir %{_javadir}/%{pkg_name}
%files plexus-scanners   -f .mfiles-plexus-scanners
%dir %{_mavenpomdir}/%{pkg_name}
%dir %{_javadir}/%{pkg_name}
%files plexus-shim       -f .mfiles-plexus-shim
%dir %{_mavenpomdir}/%{pkg_name}
%dir %{_javadir}/%{pkg_name}
%files inject-bean       -f .mfiles-inject-bean
%dir %{_mavenpomdir}/%{pkg_name}
%dir %{_javadir}/%{pkg_name}
%files inject-plexus     -f .mfiles-inject-plexus
%dir %{_mavenpomdir}/%{pkg_name}
%dir %{_javadir}/%{pkg_name}
%files osgi-registry     -f .mfiles-osgi-registry
%dir %{_mavenpomdir}/%{pkg_name}
%dir %{_javadir}/%{pkg_name}
%files spi-registry      -f .mfiles-spi-registry
%dir %{_mavenpomdir}/%{pkg_name}
%dir %{_javadir}/%{pkg_name}

%files javadoc -f .mfiles-javadoc
%doc LICENSE-ASL.txt LICENSE-EPL.txt


%changelog
* Thu Jan 15 2015 Michael Simacek <msimacek@redhat.com> - 2.3.0-11.13
- Add common dirs to subpackages

* Thu Jan 15 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.0-11.12
- Add directory ownership on %%{_mavenpomdir} subdir

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 2.3.0-11.11
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 2.3.0-11.10
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.0-11.9
- Mass rebuild 2014-05-26

* Thu Feb 20 2014 Michael Simacek <msimacek@redhat.com> - 2.3.0-11.8
- Set cdi-api scope to provided

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.0-11.7
- Mass rebuild 2014-02-19

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.0-11.6
- Rebuild to get rid of auto-requires on java-devel

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.0-11.5
- Mass rebuild 2014-02-18

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.0-11.4
- Remove requires on java

* Mon Feb 17 2014 Michal Srb <msrb@redhat.com> - 2.3.0-11.3
- SCL-ize BR

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.0-11.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.0-11.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 2.3.0-11
- Mass rebuild 2013-12-27

* Wed Nov 13 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.0-10
- Remove dependency on logback-classic

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.0-9
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Wed Mar 27 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.3.0-8
- Remove unneeded animal-sniffer BuildRequires
- Add forge-parent to BuildRequires to ensure it's present

* Thu Mar 14 2013 Michal Srb <msrb@redhat.com> - 2.3.0-7
- sisu-inject-bean: add dependency on asm
- Fix dependencies on javax.inject and javax.enterprise.inject
- Remove bundled JARs and .class files from tarball

* Thu Feb  7 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.0-6
- Add ASM dependency only to a single module, not all of them
- Disable animal-sniffer plugin
- Don't generate auto-requires for optional dependencies

* Wed Feb 06 2013 Tomas Radej <tradej@redhat.com> - 2.3.0-5
- Added BR on animal-sniffer

* Tue Feb 05 2013 Tomas Radej <tradej@redhat.com> - 2.3.0-4
- Split into subpackages
- Build with new macros
- Unbundled objectweb-asm

* Wed Dec  5 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.0-3
- Fix OSGi __requires_exclude

* Wed Dec  5 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.0-2
- Disable OSGi auto-requires: org.sonatype.sisu.guava

* Mon Dec  3 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.0-1
- Update to upstream version 2.3.0

* Tue Jul 24 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.3-6
- Convert patches to POM macros

* Mon Jul 23 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.3-5
- Fix license tag

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Aug 19 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.3-2
- Add backward compatible package path for lifecycles
- Remove temporary BRs/Rs

* Thu Jun 23 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.3-1
- Update to latest upstream 2.2.3 (#683795)
- Add forge-parent to Requires
- Rework spec to be more simple, update patches

* Tue Mar  1 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.1.1-2
- Add atinject into poms as dependency

* Mon Feb 28 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.1.1-1
- Update to 2.1.1
- Update patch
- Disable guice-eclipse for now

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb  2 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4.3.2-1
- Update to latest upstream version
- Versionless jars & javadocs

* Mon Oct 18 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4.2-2
- Add felix-framework BR

* Thu Oct 14 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4.2-1
- Initial version of the package
