package main

import "io"

type Machine struct {
	code string
	ip   int

	memory [30000]int
	dp     int

	input  io.Reader
	output io.Writer

	buf []byte
}

func NewMachine(code string, in io.Reader, out io.Writer) *Machine {
	return &Machine{
		code:   code,
		input:  in,
		output: out,
		buf:    make([]byte, 1),
	}
}

func (m *Machine) Execute() {
	// println(m.code)
	for m.ip < len(m.code) {
		ins := m.code[m.ip]

		switch ins {
		case '+':
			m.memory[m.dp]++
		case '-':
			m.memory[m.dp]--
		case '>':
			m.dp++
		case '<':
			m.dp--
		case '.':
			m.putChar()
		case ',':
			m.readChar()
		case '[':
			if m.memory[m.dp] == 0 {
				depth := 1
				for depth != 0 {
					m.ip++
					switch m.code[m.ip] {
					case '[':
						depth++
					case ']':
						depth--
					}
				}
			}
		case ']':
			if m.memory[m.dp] == 0 {
				depth := 1
				for depth != 0 {
					m.ip++
					switch m.code[m.ip] {
					case ']':
						depth++
					case '[':
						depth--
					}
				}
			}
		}

		m.ip++
	}
}

func (m *Machine) readChar() {
	n, err := m.input.Read(m.buf)

	if err != nil {
		panic(err)
	}
	if n != 1 {
		panic("wrong num bytes read")
	}
	m.memory[m.dp] = int(m.buf[0])
}

// TODO: Fix the memory issue in putChar to char

func (m *Machine) putChar() {
	m.buf[0] = byte(m.memory[m.dp])
	print("Memory", m.memory[1])
	n, err := m.output.Write(m.buf)

	// char := rune(m.memory[m.dp])
	// n, err := m.output.Write([]byte(string(char)))

	if err != nil {
		panic(err)
	}
	if n != 1 {
		panic("wrong num bytes written")
	}
}
