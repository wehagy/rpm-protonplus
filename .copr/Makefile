.PHONY: prepare srpm rpm

prepare:
	dnf install --nodocs -y \
		rpmdevtools
	spectool -g $(spec)/*.spec

srpm: prepare
	rpmbuild -bs --define "_builddir ${PWD}" \
							 --define "_buildrootdir ${PWD}/.build" \
							 --define "_rpmdir ${PWD}" \
							 --define "_srcrpmdir $(outdir)" \
		           --define "_specdir ${PWD}" \
	             --define "_sourcedir ${PWD}" \
							 $(spec)/*.spec

rpm: prepare
	dnf builddep -y \
		$(spec)/*.spec
	rpmbuild -bb --define "_builddir ${PWD}" \
							 --define "_buildrootdir ${PWD}/.build" \
							 --define "_rpmdir ${PWD}" \
							 --define "_srcrpmdir $(outdir)" \
		           --define "_specdir ${PWD}" \
	             --define "_sourcedir ${PWD}" \
							 $(spec)/*.spec
								
