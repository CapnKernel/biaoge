all: dhl.ps

dhl.ps: dhl.csv biaoge.py biaoge-ps-header.txt biaoge-ps-trailer.txt
	./biaoge.py > $@

.PHONY: clean
clean:
	rm -f dhl.ps
  
