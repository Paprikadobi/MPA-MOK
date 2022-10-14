CC      = gcc
CFLAGS  = -fPIC

%.so: %.o
	$(CC) -shared $^ -o $@

.PHONY: clean
clean:
	rm -rf *.o *.so