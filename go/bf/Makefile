run: 
	go build -o machine && ./machine ../examples/hello_world.bf

# Speed test 
ts:
	go build -o machine && time ./machine ../examples/mandelbrot.bf >/dev/null

clear:
	rm *machine