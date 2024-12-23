.PHONY: default

default:
	@echo "Usage: make [number]"

%:
	@NUM=`printf "%02d" $@`; \
	clang -o day$$NUM day$$NUM.c utils.c && cat input$$NUM.txt | ./day$$NUM

clean:
	@rm -f day[0-9][0-9]

