ETC = $(DESTDIR)/etc
DOC = $(DESTDIR)/usr/share/doc

clean:

all:

install:
	mkdir -p $(ETC)/virtualmaster
	install -m 644 ./etc/virtualmaster/network-redhat.tpl $(ETC)/virtualmaster/
	install -m 644 ./etc/virtualmaster/network.tpl $(ETC)/virtualmaster/
	install -m 644 ./etc/virtualmaster/resolv.tpl $(ETC)/virtualmaster/
	install -m 644 ./etc/virtualmaster/hosts.tpl $(ETC)/virtualmaster/
	mkdir -p $(ETC)/init.d
	mkdir -p $(ETC)/rcS.d
	install -m 755 ./etc/init.d/virtualmaster-redhat $(ETC)/init.d/virtualmaster
	install -m 755 ./etc/rcS.d/S01virtualmaster $(ETC)/rcS.d/
	mkdir -p $(DOC)/virtualmaster
	install -m 644 ./usr/share/doc/virtualmaster.cfg.sample $(DOC)/virtualmaster/virtualmaster.cfg.sample
	install -m 644 ./usr/share/doc/README $(DOC)/virtualmaster/
	install -m 644 ./usr/share/doc/LICENSE $(DOC)/virtualmaster/
