PDFS := $(patsubst %.md,../assets/%.pdf,$(wildcard *.md))
all : $(PDFS)

../assets/%.pdf : %.md
	pandoc   $<\
	  --from         markdown       \
	  --to           latex          \
	  --template     template.tex   \
	  --latex-engine xelatex        \
	-o $@
clean :
	rm $(PDFS)

rebuild : clean all