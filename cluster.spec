###############################################################################
###############################################################################
##
##  Copyright (C) 2004-2010 Red Hat, Inc.  All rights reserved.
##
##  This copyrighted material is made available to anyone wishing to use,
##  modify, copy, or redistribute it subject to the terms and conditions
##  of the GNU General Public License v.2.
##
###############################################################################
###############################################################################

# main (empty) package
# http://www.rpm.org/max-rpm/s1-rpm-subpack-spec-file-changes.html

# keep around ready for later user
## global alphatag rc4

Name: cluster
Summary: Red Hat Cluster
Version: 3.0.12
Release: 23%{?alphatag:.%{alphatag}}%{?dist}
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
URL: http://sources.redhat.com/cluster/wiki/
Source0: https://fedorahosted.org/releases/c/l/cluster/%{name}-%{version}.tar.bz2
Patch0: disable_ldap_loader_support.patch
Patch1: support_only_xmlconfig_loader.patch
Patch2: disable_fence_xvmd_support.patch
Patch3: cman_use_hash_cluster_id_by_default.patch
Patch4: cman_only_load_ckpt_service_by_default.patch
Patch5: cman_init_wait_for_corosync_shutdown.patch
Patch6: fenced_use_cpg_ringid.patch
Patch7: dlm_controld_wrong_fencing_time_comparison_part1.patch
Patch8: fix_ccs_tool_create.patch
Patch9: cman_fix_quorum_recalculation.patch
Patch10: add_missing_man_pages.patch
Patch11: dlm_controld_wrong_fencing_time_comparison_part2.patch
Patch12: gfs2_fix_device_name_and_mount_point_in_utils.patch
Patch13: cman_recalculate_expected_votes_on_config_reload.patch
Patch14: config_add_missing_resource_docs_to_schema.patch
Patch15: config_clean_up_recursion_in_schema.patch
Patch16: gfs2_convert_manpage_update.patch
Patch17: gfs2_edit_restoremeta_should_not_return_0_on_failure.patch
Patch18: fsck_gfs2_unaligned_access_on_ia64_part1.patch
Patch19: cman_tool_config_reload_man_page.patch
Patch20: cman_init_lsb_compliant.patch
Patch21: cman_sysconfig_part1.patch
Patch22: cman_sysconfig_part2.patch
Patch23: gfs2_init_lsb_compliant.patch
Patch24: config_update_schema.patch
Patch25: doc_autogen_cluster_conf_html_part1.patch
Patch26: doc_autogen_cluster_conf_html_part2.patch
Patch27: recalculate_quorum_on_config_change.patch
Patch28: add_tomcat_6_resource_agent_to_schema.patch
Patch29: add_tomcat_6_to_cluster_conf_html.patch
Patch30: add_missing_cman_label.patch
Patch31: add_doc_for_cman_label_attribute.patch
Patch32: allow_multiple_logging_daemon_tags.patch
Patch33: config_copy_all_logging_objects_to_the_top_level_tree.patch
Patch34: cman_recalculate_quorum_on_quorum_device_vote_changes.patch
Patch35: cman_check_config_only_once_per_sec.patch
Patch36: cman_init_allow_startup_options_to_fenced.patch
Patch37: cman_config_reload_fix_part1.patch
Patch38: cman_config_reload_fix_part2.patch
Patch39: cman_config_reload_fix_part3.patch
Patch40: cman_config_reload_fix_part4.patch
Patch41: cman_config_reload_fix_part5.patch
Patch42: cman_config_reload_fix_part6.patch
Patch43: cman_preconfig_handle_logging_reload_operation_part1.patch
Patch44: cman_preconfig_handle_logging_reload_operation_part2.patch
Patch45: controld_make_default_plock_ownership_0.patch
Patch46: dlm_controld_fix_plock_checkpoint_signatures.patch
Patch47: dlm_controld_fix_plock_owner_in_checkpoints.patch
Patch48: cman_fix_consensus_calculation.patch
Patch49: fsck_gfs2_unaligned_access_on_ia64_part2.patch
Patch50: cman_do_not_propagate_old_configurations_around.patch
Patch51: cman_clarify_man_page_on_config_distribution.patch
Patch52: gfs2_utils_mkfs_can_t_fsync_device_with_32mb_rgs.patch
Patch53: gfs2_fsck_do_not_delete_directories_if_they_get_too_big.patch

## Setup/build bits

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

# Build dependencies
BuildRequires: perl python
BuildRequires: glibc-kernheaders glibc-devel
BuildRequires: libxml2-devel ncurses-devel
BuildRequires: corosynclib-devel >= 1.2.2-1
BuildRequires: openaislib-devel >= 1.1.1-1
# BuildRequires: openldap-devel perl(ExtUtils::MakeMaker)
BuildRequires: cluster-glue-libs-devel pacemaker-libs-devel glib2-devel bzip2-devel

ExclusiveArch: i686 x86_64

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1 -b .disable_ldap_loader_support
%patch1 -p1 -b .support_only_xmlcofig_loader
%patch2 -p1 -b .disable_fence_xvmd_support
%patch3 -p1 -b .cman_use_hash_cluster_id_by_default
%patch4 -p1 -b .cman_only_load_ckpt_service_by_default
%patch5 -p1 -b .cman_init_wait_for_corosync_shutdown
%patch6 -p1 -b .fenced_use_cpg_ringid
%patch7 -p1 -b .dlm_controld_wrong_fencing_time_comparison_part1
%patch8 -p1 -b .fix_ccs_tool_create
%patch9 -p1 -b .cman_fix_quorum_recalculation
%patch10 -p1 -b .add_missing_man_pages
%patch11 -p1 -b .dlm_controld_wrong_fencing_time_comparison_part2
%patch12 -p1 -b .gfs2_fix_device_name_and_mount_point_in_utils
%patch13 -p1 -b .cman_recalculate_expected_votes_on_config_reload
%patch14 -p1 -b .config_add_missing_resource_docs_to_schema
%patch15 -p1 -b .config_clean_up_recursion_in_schema
%patch16 -p1 -b .gfs2_convert_manpage_update
%patch17 -p1 -b .gfs2_edit_restoremeta_should_not_return_0_on_failure
%patch18 -p1 -b .fsck_gfs2_unaligned_access_on_ia64_part1
%patch19 -p1 -b .cman_tool_config_reload_man_page
%patch20 -p1 -b .cman_init_lsb_compliant
%patch21 -p1 -b .cman_sysconfig_part1
%patch22 -p1 -b .cman_sysconfig_part2
%patch23 -p1 -b .gfs2_init_lsb_compliant
%patch24 -p1 -b .config_update_schema
%patch25 -p1 -b .doc_autogen_cluster_conf_html_part1
%patch26 -p1 -b .doc_autogen_cluster_conf_html_part2
%patch27 -p1 -b .recalculate_quorum_on_config_change
%patch28 -p1 -b .add_tomcat_6_resource_agent_to_schema
%patch29 -p1 -b .add_tomcat_6_to_cluster_conf_html
%patch30 -p1 -b .add_missing_cman_label
%patch31 -p1 -b .add_doc_for_cman_label_attribute
%patch32 -p1 -b .allow_multiple_logging_daemon_tags
%patch33 -p1 -b .config_copy_all_logging_objects_to_the_top_level_tree
%patch34 -p1 -b .cman_recalculate_quorum_on_quorum_device_vote_changes
%patch35 -p1 -b .cman_check_config_only_once_per_sec
%patch36 -p1 -b .cman_init_allow_startup_options_to_fenced
%patch37 -p1 -b .cman_config_reload_fix_part1
%patch38 -p1 -b .cman_config_reload_fix_part2
%patch39 -p1 -b .cman_config_reload_fix_part3
%patch40 -p1 -b .cman_config_reload_fix_part4
%patch41 -p1 -b .cman_config_reload_fix_part5
%patch42 -p1 -b .cman_config_reload_fix_part6
%patch43 -p1 -b .cman_preconfig_handle_logging_reload_operation_part1
%patch44 -p1 -b .cman_preconfig_handle_logging_reload_operation_part2
%patch45 -p1 -b .controld_make_default_plock_ownership_0
%patch46 -p1 -b .dlm_controld_fix_plock_checkpoint_signatures
%patch47 -p1 -b .dlm_controld_fix_plock_owner_in_checkpoints
%patch48 -p1 -b .cman_fix_consensus_calculation
%patch49 -p1 -b .fsck_gfs2_unaligned_access_on_ia64_part2
%patch50 -p1 -b .cman_do_not_propagate_old_configurations_around
%patch51 -p1 -b .cman_clarify_man_page_on_config_distribution
%patch52 -p1 -b .gfs2_utils_mkfs_can_t_fsync_device_with_32mb_rgs
%patch53 -p1 -b .gfs2_fsck_do_not_delete_directories_if_they_get_too_big

%build
./configure \
  --sbindir=%{_sbindir} \
  --initddir=%{_sysconfdir}/rc.d/init.d \
  --libdir=%{_libdir} \
  --enable_pacemaker \
  --without_bindings \
  --without_fence_agents \
  --without_rgmanager \
  --without_resource_agents \
  --without_kernel_modules \
  --disable_kernel_check

##CFLAGS="$(echo '%{optflags}')" make %{_smp_mflags}
CFLAGS="$(echo '%{optflags}')" make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

## tree fix up
# /etc/sysconfig/cman
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
cp cman/init.d/cman.init.defaults \
   %{buildroot}%{_sysconfdir}/sysconfig/cman
# logrotate name
mv %{buildroot}%{_sysconfdir}/logrotate.d/cluster \
	%{buildroot}%{_sysconfdir}/logrotate.d/cman
# remove static libraries
find %{buildroot} -name "*.a" -exec rm {} \;
# fix library permissions or fedora strip helpers won't work.
find %{buildroot} -name "lib*.so.*" -exec chmod 0755 {} \;
# fix lcrso permissions or fedora strip helpers won't work.
find %{buildroot} -name "*.lcrso" -exec chmod 0755 {} \;
# remove docs
rm -rf %{buildroot}/usr/share/doc/cluster
# cleanup perl bindings bits
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name perllocal.pod -exec rm -f {} \;
find %{buildroot} -type f -name '*.bs' -a -empty -exec rm -f {} \;
find %{buildroot} -type f -name CCS.so -exec chmod 755 {} \;

%clean
rm -rf %{buildroot}

## Runtime and subpackages section

# main empty package
%description
Red Hat Cluster

## subpackages

%package -n cman
Group: System Environment/Base
Summary: Red Hat Cluster Manager
Requires(post): chkconfig
Requires(preun): initscripts
Requires(preun): chkconfig
Requires: corosync >= 1.2.3-17
Requires: openais >= 1.1.1-1
# Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires: ricci >= 0.15.0-4 modcluster >= 0.15.0-3
Requires: fence-agents >= 3.0.6-1
Requires: fence-virt >= 0.2.1-1
Requires: clusterlib = %{version}-%{release}

%description -n cman
Red Hat Cluster Manager

%post -n cman
/sbin/chkconfig --add cman

# make sure to stop cman always as last
%preun -n cman
if [ "$1" = 0 ]; then
	/sbin/service cman stop >/dev/null 2>&1
	/sbin/chkconfig --del cman
fi

%files -n cman
%defattr(-,root,root,-)
%doc doc/COPYING.* doc/COPYRIGHT doc/README.licence doc/*.txt
%doc doc/cman_notify_template.sh doc/cluster_conf.html
# %doc config/plugins/ldap/*.ldif
%dir %{_sysconfdir}/cluster
%{_sysconfdir}/rc.d/init.d/cman
%dir %{_sysconfdir}/cluster/cman-notify.d
%config(noreplace) %{_sysconfdir}/logrotate.d/cman
%config(noreplace) %{_sysconfdir}/sysconfig/cman
%{_sbindir}/ccs*
%{_sbindir}/cman*
# %{_sbindir}/confdb2ldif
%{_sbindir}/dlm_controld
%{_sbindir}/dlm_tool
%{_sbindir}/fence*
%{_sbindir}/gfs_control
%{_sbindir}/gfs_controld
%{_sbindir}/group*
%{_sbindir}/*qdisk*
/usr/libexec/*
%dir %{_datadir}/cluster
%{_datadir}/cluster/cluster.rng
# %{perl_vendorarch}/*
%dir /var/log/cluster
%dir /var/lib/cluster
%dir /var/run/cluster
%{_mandir}/man5/*
%{_mandir}/man8/ccs*
%{_mandir}/man8/cman*
# %{_mandir}/man8/confdb2ldif*
%{_mandir}/man8/dlm_tool*
%{_mandir}/man8/dlm_controld.8.gz
%{_mandir}/man8/fence*
%{_mandir}/man8/gfs_control.*
%{_mandir}/man8/gfs_controld.8.gz
%{_mandir}/man8/group*
%{_mandir}/man8/*qdisk*
# %{_mandir}/man3/*.3pm.gz

%package -n clusterlib
Group: System Environment/Libraries
Summary: The Red Hat Cluster libraries
Conflicts: cman < 3.0.3-1
Provides: cmanlib = %{version}
Obsoletes: cmanlib < 3.0.0-5.alpha4

%description -n clusterlib
The Red Hat Cluster libraries package

%files -n clusterlib
%defattr(-,root,root,-)
%doc doc/COPYING.* doc/COPYRIGHT doc/README.licence
%config(noreplace) %{_sysconfdir}/udev/rules.d/*-dlm.rules
%{_libdir}/libcman.so.*
%{_libdir}/libccs*.so.*
%{_libdir}/libdlm*.so.*
%{_libdir}/libfence*.so.*
%{_libdir}/liblogthread*.so.*

%post -n clusterlib -p /sbin/ldconfig

%postun -n clusterlib -p /sbin/ldconfig

%package -n clusterlib-devel
Group: Development/Libraries
Summary: The Red Hat Cluster libraries development package
Requires: clusterlib = %{version}-%{release}
Requires: pkgconfig
Provides: cman-devel = %{version}
Obsoletes: cman-devel < 3.0.0-5.alpha4
Provides: cmanlib-devel = %{version}
Obsoletes: cmanlib-devel < 3.0.0-5.alpha4

%description -n clusterlib-devel
The Red Hat Cluster libraries development package

%files -n clusterlib-devel
%defattr(-,root,root,-)
%doc doc/COPYING.* doc/COPYRIGHT doc/README.licence
%{_libdir}/libcman.so
%{_libdir}/libccs*.so
%{_libdir}/libdlm*.so
%{_libdir}/libfence*.so
%{_libdir}/liblogthread*.so
%{_includedir}/ccs.h
%{_includedir}/libcman.h
%{_includedir}/libdlm*.h
%{_includedir}/libfence.h
%{_includedir}/libfenced.h
%{_includedir}/liblogthread.h
%{_mandir}/man3/*3.gz
%{_libdir}/pkgconfig/*.pc

%package -n dlm-pcmk
Group: System Environment/Base
Summary: DLM pacemaker integration layer
License: GPLv2+ and LGPLv2+
Requires: clusterlib = %{version}-%{release}

%description -n dlm-pcmk
The dlm-pcmk package contains the daemon that allows pacemaker
to drive the Distributed Lock Manager.

%files -n dlm-pcmk
%defattr(-,root,root,-)
%doc doc/COPYRIGHT doc/README.licence doc/COPYING.*
%{_sbindir}/dlm_controld.pcmk
%{_mandir}/man8/dlm_controld.pcmk*

%package -n gfs-pcmk
Group: System Environment/Base
Summary: GFS pacemaker integration layer
License: GPLv2+ and LGPLv2+
Requires: dlm-pcmk
Requires: clusterlib = %{version}-%{release}

%description -n gfs-pcmk
The gfs-pcmk package contains the daemon that allows pacemaker
to drive the GFS1/GFS2 File Systems.

%files -n gfs-pcmk
%defattr(-,root,root,-)
%doc doc/COPYRIGHT doc/README.licence doc/COPYING.*
%{_sbindir}/gfs_controld.pcmk
%{_mandir}/man8/gfs_controld.pcmk*

%package -n gfs2-utils
Group: System Environment/Kernel
Summary: Utilities for managing the global filesystem (GFS2)
Requires(post): chkconfig
Requires(preun): initscripts
Requires(preun): chkconfig
Requires: file

%description -n gfs2-utils
The gfs2-utils package contains a number of utilities for creating,
checking, modifying, and correcting any inconsistencies in GFS2
filesystems.

%post -n gfs2-utils
/sbin/chkconfig --add gfs2

%preun -n gfs2-utils
if [ "$1" = 0 ]; then
	/sbin/service gfs2 stop >/dev/null 2>&1
	/sbin/chkconfig --del gfs2
fi

%files -n gfs2-utils
%defattr(-,root,root,-)
%doc doc/COPYRIGHT doc/README.licence doc/COPYING.*
%{_sysconfdir}/rc.d/init.d/gfs2
/sbin/*.gfs2
%{_sbindir}/*gfs2*
%{_mandir}/man8/*gfs2*

%changelog
* Tue Aug 17 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-23
- gfs2-utils: fsck.gfs2 deletes directories if they get too big
  (gfs2_fsck_do_not_delete_directories_if_they_get_too_big.patch)
  Resolves: rhbz#624691

* Fri Aug 13 2010 Lon Hohberger <lhh@redhat.com> - Version: 3.0.12-22
- gfs2-utils: mkfs can't fsync device with 32MB RGs
  (gfs2_utils_mkfs_can_t_fsync_device_with_32mb_rgs.patch)
  Resolves: rhbz#622844

* Thu Aug 05 2010 Lon Hohberger <lhh@redhat.com> - Version: 3.0.12-21
- cman: do not propagate old configurations around
  (cman_do_not_propagate_old_configurations_around.patch)
  cman: Clarify man page on config distribution
  (cman_clarify_man_page_on_config_distribution.patch)
  Resolves: rhbz#619680

* Wed Jul 28 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-20
- Fix regression in "Fix fsck.gfs2 unaligned access on ia64" that
  affects all 32bit systems.
  Rename fsck_gfs2_unaligned_access_on_ia64.patch to
  fsck_gfs2_unaligned_access_on_ia64_part1.patch
  (fsck_gfs2_unaligned_access_on_ia64_part2.patch)
  Resolves: rhbz#608154

* Tue Jul 27 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-19
- dlm_controld/gfs_controld: make default plock_ownership 0
  Use the simpler, safer, and more reliable option as default.
  (controld_make_default_plock_ownership_0.patch)
  Resolves: rhbz#618303
- dlm_controld: fix plock checkpoint signatures
  (dlm_controld_fix_plock_checkpoint_signatures.patch)
  Resolves: rhbz#618806
- dlm_controld: fix plock owner in checkpoints
  (dlm_controld_fix_plock_owner_in_checkpoints.patch)
  Resolves: rhbz#618814
- cman: fix consensus calculation
  Bump Requires: corosync to 1.2.3-17 to guarantee that corosync
  is at the minimal version for this fix to work.
  (cman_fix_consensus_calculation.patch)
  Resolves: rhbz#618534

* Tue Jul 27 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-18
- Fix several issues related to cluster config reload operation
  including checks that would allow the config to be downgraded
  and extra spurious config reload notifications.
  (cman_config_reload_fix_part1.patch)
  (cman_config_reload_fix_part2.patch)
  (cman_config_reload_fix_part3.patch)
  (cman_config_reload_fix_part4.patch)
  (cman_config_reload_fix_part5.patch)
  (cman_config_reload_fix_part6.patch)
  Resolves: rhbz#617161, rhbz#617163
- Fix logging configuration reload operations
  (cman_preconfig_handle_logging_reload_operation_part1.patch)
  (cman_preconfig_handle_logging_reload_operation_part2.patch)
  Resolves: rhbz#615202

* Fri Jul 23 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-17
- cman init: allow startup options to fenced
  (cman_init_allow_startup_options_to_fenced.patch)
  Resolves: rhbz#617566

* Fri Jul 23 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-16
- cman: Check for new configs only once per second to avoid 100% cpu spin
  (cman_check_config_only_once_per_sec.patch)
  Resolves: rhbz#616222

* Thu Jul 22 2010 Lon Hohberger <lhh@redhat.com> - 3.0.12-15
- cman: Recalculate quorum on quorum device vote changes
  (cman_recalculate_quorum_on_quorum_device_vote_changes.patch)
  Resolves: rhbz#606989

* Mon Jul 19 2010 Lon Hohberger <lhh@redhat.com> - 3.0.12-14
- cman: Recalculate quorum on config change
  (recalculate_quorum_on_config_change.patch)
  Resolves: rhbz#606989
- config: Add tomcat-6 resource agent to schema
  (add_tomcat_6_resource_agent_to_schema.patch)
  doc: Add tomcat-6 to cluster_conf.html
  (add_tomcat_6_to_cluster_conf_html.patch)
  Resolves: rhbz#614127
- config: Add missing cman_label
  (add_missing_cman_label.patch)
  config: Add doc for cman_label attribute
  (add_doc_for_cman_label_attribute.patch)
  Resolves: rhbz#615509
- config: Allow multiple logging_daemon tags
  (allow_multiple_logging_daemon_tags.patch)
  Resolves: rhbz#614961
- cman config: copy all logging objects to the top level tree
  (config_copy_all_logging_objects_to_the_top_level_tree.patch)
  Resolves: rhbz#615202

* Mon Jul 12 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-13
- Add autogenerated cluster_conf.html
  (doc_autogen_cluster_conf_html_part1.patch)
  (doc_autogen_cluster_conf_html_part2.patch)
  Resolves: rhbz#593015
- Update relax ng schema
  (config_update_schema.patch)
  Related: rhbz#595547, rhbz#593015
- Fix patch file naming
  Related: rhbz#553383, rhbz#606368, rhbz#609978, rhbz#612097

* Fri Jul  9 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-12
- Fix gfs2 init script to be more LSB compliant
  (gfs2_init_lsb_compliant.patch)
  Resolves: rhbz#553383

* Fri Jul  9 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-11
- Add /etc/sysconfig/cman example file with extensive documentation
  of options that can be passed to the init script.
  (cman_sysconfig_part1.patch from upstream)
  (cman_sysconfig_part2.patch rhel6 specific)
  Resolves: rhbz#606368

* Fri Jul  9 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-10
- Add cman_tool version -S to man page
  (cman_tool_config_reload_man_page.patch)
  Resolves: rhbz#609978
- Fix cman init script to be more LSB compliant
  (cman_init_lsb_compliant.patch)
  Resolves: rhbz#612097

* Mon Jun 28 2010 Lon Hohberger <lhh@redhat.com> - 3.0.12-9
- Update gfs2_convert man page
  (gfs2_convert_manpage_update.patch)
  Resolves: rhbz#601315
- Don't return 0 if gfs2_edit restoremeta fails
  (gfs2_edit_restoremeta_should_not_return_0_on_failure.patch)
  Resolves: rhbz#607321
- Fix fsck.gfs2 unaligned access on ia64
  (fsck_gfs2_unaligned_access_on_ia64.patch)
  Resolves: rhbz#608154

* Fri Jun 25 2010 Lon Hohberger <lhh@redhat.com> - 3.0.12-8
- Add missing components to cluster schema
  (config_add_missing_resource_docs_to_schema.patch)
- Clean up recursion in cluster schema
  (config_clean_up_recursion_in_schema.patch)
  Resolves: rhbz#604298

* Fri Jun 25 2010 Lon Hohberger <lhh@redhat.com> - 3.0.12-7
- Ensure cman recalculates quorum on configuration reload
  (cman_recalculate_expected_votes_on_config_reload.patch)
  Resolves: rhbz#606989

* Fri May 28 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-6
- Fix device name and mount point in utils
  (gfs2_fix_device_name_and_mount_point_in_utils.patch)
  Resolves: rhbz#597002

* Fri May 28 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-5
- Fix dlm_controld wrong fencing time comparison (part2):
  Rename dlm_controld_wrong_fencing_time_comparison.patch to
  dlm_controld_wrong_fencing_time_comparison_part1.patch
  Add dlm_controld_wrong_fencing_time_comparison_part2.patch
  Resolves: rhbz#594511

* Thu May 27 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-4
- cman: fix quorum recalculation when a node is externally killed
  (cman_fix_quorum_recalculation.patch)
  Resolves: rhbz#596046
- rpmdiff automatic test tool found 2 issues:
  * add missing man pages for cman_notify, dlm_controld.pcmk and
    gfs_controld.pcmk, and update the spec file to ship them
    in the correct subpackages.
  (add_missing_man_pages.patch)
  * cman, dlm-pcmk, gfs-pcmk should have a tigher Requires on cluster
    libraries.
  Resolves: rhbz#594111

* Tue May 25 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-3
- Fix dlm_controld wrong fencing time comparison
  (dlm_controld_wrong_fencing_time_comparison.patch)
  Resolves: rhbz#594511
- Fix ccs_tool create -n
  (fix_ccs_tool_create.patch)
  Resolves: rhbz#594626

* Tue May 18 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-2
- Fix cman init script stop action to wait for corosync daemon to shutdown
  (cman_init_wait_for_corosync_shutdown.patch)
  Resolves: rhbz#592103
- fenced: use cpg ringid
  (fenced_use_cpg_ringid.patch)
  Update Requires/BuildRequires on corosync + cpg ringid patch.
  Resolves: rhbz#584140
- fix changelog entries from 3.0.12-1 (missing bugzilla entries)

* Wed May 12 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-1
- Rebase on top of new upstream bug fix only release:
  * drop all bug fix patches.
  * refresh patches with official SHA1 git commits from RHEL6
    upstream branch:
    - disable_ldap_loader_support.patch
    - support_only_xmlconfig_loader.patch
    - disable_fence_xvmd_support.patch
  * rename cman_use_hashed_cluster_id_part4.patch to
    cman_use_hash_cluster_id_by_default.patch.
  * Addresses the following issues:
    from 3.0.11 release:
  Resolves: rhbz#581047, rhbz#576330, rhbz#582017, rhbz#583945
  Resolves: rhbz#581038
    from 3.0.12 release:
  Resolves: rhbz#589823, rhbz#586100, rhbz#585083, rhbz#587079
  Resolves: rhbz#590000
  * Rebase:
  Resolves: rhbz#582322
- Stop build on ppc and ppc64.
  Resolves: rhbz#590980
- cman should only load OpenAIS checkpoint service by default
  (cman_only_load_ckpt_service_by_default.patch)
  Resolves: rhbz#568407

* Wed Apr  7 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.9-5
- Fix ccs_tool man page
  (fix_ccs_tool_man_page.patch)
  Resolves: rhbz#577874
- dlm_controld: add plock checkpoint signatures
  (dlm_controld_add_plock_checkpoint_signatures.patch)
  Resolves: rhbz#578625
- dlm_controld: set last_plock_time for ownership operations
  (dlm_controld_set_last_plock_time_for_ownership_ops.patch)
  (gfs_controld_set_last_plock_time_for_ownership_ops.patch)
  Resolves: rhbz#578626
- dlm_controld: don't skip unlinking checkpoint
  (dlm_controld_do_not_skip_unlinking_checkpoint.patch)
  Resolves: rhbz#578628
- gfs2_convert segfaults when converting fs of blocksize 512 bytes
  (gfs2_convert_fix_segfault_with_512bytes_bs.patch)
  Resolves: rhbz#579621
- gfs2_convert uses too much memory for jdata conversion
  (gfs2_convert_uses_too_much_memory_for_jdata_conversion.patch)
  Resolves: rhbz#579623
- Fix conversion of gfs1 CDPNs
  (gfs2_convert_fix_conversion_of_gfs1_cdpns.patch)
  Resolves: rhbz#579625
- gfs2_convert: Doesn't convert indirectly-pointed eattrs correctly
  (gfs2_convert_does_not_convert_eattrs_correctly.patch)
  Resolves: rhbz#579626

* Fri Mar 26 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.9-4
- Fix weakness in clusterid generation by using non-crypto hashing.
  part1-3 are he upstream generic implemetation.
  part4 turns it on specifically for RHEL-6 as the change breaks
  micro rolling upgrades.
  (cman_use_hashed_cluster_id_part1.patch)
  (cman_use_hashed_cluster_id_part2.patch)
  (cman_use_hashed_cluster_id_part3.patch)
  (cman_use_hashed_cluster_id_part4.patch)
  Resolves: rhbz#574886
- Add plock debug buffer.
  (dlm_separate_plock_debug_buffer_part1.patch)
  (dlm_separate_plock_debug_buffer_part2.patch)
  Resolves: rhbz#576322
- Add more fs_notified debugging
  (dlm_controld_add_more_fs_notified_debugging.patch)
  Resolves: rhbz#576335
- dlm_controld/gfs_controld: avoid full plock unlock when no
  resource exists
  (controld_avoid_full_plock_unlock.patch)
  Resolves: rhbz#575103

* Tue Mar 23 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.9-3
- Fix fsck.gfs2 segfault
  (gfs2_fix_segfault_osi_tree.patch)
  Resolves: rhbz#574215

* Wed Mar 10 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.9-2
- Fix gfs2_quota hadle of boundary conditions
  (gfs2_fix_quota_boundary.patch)
  Resolves: rhbz#570525
- Fix gfs_controld dm suspend event handling
  (gfs_controld_dm_suspend.patch)
  Resolves: rhbz#571806

* Mon Mar  1 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.9-1
- new upstream release:
  Resolves: rhbz#566784, rhbz#555047, rhbz#556603, rhbz#561862
  Resolves: rhbz#565907, rhbz#568446, rhbz#564471, rhbz#561416
  Resolves: rhbz#553383
- upstream rebase and patch cleanup
  Resolves: rhbz#557348
- gfs2: make use of exported device topology
  (gfs2_exported_dev_topology)
  Resolves: rhbz#519491
- spec file update:
  * cman should Requires fence-virt directly
  * merge changelog from Fedora
  * re-enable cmannotifyd support and ship doc/template

* Thu Feb 25 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.7-4
- Resolves: rhbz#567884
- Do not build cluster on s390 and s390x.

* Thu Jan 14 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.7-3
- Add workaround for corosync IPC shutdown issue (cman-init-workaround-bz547813.patch)
- Related: rhbz#547813

* Wed Jan 13 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.7-2
- Drop ldapconfig loader support (PM-disable-ldap-loader-support.patch)
- Drop notifyd support (PM-disable-notifyd-support.patch)
- Support only xmlconfig loader (PM-support-only-xmlconfig-loader.patch)
- Disable support for perl bindings

* Tue Jan 12 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.7-1
- New upstream release

* Tue Jan  6 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.6-2
- Drop gfs-utils commodity package

* Mon Dec  7 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.6-1
- New upstream release
- spec file update:
  * use global instead of define
  * use new Source0 url
  * use %name macro more aggressively
  * bump Requires on fence-agents
  * ship var/run/cluster and var/lib/cluster

* Fri Nov 20 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.5-1
- New upstream release
- spec file update:
  * drop BuildRequires on slang-devel.

* Wed Oct 21 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.4-1
- New upstream release
- spec file update:
  * explicitly Requires newer version of fence-agents

* Fri Oct  2 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.3-2
- spec file update:
  * gfs-pcmk now Requires dlm-pcmk

* Fri Sep 25 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.3-1
- New upstream release
- spec file updates:
  * drop cp_workaround patch
  * stop shipping rgmanager from cluster
  * move dlm udev rules in clusterlib where they belong
  * enable pacemaker components build
  * ship 2 new rpms: dlm-pcmk and gfs-pcmk for pacemaker integration

* Mon Aug 24 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.2-2
- Add temporary workaround to install symlinks

* Mon Aug 24 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.2-1
- New upstream release

* Thu Aug 20 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.1-1
- New upstream release

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul  8 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-20
- New upstream release
- spec file updates:
  * Update copyright header
  * final release.. undefine alphatag
  * BuildRequires and Requires corosync/openais 1.0.0-1 final.

* Thu Jul  2 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-19.rc4
- New upstream release
- spec file updates:
  * cman subpackage: avoid unnecessary calls to ldconfig
  * rgmanager subpackage: drop unrequired Requires: that belong to ras
  * BuildRequires and Requires corosync/openais 1.0.0.rc1

* Sat Jun 20 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-18.rc3
- New upstream release
- spec file updates:
  * Drop local patches.
  * Update BuildRequires and Requires: on newer corosync/openais.

* Thu Jun 11 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-17.rc2
- Update from git up to 779dd3c23ca6c56f5b3f7a8a7831bae775c85201
- spec file updates:
  * Drop BuildRequires on libvolume_id-devel that's now obsoleted
  * gfs*-utils now Requires: file
  * Add temporary patch to get rid of volume_id references in the code

* Wed Jun 10 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-16.rc2
- New upstream release + git94df30ca63e49afb1e8aeede65df8a3e5bcd0970
- spec file updates:
  * BuildRequires / Requires: latest corosync and openais
  * Update configure invokation
  * Cleanup tree fix up bits that are now upstream
  * Ship cluster.rng
  * Move fsck/mkfs gfs/gfs2 binaries in /sbin to be FHS compliant

* Tue Mar 24 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-15.rc1
- New upstream release.
- Update corosync/openais BuildRequires and Requires.
- Drop --corosynclibdir from configure. Libs are now in standard path.
- Update BuildRoot usage to preferred versions/names
- Drop qdisk init script. Now merged in cman init from upstream.

* Mon Mar  9 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-14.alpha7
- New upstream release.
- Update corosync/openais BuildRequires and Requires.
- Fix gfs-utils and cman man page overlapping files.

* Fri Mar  6 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-13.alpha7
- New upstream release.
- Drop local build fix patch.

* Tue Mar  3 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-12.alpha6
- New upstream release.
- Add missing LICENCE and COPYRIGHT files from clusterlib-devel.
- Add patch to fix build failure (already upstream).

* Tue Feb 24 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-11.alpha5
- Stop building fence and resource agents.
- cman now Requires: fence-agents.
- rgmanager now Requires: resource-agents.

* Tue Feb 24 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-10.alpha5
- Fix typo in gfs-utils preun scriptlet.
- Fix gfs-utils file list.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-9.alpha5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 23 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-8.alpha5
- New upstream release.

* Thu Feb 19 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-7.alpha4
- Update to latest stable3 code from git (e3a9ac674fa0ff025e833dcfbc8575cada369843)
- Fix Provides: version.
- Update corosync/openais BuildRequires and Requires

* Fri Feb  6 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-6.alpha4
- Fix datadir/fence directory ownership.

* Sat Jan 31 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-5.alpha4
- New upstream release.
- Fix directory ownership #483330.
- Add support pkgconfig to devel package.
- Total libraries cleanup:
  - split libraries out of cman into clusterlib.
  - merge cmanlib into clusterlib.
  - rename cman-devel into clusterlib-devel.
  - merge cmanlib-devel into clusterlib-devel.
- Comply with multiarch requirements (libraries).
- Relax BuildRequires and Requires around corosync and openais.

* Tue Jan 27 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-4.alpha3
- New upstream release

* Wed Jan 21 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-3.alpha2
- Move all binaries where they belong. All the legacy stuff is now dead.

* Mon Jan 12 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-2.alpha2
- New upstream release (retag cvs package)

* Mon Jan 12 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-1.alpha2
- New upstream release

* Wed Dec 17 2008 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-1.alpha1
- New upstream release.
- Fix legacy code build.
- Fix wrong conffile attribute.

* Mon Dec 15 2008 Fabio M. Di Nitto <fdinitto@redhat.com> - 2.99.13-1
- New upstream release.
- Drop gnbd* packages that are now a separate project.
- Tight dependencies with corosync/openais.

* Mon Dec 01 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.99.12-2
- Rebuild for Python 2.6

* Mon Nov  3 2008 Fabio M. Di Nitto <fdinitto@redhat.com> - 2.99.12-1
- new upstream release.
  Fix several security related issues.

* Mon Oct 20 2008 Fabio M. Di Nitto <fdinitto@redhat.com> - 2.99.11-1
- new upstream release.
- drop obsoleted patches.
- include very important gfs1 bug fix.
- include fix for fence_egenera (CVE-2008-4192).

* Wed Oct  8 2008 Fabio M. Di Nitto <fdinitto@redhat.com> - 2.99.10-6
- cman init: add fix from upstream for cman_tool wrong path.

* Fri Sep 26 2008 Fabio M. Di Nitto <fdinitto@redhat.com> - 2.99.10-5
- cman now Requires: ricci and modcluster.

* Fri Sep 26 2008 Fabio M. Di Nitto <fdinitto@redhat.com> - 2.99.10-4
- Split libcman.so* from cman and cman-devel into  cmanlib and cmanlib-devel
  to break a very annoying circular dependency.

* Thu Sep 25 2008 Fabio M. Di Nitto <fdinitto@redhat.com> - 2.99.10-3
- The "CVS HATES ME" release.
- New upstream release.
- Build against new corosync and openais.
- specfile cleanup: rename buildxen to buildvirt.

* Thu Sep 25 2008 Fabio M. Di Nitto <fdinitto@redhat.com> - 2.99.10-2
- Retag release.
- New upstream release.
- Build against new corosync and openais.
- specfile cleanup: rename buildxen to buildvirt.

* Thu Sep 25 2008 Fabio M. Di Nitto <fdinitto@redhat.com> - 2.99.10-1
- New upstream release.
- Build against new corosync and openais.
- specfile cleanup: rename buildxen to buildvirt.

* Wed Sep 03 2008 Jesse Keating <jkeating@redhat.com> - 2.99.08-3
- Rebuild for broken deps.
- Pull in upstream patches for libvolume_id changes

* Wed Sep 03 2008 Jesse Keating <jkeating@redhat.com> - 2.99.08-2
- Rebuild for broken deps.

* Tue Aug 12 2008 Fabio M. Di Nitto <fdinitto@redhat.com> - 2.99.08-1
- New upstream release.
- Drop local patch that's part of upstream.
- Tight BR and Requires for openais to a very specific version.
- cman Requires ricci as new default config distribution system.
  (ricci changes will land soon but in the meantime this is done our side)

* Fri Aug  1 2008 Fabio M. Di Nitto <fdinitto@redhat.com> - 2.99.07-1
- New upstream release.
- Add patch to build against new headers (already part of upstream next release)
- BR on perl(ExtUtils::MakeMaker) to build perl bindings
- Fix logrotate install from upstream
- Add "clean up after perl bindings" snippet
- Update Requires for perl bindings
- Properly split man3 man pages

* Tue Jul 15 2008 Fabio M. Di Nitto <fdinitto@redhat.com> - 2.99.06-1
- New upstream release.
- BR on new openais for logging features.
- drop local logrotate snippet in favour of upstream one.
- cman Requires: PyOpenSSL for telnet_ssl wrapper.
- cman Requires: pexpect and net-snmp-utils for fence agents.
  Thanks to sendro on IRC for spotting the issue.
- Another cleanup round for docs

* Tue Jun 24 2008 Fabio M. Di Nitto <fdinitto@redhat.com> - 2.99.05-1
- New upstream release
- Update licence tags again after upstream relicensing to kill OSL 2.1.
- Add 2 commodity packages (gfs-utils and gnbd-utils). They both
  require external kernel modules but at least userland will stay
  automatically in sync for our users.
- BR openais 0.84 for new logsys symbols (and requires for runtime).
- Update build section to enable gfs-utils and gnbd-utils.

* Mon Jun  9 2008 Fabio M. Di Nitto <fdinitto@redhat.com> - 2.99.04-1
- New upstream release
- Update license tags after major upstream cleanup (note: rgmanager
  includes a shell script that is shipped under OSL 2.1 license).
- Update inclusion of documents to reflect updated COPYRIGHT file
  from upstream.
- Add documentation to different packages.

* Mon Jun  2 2008 Fabio M. Di Nitto <fdinitto@redhat.com> - 2.99.03-1
- New upstream release
- cman Requires telnet and ssh client
- drops some tree fix up bits that are now upstream

* Fri May 23 2008 Fabio M. Di Nitto <fdinitto@redhat.com> - 2.99.02-4
- Add missing OpenIPMI requires to cman for fence_ipmilan

* Thu May 22 2008 Fabio M. Di Nitto <fdinitto@redhat.com> - 2.99.02-3
- New kernel-headers has what we need release.
- Drop BR on kernel-devel.
- Drop cluster-dlmheaders.patch.
- Drop --kernel_* from configure invokation.
- Cleanup a few comments in the spec file.

* Tue May 20 2008 Fabio M. Di Nitto <fdinitto@redhat.com> - 2.99.02-2
- disable parallel build (broken upstream)
- build requires higher openais (fix ppc64 build failure)

* Mon May 19 2008 Fabio M. Di Nitto <fdinitto@redhat.com> - 2.99.02-1
- New upstream release
- Shut up the last few rpmlint warnings

* Wed May 15 2008 Fabio M. Di Nitto <fdinitto@redhat.com> - 2.99.01-4
- Fix typo in rgmanager Summary

* Wed May 14 2008 Fabio M. Di Nitto <fdinitto@redhat.com> - 2.99.01-3
- Fix rgmanager License: tag.

* Wed May 14 2008 Fabio M. Di Nitto <fdinitto@redhat.com> - 2.99.01-2
- Drop BR on openais as it is pulled by openais-devel.
- Change postun section to use -p /sbin/ldconfig.
- Fix rgmanager Requires.

* Wed May 14 2008 Fabio M. Di Nitto <fdinitto@redhat.com> - 2.99.01-1
- Initial packaging.
